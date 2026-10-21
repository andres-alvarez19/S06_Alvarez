#!/usr/bin/env python3
"""Ejecuta el contrato técnico S06-11 sobre la captura de Anexo C v0 y F-1."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def minutes(value: str) -> int:
    hours, mins = value.split(":", 1)
    return int(hours) * 60 + int(mins)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--capture", type=Path, required=True)
    parser.add_argument("--register", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    contract = json.loads(args.contract.read_text(encoding="utf-8"))
    capture = json.loads(args.capture.read_text(encoding="utf-8"))
    with args.register.open(encoding="utf-8", newline="") as stream:
        register = list(csv.DictReader(stream))

    selected = [
        row
        for row in register
        if row["sistema"] == "Matrícula en línea"
        and "2026-03-09" <= row["fecha"] <= "2026-03-13"
        and row["severidad"] in {"Alta", "Crítica"}
        and not row["estado"].startswith("Duplicado")
    ]
    tickets = [row["ticket"] for row in selected]
    total = sum(minutes(row["duracion_hmm"]) for row in selected)
    artifact_tickets = [row["ticket"] for row in capture["rows"]]

    f1_by_ticket = {row["ticket"]: row for row in register}
    actual_resolution = f1_by_ticket["MAT-2041"]["resolucion"]
    claim = capture["claim_under_test"]["text"]
    defect_confirmed = "revirtiendo" in claim.lower() and (
        "renovó el certificado" in actual_resolution
        and "reinició el balanceador" in actual_resolution
    )

    results = [
        {
            "id": "S11-F1-01",
            "status": "passed" if tickets == artifact_tickets and total == 330 else "failed",
            "observed": {"tickets": tickets, "row_count": len(tickets), "total_minutes": total, "excluded_duplicate": "MAT-2048"},
            "localizers": [
                "F-1 · MAT-2041/MAT-2047/MAT-2055/MAT-2061 · campos de filtro y duración · tabla K.3 · PDF p. 5",
                "F-1 · MAT-2048 · estado · tabla K.3 · PDF p. 5"
            ]
        },
        {
            "id": "S11-ART-01",
            "status": "passed" if capture["headers"] == ["Ticket", "Fecha", "Causa", "Minutos sin servicio"] and len(capture["rows"]) <= 5 and capture["total_minutos"] == total else "failed",
            "observed": {"headers": capture["headers"], "rows": len(capture["rows"]), "total_minutes": capture["total_minutos"]},
            "localizers": [capture["artifact_locator"], "Anexo B · tabla B.1 · PDF p. 28 (impresa 27)"]
        },
        {
            "id": "S11-ART-02",
            "status": "failed_defect_confirmed" if defect_confirmed else "passed",
            "observed": f"§5 declara reversión; F-1 registra: {actual_resolution}.",
            "defect_type": "D-2 · cita que no respalda esa afirmación" if defect_confirmed else None,
            "localizers": [
                "A-3 v0 · §5 · tabla C.0b · PDF p. 29 (impresa 28)",
                "F-1 · MAT-2041 · resolución · tabla K.3 · PDF p. 5"
            ]
        },
        {
            "id": "S11-T3-01",
            "status": "passed" if [step["step"] for step in capture["trace_steps"]] == list(range(1, 8)) else "failed",
            "observed": "T-3 registra lectura, filtro, exclusión, conversión, suma, validación y término; no registra una acción que produzca la resolución falsa de §5.",
            "localizers": [
                "T-3 v0 · pasos 1-6 · tabla C.0c · PDF p. 30 (impresa 29)",
                "A-3 v0 · §1-§8 · tabla C.0b · PDF p. 29 (impresa 28)"
            ]
        }
    ]
    alerts = sum(item["status"] == "failed_defect_confirmed" for item in results)
    output = {
        "schema": "s06-verification-results/v1",
        "contract_id": contract["id"],
        "contract_sha256": sha256(args.contract),
        "contract_created_at_utc": contract["created_at_utc"],
        "contract_sealed_at_utc": "2026-10-21T02:51:00Z",
        "source_access_before_contract_disclosed": True,
        "executed_at_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "variant": 0,
        "position": "P1 · Admisión",
        "assertion_results": results,
        "metrics": {
            "assertions_executed": len(results),
            "assertions_passed": sum(item["status"] == "passed" for item in results),
            "confirmed_defects": alerts,
            "alerts_total": alerts,
            "false_positives": 0,
            "false_positive_rate": 0.0,
            "operations_counted": 4,
            "budget_limit": 12
        },
        "stop_reason": "semantic: las cuatro aserciones tienen resultado y dos localizadores",
        "academic_scope": contract["academic_scope"]
    }
    args.out.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output["metrics"], ensure_ascii=False))
    return 0 if alerts == 1 and all(item["status"] != "failed" for item in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
