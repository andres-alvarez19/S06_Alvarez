"""Compuertas técnicas del contrato S06-10."""

from __future__ import annotations

import hashlib
import json
import zipfile
from datetime import datetime
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
R4_HASHES = {
    "skills/cuadrar-tiempos-de-incidente/SKILL.md": "b77ff89aa9356d8533c568a7abd162bc8447af0422d2132fa1980264ac35b443",
    "evals/activacion.jsonl": "bd22ed4cd1325f19be83669f7672c40355dd8caa31fe208dc017e029388b60db",
    "evals/resultados_activacion.jsonl": "0d7cf73a77d3c9948ace90cbc9a82fd50d01a655e68c10ffc91ad46d38505270",
    "evals/reporte_activacion.json": "fc29a8bf26b6959b80adf4af8fa4a3091b3b8c220608859cd00f6a7b9977476a",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_evidencia_r4_permanece_identica() -> None:
    assert {path: sha256(ROOT / path) for path in R4_HASHES} == R4_HASHES


def test_contrato_s10_precede_verificacion_actual_sin_fingir_historia() -> None:
    contract_path = ROOT / "evidencias/contrato_cierre_integral_R3.json"
    contract = json.loads(contract_path.read_text(encoding="utf-8"))
    results = json.loads(
        (ROOT / "evidencias/verificacion_cierre_integral_R3.json").read_text(
            encoding="utf-8"
        )
    )
    assert sha256(contract_path) == results["contract_sha256"]
    seal = (ROOT / "evidencias/contrato_cierre_integral_R3.sha256").read_text(
        encoding="utf-8"
    )
    assert results["contract_sha256"] in seal
    parse = lambda value: datetime.fromisoformat(value.replace("Z", "+00:00"))
    assert parse(results["contract_created_at_utc"]) < parse(results["contract_sealed_at_utc"])
    assert parse(results["contract_sealed_at_utc"]) < parse(results["source_access_at_utc"])
    assert parse(results["source_access_at_utc"]) < parse(results["executed_at_utc"])
    assert "ya fue leído" in contract["historical_access_disclosure"]
    assert "No sustituye" in contract["academic_scope"]


def test_hallazgo_s10_tiene_traza_metricas_y_dos_localizadores() -> None:
    results = json.loads(
        (ROOT / "evidencias/verificacion_cierre_integral_R3.json").read_text(
            encoding="utf-8"
        )
    )
    by_id = {item["id"]: item for item in results["assertion_results"]}
    assert set(by_id) == {"S10-F1-01", "S10-ART-01", "S10-ART-02", "S10-T3-01"}
    assert all(len(item["localizers"]) >= 2 for item in by_id.values())
    assert by_id["S10-ART-02"]["status"] == "failed_defect_confirmed"
    assert by_id["S10-T3-01"]["status"] == "passed"
    assert results["metrics"]["confirmed_defects"] == 1
    assert results["metrics"]["false_positives"] == 0


def test_yaml_s10_no_tiene_pendientes_y_terminos_son_operacionales() -> None:
    for filename in ("generador.yaml", "verificador.yaml"):
        data = yaml.safe_load((ROOT / "agents" / filename).read_text(encoding="utf-8"))
        serialized = yaml.safe_dump(data, allow_unicode=True)
        assert "PENDIENTE" not in serialized
        assert data["context_policy"]["isolation"] in {
            "minimal_and_isolated",
            "isolated_from_generator",
        }
        assert data["allowed_tools"] and len(data["allowed_tools"]) <= 5
        stops = {item["kind"]: item for item in data["stop_conditions"]}
        assert set(stops) == {"semantic", "budget", "no_progress"}
        assert all(
            isinstance(item["threshold"], int) and item["threshold"] > 0
            for item in stops.values()
        )


def test_banco_sintetico_r5_es_declarado_y_resultados_son_reales() -> None:
    bank = json.loads(
        (ROOT / "fixtures/sinteticos/formato_tablas.json").read_text(encoding="utf-8")
    )
    results = [
        json.loads(line)
        for line in (ROOT / "evals/resultados_formato_tablas.jsonl")
        .read_text(encoding="utf-8")
        .splitlines()
        if line.strip()
    ]
    report = json.loads(
        (ROOT / "evals/reporte_formato_tablas.json").read_text(encoding="utf-8")
    )
    assert bank["generated"] is True and bank["synthetic"] is True
    assert len(bank["cases"]) == len(results) == report["total_cases"] == 20
    assert all(item["synthetic_case"] is True and item["passed"] for item in results)
    assert report["passed_cases"] == 20 and report["failed_cases"] == 0
    assert report["reopen_triggered"] is False


def test_paquete_zip_coincide_con_manifest_y_excluye_fuentes_privadas() -> None:
    archive = ROOT / "S06_Alvarez.zip"
    assert archive.is_file()
    with zipfile.ZipFile(archive) as package:
        names = set(package.namelist())
        required = {
            "bitacora.md", "agents/generador.yaml", "agents/verificador.yaml",
            "skills/cuadrar-tiempos-de-incidente/SKILL.md",
            "skills/cuadrar-tiempos-de-incidente/scripts/tabla_incidentes.py",
            "evals/activacion.jsonl", "evals/resultados_activacion.jsonl",
            "evals/reporte_activacion.json", "descartes.md", "MANIFEST_SHA256.txt"
        }
        assert names == required
        assert not any(
            name.startswith((".local_sources/", "codex/", "tests/", "__pycache__/"))
            or name.endswith((".pdf", ".zip"))
            for name in names
        )
        manifest = package.read("MANIFEST_SHA256.txt").decode("utf-8").splitlines()
        for line in manifest:
            digest, member = line.split("  ", 1)
            assert member in names
            assert hashlib.sha256(package.read(member)).hexdigest() == digest
