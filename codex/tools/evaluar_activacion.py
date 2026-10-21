#!/usr/bin/env python3
"""Ejecuta el banco de activación con una sesión Codex aislada por caso."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

import yaml


OWN_SKILL = "cuadrar-tiempos-de-incidente"
NO_MATCH = "ninguna-skill"
REFERENCE_SKILLS = {
    "extraer-comandos-cli",
    "extraer-endpoints",
    "validar-orden-de-trabajo",
    "preparar-notas-de-version",
}


def read_jsonl(path: Path) -> list[dict[str, object]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def read_frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, flags=re.DOTALL)
    if not match:
        raise ValueError(f"frontmatter YAML ausente en {path}")
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise ValueError(f"frontmatter inválido en {path}")
    return data


def read_catalog(path: Path) -> list[dict[str, str]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    skills = payload.get("skills") if isinstance(payload, dict) else None
    if not isinstance(skills, list):
        raise ValueError("el catálogo debe contener una lista skills")
    normalized = []
    for item in skills:
        if not isinstance(item, dict) or not isinstance(item.get("name"), str) or not isinstance(item.get("description"), str):
            raise ValueError("cada skill del catálogo requiere name y description")
        normalized.append({"name": item["name"], "description": item["description"]})
    if {item["name"] for item in normalized} != REFERENCE_SKILLS:
        raise ValueError("el catálogo no contiene exactamente las cuatro skills de K.11")
    return normalized


def make_prompt(catalog: list[dict[str, str]], request: str) -> str:
    rendered = "\n".join(f'- {item["name"]}: {item["description"]}' for item in catalog)
    names = ", ".join([*(item["name"] for item in catalog), NO_MATCH])
    return (
        "Selecciona una skill solo si su descripción corresponde a la petición. "
        f"Si ninguna corresponde, selecciona {NO_MATCH}.\n"
        "Catálogo:\n"
        f"{rendered}\n\n"
        f"Petición:\n{request}\n\n"
        f"Devuelve exactamente uno de estos nombres y nada más: {names}."
    )


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def cli_version(command: str) -> str:
    completed = subprocess.run([command, "--version"], text=True, capture_output=True, check=True)
    return completed.stdout.strip()


def run_case(
    *,
    command: str,
    model: str | None,
    reasoning_effort: str,
    prompt: str,
    allowed_names: set[str],
    raw_path: Path,
) -> tuple[str, str, str]:
    with tempfile.TemporaryDirectory(prefix="s06-selector-") as tmp:
        last_message = Path(tmp) / "last_message.txt"
        args = [
            command,
            "exec",
            "--ephemeral",
            "--skip-git-repo-check",
            "--ignore-user-config",
            "--ignore-rules",
            "-C",
            tmp,
            "-s",
            "read-only",
            "--color",
            "never",
            "--output-last-message",
            str(last_message),
        ]
        if model:
            args.extend(["--model", model])
        args.extend(["-c", f'model_reasoning_effort="{reasoning_effort}"'])
        args.append(prompt)
        started_at = utc_now()
        completed = subprocess.run(args, text=True, capture_output=True, check=False)
        raw = (
            f"started_at: {started_at}\n"
            f"exit_code: {completed.returncode}\n"
            "--- stdout ---\n"
            f"{completed.stdout}\n"
            "--- stderr ---\n"
            f"{completed.stderr}"
        )
        raw_path.write_text(raw, encoding="utf-8")
        if completed.returncode != 0:
            raise RuntimeError(f"selector falló; revisar {raw_path}")
        if not last_message.is_file():
            raise RuntimeError(f"selector no produjo mensaje final; revisar {raw_path}")
        response = last_message.read_text(encoding="utf-8").strip()
        if response not in allowed_names:
            raise RuntimeError(f"respuesta no normalizable {response!r}; revisar {raw_path}")
        session_match = re.search(r"session id:\s*([0-9a-f-]+)", raw, flags=re.IGNORECASE)
        session_id = session_match.group(1) if session_match else "unreported"
        return response, started_at, session_id


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--bank", required=True, type=Path)
    result.add_argument("--skill", required=True, type=Path)
    result.add_argument("--catalog", required=True, type=Path)
    result.add_argument("--out-results", required=True, type=Path)
    result.add_argument("--out-report", required=True, type=Path)
    result.add_argument("--raw-dir", required=True, type=Path)
    result.add_argument("--codex-command", default=os.environ.get("CODEX_SELECTOR_COMMAND", "codex"))
    result.add_argument("--model", default=os.environ.get("CODEX_SELECTOR_MODEL"))
    result.add_argument(
        "--reasoning-effort",
        default=os.environ.get("CODEX_SELECTOR_REASONING_EFFORT", "none"),
    )
    result.add_argument("--jobs", type=int, default=1, help="Sesiones independientes simultáneas")
    return result


def main() -> int:
    args = parser().parse_args()
    bank = read_jsonl(args.bank)
    if len(bank) != 20 or len({case.get("id") for case in bank}) != 20:
        raise SystemExit("el banco debe contener 20 identificadores únicos")

    frontmatter = read_frontmatter(args.skill)
    if frontmatter.get("name") != OWN_SKILL or not isinstance(frontmatter.get("description"), str):
        raise SystemExit("la skill propia requiere name esperado y description textual")
    reference = read_catalog(args.catalog)
    catalog = [{"name": OWN_SKILL, "description": frontmatter["description"]}, *reference]
    allowed_names = {item["name"] for item in catalog} | {NO_MATCH}
    args.raw_dir.mkdir(parents=True, exist_ok=False)
    if args.jobs < 1:
        raise SystemExit("--jobs debe ser al menos 1")

    version = cli_version(args.codex_command)
    results_by_sequence: dict[int, dict[str, object]] = {}

    def evaluate(index: int, case: dict[str, object]) -> tuple[int, dict[str, object]]:
        case_id = case.get("id")
        request = case.get("peticion")
        if not isinstance(case_id, str) or not isinstance(request, str):
            raise ValueError("cada caso requiere id y peticion textuales")
        raw_path = args.raw_dir / f"{case_id}.txt"
        chosen, invoked_at, session_id = run_case(
            command=args.codex_command,
            model=args.model,
            reasoning_effort=args.reasoning_effort,
            prompt=make_prompt(catalog, request),
            allowed_names=allowed_names,
            raw_path=raw_path,
        )
        raw_hash = hashlib.sha256(raw_path.read_bytes()).hexdigest()
        return index, {
            "id": case_id,
            "skill_elegida": chosen,
            "evaluador": "codex-cli selector",
            "model": args.model or "codex-cli default",
            "reasoning_effort": args.reasoning_effort,
            "cli_version": version,
            "invoked_at": invoked_at,
            "session_id": session_id,
            "raw_response_ref": raw_path.as_posix(),
            "raw_response_sha256": raw_hash,
            "sequence": index,
        }

    with ThreadPoolExecutor(max_workers=args.jobs) as executor:
        futures = {
            executor.submit(evaluate, index, case): index
            for index, case in enumerate(bank, start=1)
        }
        for future in as_completed(futures):
            index, result_item = future.result()
            results_by_sequence[index] = result_item

    results = [results_by_sequence[index] for index in range(1, len(bank) + 1)]

    args.out_results.write_text(
        "".join(json.dumps(item, ensure_ascii=False) + "\n" for item in results),
        encoding="utf-8",
    )
    by_id = {item["id"]: item for item in results}
    positives = [case for case in bank if case.get("debe_activar") is True]
    negatives = [case for case in bank if case.get("debe_activar") is False]
    vp = sum(by_id[case["id"]]["skill_elegida"] == OWN_SKILL for case in positives)
    fp = sum(by_id[case["id"]]["skill_elegida"] == OWN_SKILL for case in negatives)
    passed = vp >= 9 and fp <= 1
    report = {
        "status": "passed" if passed else "failed_threshold",
        "executed": True,
        "skill_version": frontmatter.get("metadata", {}).get("version"),
        "evaluated_description": frontmatter["description"],
        "catalog_source": str(args.catalog),
        "evaluator": "codex-cli selector",
        "model": args.model or "codex-cli default",
        "reasoning_effort": args.reasoning_effort,
        "cli_version": version,
        "isolation": f"20 independent ephemeral sessions; no resume or shared history; jobs={args.jobs}",
        "total_cases": len(bank),
        "result_count": len(results),
        "raw_evidence_dir": args.raw_dir.as_posix(),
        "metrics": {
            "true_positives": vp,
            "false_positives": fp,
            "positive_total": len(positives),
            "negative_total": len(negatives),
            "vp_target": 9,
            "fp_limit": 1,
            "passed_threshold": passed,
        },
    }
    args.out_report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0 if passed else 3


if __name__ == "__main__":
    raise SystemExit(main())
