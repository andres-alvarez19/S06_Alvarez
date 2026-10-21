"""Pruebas funcionales del procesador F-1."""

from __future__ import annotations

import csv
import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/cuadrar-tiempos-de-incidente/scripts/tabla_incidentes.py"
FIXTURE = ROOT / "fixtures/registro_F1.csv"


def run_cli(tmp_path: Path, **overrides: object) -> tuple[subprocess.CompletedProcess[str], dict[str, object]]:
    out = tmp_path / "out.json"
    values = {
        "registro": FIXTURE,
        "sistema": "Matrícula en línea",
        "desde": "2026-03-09",
        "hasta": "2026-03-13",
        "severidad": "Alta,Crítica",
        "max_filas": 5,
    }
    values.update(overrides)
    command = [
        sys.executable,
        str(SCRIPT),
        "--registro",
        str(values["registro"]),
        "--sistema",
        str(values["sistema"]),
        "--desde",
        str(values["desde"]),
        "--hasta",
        str(values["hasta"]),
        "--severidad",
        str(values["severidad"]),
        "--max-filas",
        str(values["max_filas"]),
        "--out",
        str(out),
    ]
    completed = subprocess.run(command, text=True, capture_output=True, check=False)
    return completed, json.loads(out.read_text(encoding="utf-8"))


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def fixture_rows() -> tuple[list[str], list[dict[str, str]]]:
    with FIXTURE.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def test_exito_cuatro_filas_y_330_minutos(tmp_path: Path) -> None:
    completed, payload = run_cli(tmp_path)
    assert completed.returncode == 0
    assert payload["status"] == "ok"
    assert payload["row_count"] == 4
    assert payload["total_minutos"] == 330
    tickets = {row["ticket"] for row in payload["rows"]}
    assert tickets == {"MAT-2041", "MAT-2047", "MAT-2055", "MAT-2061"}
    assert {"MAT-2048", "COR-0388", "MAT-2066"}.isdisjoint(tickets)


def test_fecha_16_correo_y_duplicados_quedan_excluidos(tmp_path: Path) -> None:
    _, payload = run_cli(tmp_path)
    rows = payload["rows"]
    assert all(row["fecha"] <= "2026-03-13" for row in rows)
    assert all(row["sistema"] == "Matrícula en línea" for row in rows)
    assert all(not row["estado"].startswith("Duplicado de") for row in rows)


def test_sin_coincidencias_es_not_answerable(tmp_path: Path) -> None:
    completed, payload = run_cli(tmp_path, sistema="Sistema inexistente")
    assert completed.returncode == 0
    assert payload["status"] == "not_answerable"
    assert payload["row_count"] == 0 and payload["rows"] == []


def test_formato_hmm_invalido(tmp_path: Path) -> None:
    fields, rows = fixture_rows()
    rows[0]["duracion_hmm"] = "1:75"
    malformed = tmp_path / "malformed.csv"
    write_csv(malformed, rows, fields)
    completed, payload = run_cli(tmp_path, registro=malformed)
    assert completed.returncode == 2
    assert payload["status"] == "error"
    assert payload["error"]["code"] == "invalid_duration"


def test_campos_faltantes(tmp_path: Path) -> None:
    fields, rows = fixture_rows()
    fields.remove("causa")
    missing = tmp_path / "missing.csv"
    write_csv(missing, [{key: value for key, value in row.items() if key != "causa"} for row in rows], fields)
    completed, payload = run_cli(tmp_path, registro=missing)
    assert completed.returncode == 2
    assert payload["error"]["code"] == "missing_fields"
    assert payload["error"]["missing"] == ["causa"]


def test_presupuesto_no_trunca(tmp_path: Path) -> None:
    completed, payload = run_cli(tmp_path, max_filas=3)
    assert completed.returncode == 2
    assert payload["error"]["code"] == "row_budget_exceeded"
    assert payload["error"]["matched_rows"] == 4
    assert "rows" not in payload

