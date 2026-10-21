#!/usr/bin/env python3
"""Valida y calcula una corrida real importada; no simula elecciones."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


EXPECTED_SKILLS = {
    "cuadrar-tiempos-de-incidente",
    "extraer-comandos-cli",
    "extraer-endpoints",
    "validar-orden-de-trabajo",
    "preparar-notas-de-version",
}


def read_jsonl(path: Path) -> list[dict[str, object]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", required=True, type=Path)
    parser.add_argument("--bank", required=True, type=Path)
    parser.add_argument("--responses", required=True, type=Path)
    parser.add_argument("--evaluator", required=True)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()

    catalog = json.loads(args.catalog.read_text(encoding="utf-8"))
    descriptions = {item.get("name"): item.get("description") for item in catalog}
    if set(descriptions) != EXPECTED_SKILLS or any(not value for value in descriptions.values()):
        raise SystemExit("catálogo incompleto: se requieren cinco nombres y descripciones fuente no vacías")

    bank = read_jsonl(args.bank)
    responses = read_jsonl(args.responses)
    if len(responses) != len(bank):
        raise SystemExit("la corrida debe contener una respuesta real por petición")
    by_id = {item["id"]: item for item in responses}
    if set(by_id) != {item["id"] for item in bank}:
        raise SystemExit("los identificadores de respuestas no coinciden con el banco")
    for response in responses:
        if not response.get("skill_elegida") or not response.get("evaluador"):
            raise SystemExit("cada respuesta requiere skill_elegida y evaluador")
        if response["skill_elegida"] not in EXPECTED_SKILLS:
            raise SystemExit("skill_elegida fuera del catálogo")

    positives = [case for case in bank if case["debe_activar"]]
    negatives = [case for case in bank if not case["debe_activar"]]
    vp = sum(by_id[case["id"]]["skill_elegida"] == "cuadrar-tiempos-de-incidente" for case in positives)
    fp = sum(by_id[case["id"]]["skill_elegida"] == "cuadrar-tiempos-de-incidente" for case in negatives)
    report = {
        "status": "completed",
        "executed": True,
        "evaluator": args.evaluator,
        "total_cases": len(bank),
        "result_count": len(responses),
        "metrics": {
            "true_positives": vp,
            "false_positives": fp,
            "positive_total": len(positives),
            "negative_total": len(negatives),
            "vp_target": 9,
            "fp_limit": 1,
        },
    }
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

