#!/usr/bin/env python3
"""Ejecuta el banco sintético R5 contra el CLI determinista."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "skills/cuadrar-tiempos-de-incidente/scripts/tabla_incidentes.py"
REGISTER = ROOT / "fixtures/registro_F1.csv"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def run_case(case: dict[str, object], temp_dir: Path) -> dict[str, object]:
    output = temp_dir / f"{case['id']}.json"
    command = [
        sys.executable,
        str(SCRIPT),
        "--registro",
        str(REGISTER),
        "--sistema",
        str(case["sistema"]),
        "--desde",
        str(case["desde"]),
        "--hasta",
        str(case["hasta"]),
        "--severidad",
        str(case["severidad"]),
        "--max-filas",
        str(case["max_filas"]),
        "--out",
        str(output),
    ]
    completed = subprocess.run(command, text=True, capture_output=True, check=False)
    payload = json.loads(output.read_text(encoding="utf-8"))
    expected = case["expected"]
    checks = {"status": payload.get("status") == expected["status"]}
    if expected["status"] in {"ok", "not_answerable"}:
        checks["row_count"] = payload.get("row_count") == expected["row_count"]
        checks["total_minutos"] = payload.get("total_minutos") == expected["total_minutos"]
    else:
        error = payload.get("error", {})
        checks["error_code"] = error.get("code") == expected["error_code"]
        checks["matched_rows"] = error.get("matched_rows") == expected["matched_rows"]
    expected_exit = 2 if expected["status"] == "error" else 0
    checks["exit_code"] = completed.returncode == expected_exit
    return {
        "id": case["id"],
        "executed_at_utc": utc_now(),
        "synthetic_case": True,
        "command_args": {
            key: case[key]
            for key in ("sistema", "desde", "hasta", "severidad", "max_filas")
        },
        "expected": expected,
        "observed": payload,
        "exit_code": completed.returncode,
        "checks": checks,
        "passed": all(checks.values()),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bank", type=Path, required=True)
    parser.add_argument("--out-results", type=Path, required=True)
    parser.add_argument("--out-report", type=Path, required=True)
    args = parser.parse_args()
    bank = json.loads(args.bank.read_text(encoding="utf-8"))
    cases = bank["cases"]
    with tempfile.TemporaryDirectory(prefix="s06-r5-") as directory:
        results = [run_case(case, Path(directory)) for case in cases]
    failures = sum(not item["passed"] for item in results)
    args.out_results.parent.mkdir(parents=True, exist_ok=True)
    args.out_results.write_text(
        "".join(json.dumps(item, ensure_ascii=False) + "\n" for item in results),
        encoding="utf-8",
    )
    report = {
        "schema": "s06-r5-format-report/v1",
        "executed_at_utc": utc_now(),
        "bank": str(args.bank),
        "bank_generated": bank["generated"],
        "bank_synthetic": bank["synthetic"],
        "evidence_scope": bank["evidence_scope"],
        "total_cases": len(results),
        "passed_cases": len(results) - failures,
        "failed_cases": failures,
        "reopen_threshold": "failed_cases > 2 of 20",
        "reopen_triggered": failures > 2,
    }
    args.out_report.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False))
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
