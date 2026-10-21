"""Validación estructural de la entrega S06.

Este módulo también se puede ejecutar directamente. Su salida distingue entre
estructura inexistente (fail), estructura presente con evidencias restringidas
pendientes (partial) y estructura completa (passed).
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def validate_submission(root: Path) -> dict[str, object]:
    required = [
        "bitacora.md",
        "agents/generador.yaml",
        "agents/verificador.yaml",
        "skills/cuadrar-tiempos-de-incidente/SKILL.md",
        "evals/activacion.jsonl",
        "descartes.md",
    ]
    missing = [path for path in required if not (root / path).is_file()]
    if missing:
        return {"status": "failed", "missing": missing, "pending": []}

    bitacora = (root / "bitacora.md").read_text(encoding="utf-8")
    pending = []
    for marker in (
        "Matrícula completa: **PENDIENTE",
        "Comparación R1/R2: **PENDIENTE",
        "Hallazgo que enfrenta",
        "**PENDIENTE DE VERIFICACIÓN PERSONAL**",
    ):
        if marker in bitacora:
            pending.append(marker)
    return {
        "status": "partial" if pending else "passed",
        "missing": [],
        "pending": pending,
    }


def test_bitacora_identifica_variante_p1_y_no_fabrica_resultados() -> None:
    text = (ROOT / "bitacora.md").read_text(encoding="utf-8")
    assert "Variante: **0**" in text
    assert "Puesto: **P1 · Admisión**" in text
    assert "Modalidad: **autónoma con transcripciones**" in text
    assert "Matrícula completa: **21004816220**" in text
    assert "Tabla 6.A" in text and "Tabla 6.B" in text
    assert "## R4" in text and "## R5" in text


def test_validador_detecta_faltantes(tmp_path: Path) -> None:
    result = validate_submission(tmp_path)
    assert result["status"] == "failed"
    assert result["missing"]


if __name__ == "__main__":
    print(json.dumps(validate_submission(ROOT), ensure_ascii=False, indent=2))

