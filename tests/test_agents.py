"""Validador de fichas R3; una plantilla pendiente nunca se aprueba."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml


ROOT = Path(__file__).resolve().parents[1]
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


def load_agent(path: Path) -> dict[str, object]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    return data


def validate_complete_agent(data: dict[str, object]) -> None:
    missing = REQUIRED - data.keys()
    if missing:
        raise ValueError(f"campos ausentes: {sorted(missing)}")

    serialized = yaml.safe_dump(data, allow_unicode=True)
    if "PENDIENTE" in serialized:
        raise ValueError("la ficha conserva campos PENDIENTE")

    stops = data.get("stop_conditions")
    if not isinstance(stops, list) or len(stops) != 3:
        raise ValueError("se requieren exactamente tres condiciones de término")
    by_kind = {item.get("kind"): item for item in stops if isinstance(item, dict)}
    if set(by_kind) != {"semantic", "budget", "no_progress"}:
        raise ValueError("faltan condiciones semantic, budget o no_progress")
    if not isinstance(by_kind["budget"].get("threshold"), int):
        raise ValueError("budget requiere umbral entero")
    if not isinstance(by_kind["no_progress"].get("threshold"), int):
        raise ValueError("no_progress requiere umbral entero")


@pytest.mark.parametrize("filename", ["generador.yaml", "verificador.yaml"])
def test_plantillas_tienen_campos_pero_no_se_aprueban(filename: str) -> None:
    data = load_agent(ROOT / "agents" / filename)
    assert REQUIRED <= data.keys()
    with pytest.raises(ValueError, match="PENDIENTE"):
        validate_complete_agent(data)


def test_verificador_es_adversarial_aislado_y_solo_lectura_recalculo() -> None:
    generator = load_agent(ROOT / "agents/generador.yaml")
    verifier = load_agent(ROOT / "agents/verificador.yaml")
    assert verifier["id"] != generator["id"]
    assert verifier["adversarial_to"] == generator["id"]
    assert verifier["context_policy"]["isolation"] == "isolated_from_generator"
    assert {"read_artifact", "read_trace", "recalculate"} <= set(verifier["allowed_tools"])
    assert verifier["success_metric"]["name"] == "defectos_confirmados"


def test_validador_rechaza_condicion_vaga() -> None:
    sample = load_agent(ROOT / "agents/verificador.yaml")
    sample = dict(sample)
    sample["template_status"] = "complete"
    text = yaml.safe_dump(sample, allow_unicode=True).replace("PENDIENTE", "definido")
    sample = yaml.safe_load(text)
    sample["stop_conditions"][0]["threshold"] = 1
    sample["stop_conditions"][1]["threshold"] = 10
    sample["stop_conditions"][2]["threshold"] = None
    with pytest.raises(ValueError, match="no_progress requiere umbral entero"):
        validate_complete_agent(sample)

