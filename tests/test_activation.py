"""Pruebas del banco y coherencia de métricas de activación."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_jsonl(path: Path) -> list[dict[str, object]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def test_banco_exacto_y_casos_cercanos() -> None:
    bank = read_jsonl(ROOT / "evals/activacion.jsonl")
    assert len(bank) == 20
    assert len({case["id"] for case in bank}) == 20
    assert sum(case["debe_activar"] is True for case in bank) == 10
    assert sum(case["debe_activar"] is False for case in bank) == 10
    assert sum(case["cercano"] is True and case["debe_activar"] is False for case in bank) >= 3
    assert all(set(case) == {"id", "peticion", "debe_activar", "cercano"} for case in bank)


def test_resultados_y_reporte_son_coherentes() -> None:
    bank = read_jsonl(ROOT / "evals/activacion.jsonl")
    results = read_jsonl(ROOT / "evals/resultados_activacion.jsonl")
    report = json.loads((ROOT / "evals/reporte_activacion.json").read_text(encoding="utf-8"))
    if results:
        assert len(results) == len(bank) == 20
        assert report["executed"] is True
        by_id = {item["id"]: item for item in results}
        vp = sum(
            by_id[case["id"]]["skill_elegida"] == "cuadrar-tiempos-de-incidente"
            for case in bank
            if case["debe_activar"]
        )
        fp = sum(
            by_id[case["id"]]["skill_elegida"] == "cuadrar-tiempos-de-incidente"
            for case in bank
            if not case["debe_activar"]
        )
        assert report["metrics"]["true_positives"] == vp
        assert report["metrics"]["false_positives"] == fp
    else:
        assert report["status"] == "blocked"
        assert report["executed"] is False
        assert report["result_count"] == 0
        assert report["metrics"]["true_positives"] is None
        assert report["metrics"]["false_positives"] is None
        assert report["evaluator"] is None


def test_no_se_declara_umbral_cumplido_sin_corrida() -> None:
    report = json.loads((ROOT / "evals/reporte_activacion.json").read_text(encoding="utf-8"))
    if not report["executed"]:
        assert report["status"] != "passed"
        assert "passed_threshold" not in report

