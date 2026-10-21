"""Contratos y políticas del cierre técnico asistido S06-09."""

from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime
from pathlib import Path

import pytest
import yaml


ROOT = Path(__file__).resolve().parents[1]
AGENT_FILES = ("generador.yaml", "verificador.yaml")
REQUIRED = {
    "id",
    "version",
    "purpose",
    "exists_because",
    "adversarial_to",
    "use_when",
    "do_not_use_when",
    "input_schema_ref",
    "output_schema_ref",
    "allowed_tools",
    "permissions",
    "context_policy",
    "memory_write",
    "forbidden",
    "on_failure",
    "stop_conditions",
    "success_metric",
    "evals",
}
ALLOWED_REASONS = {
    "responsabilidad independiente con salida propia y verificable",
    "aislamiento de contexto o de datos que no deben mezclarse",
    "permisos o herramientas distintos de los del resto",
    "verificación adversarial",
    "especialización evaluable con contrato de salida propio",
    "trabajo paralelo realmente divisible en frentes independientes",
    "traspaso deliberado de propiedad de la tarea",
}


def load_yaml(filename: str) -> dict[str, object]:
    data = yaml.safe_load((ROOT / "agents" / filename).read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    return data


def load_results() -> dict[str, object]:
    return json.loads(
        (ROOT / "evidencias/resultados_tecnicos_R1_R3.json").read_text(
            encoding="utf-8"
        )
    )


@pytest.mark.parametrize("filename", AGENT_FILES)
def test_agent_yaml_es_sintactico_y_semanticamente_completo(filename: str) -> None:
    data = load_yaml(filename)
    assert REQUIRED <= data.keys()
    serialized = yaml.safe_dump(data, allow_unicode=True)
    assert "PENDIENTE" not in serialized
    assert data["exists_because"] in ALLOWED_REASONS
    assert 1 <= len(data["allowed_tools"]) <= 5
    assert data["permissions"]["side_effects"] is False
    assert data["on_failure"]["reason_codes"]
    assert data["on_failure"]["payload_required"]
    for ref_key in ("input_schema_ref", "output_schema_ref"):
        schema_path = ROOT / data[ref_key]
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        assert schema["$schema"].endswith("2020-12/schema")
        assert schema["type"] == "object"

    stops = data["stop_conditions"]
    assert isinstance(stops, list) and len(stops) == 3
    by_kind = {stop["kind"]: stop for stop in stops}
    assert set(by_kind) == {"semantic", "budget", "no_progress"}
    assert all(
        isinstance(stop["threshold"], int) and stop["threshold"] > 0
        for stop in by_kind.values()
    )


def test_verificador_es_independiente_adversarial_y_acotado() -> None:
    generator = load_yaml("generador.yaml")
    verifier = load_yaml("verificador.yaml")
    assert verifier["id"] != generator["id"]
    assert verifier["adversarial_to"] == generator["id"]
    assert verifier["context_policy"]["isolation"] == "isolated_from_generator"
    assert set(verifier["allowed_tools"]) == {
        "read_artifact",
        "read_trace",
        "read_source",
        "recalculate",
    }
    assert verifier["permissions"]["write"] == [
        "project:WORK/hallazgos_contexto.json"
    ]
    assert verifier["success_metric"]["name"] == (
        "confirmed_defects_with_false_positive_rate"
    )


def test_contrato_fue_sellado_antes_de_la_ejecucion_actual() -> None:
    contract_path = ROOT / "evidencias/contrato_automatizado_R3.json"
    contract = json.loads(contract_path.read_text(encoding="utf-8"))
    results = load_results()
    digest = hashlib.sha256(contract_path.read_bytes()).hexdigest()
    assert digest == results["r3"]["contract_sha256"]

    seal = (ROOT / "evidencias/contrato_automatizado_R3.sha256").read_text(
        encoding="utf-8"
    )
    assert digest in seal
    assert datetime.fromisoformat(results["r3"]["contract_sealed_at"]) < (
        datetime.fromisoformat(results["executed_at"])
    )
    assert contract["academic_scope"].startswith("No sustituye")
    assert results["r3"]["automated_precedence_only"] is True


def test_asercion_de_traza_y_hallazgo_tienen_dos_localizadores() -> None:
    r3 = load_results()["r3"]
    by_id = {item["id"]: item for item in r3["assertion_results"]}
    trace = by_id["A-T3-01"]
    assert trace["status"] == "passed"
    assert len(trace["localizers"]) == 2
    assert all("T-3 v2 · paso" in locator for locator in trace["localizers"])

    defect = by_id["A-ART-02"]
    assert defect["status"] == "failed_defect_confirmed"
    assert defect["defect_type"].startswith("D-1")
    assert len(defect["localizers"]) == 2
    assert r3["metrics"]["confirmed_defects"] == 1
    assert r3["metrics"]["false_positives"] == 0


def test_recalculo_f1_coincide_con_asercion_sellada() -> None:
    with (ROOT / "fixtures/registro_F1.csv").open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    selected = [
        row
        for row in rows
        if row["sistema"] == "Matrícula en línea"
        and "2026-03-09" <= row["fecha"] <= "2026-03-13"
        and row["severidad"] in {"Alta", "Crítica"}
        and not row["estado"].startswith("Duplicado")
    ]
    minutes = sum(
        int(row["duracion_hmm"].split(":")[0]) * 60
        + int(row["duracion_hmm"].split(":")[1])
        for row in selected
    )
    observed = load_results()["r3"]["assertion_results"][0]["observed"]
    assert [row["ticket"] for row in selected] == observed["tickets"]
    assert len(selected) == observed["row_count"] == 4
    assert minutes == observed["total_minutes"] == 330


def test_conteos_c1_derivan_de_los_cinco_requisitos_del_anexo_b() -> None:
    c1 = load_results()["c1"]
    requirements = c1["requirements"]
    assert c1["criteria_source"].startswith(
        "S06_complemento_estudiante.pdf · Anexo B · tabla B.1"
    )
    assert [(item["id"], item["name"]) for item in requirements] == [
        ("R1", "Formato"),
        ("R2", "Alcance"),
        ("R3", "Exclusión"),
        ("R4", "Evidencia"),
        ("R5", "Presupuesto"),
    ]
    assert sum(item["round_1"] for item in requirements) == c1["round_1_score"] == 2
    assert sum(item["round_2"] for item in requirements) == c1["round_2_score"] == 5
    assert all(item["round_1_first_loss"] for item in requirements if not item["round_1"])
