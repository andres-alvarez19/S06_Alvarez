#!/usr/bin/env python3
"""Crea el ZIP técnico S06 con inventario SHA-256 y exclusiones explícitas."""

from __future__ import annotations

import hashlib
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT / "S06_Alvarez.zip"
MANIFEST = ROOT / "MANIFEST_SHA256.txt"

EXACT = [
    "AGENTS.md",
    "README.md",
    "README_PROCEDENCIA.md",
    "AUDITORIA.md",
    "bitacora.md",
    "descartes.md",
    "fixtures/README.md",
    "fixtures/registro_F1.csv",
    "fixtures/sinteticos/formato_tablas.json",
    "evals/activacion.jsonl",
    "evals/resultados_activacion.jsonl",
    "evals/reporte_activacion.json",
    "evals/resultados_formato_tablas.jsonl",
    "evals/reporte_formato_tablas.json",
]
PATTERNS = [
    "agents/*.yaml",
    "skills/cuadrar-tiempos-de-incidente/SKILL.md",
    "skills/cuadrar-tiempos-de-incidente/scripts/*.py",
    "docs/*.md",
    "schemas/*.json",
    "evidencias/*.json",
    "evidencias/*.sha256",
    "tests/*.py",
    "codex/manifest.json",
    "codex/contracts/*.json",
    "codex/reports/S06-0[0-9].json",
    "codex/tools/*.py",
    "evals/raw_activation/20261021T013409Z_gpt-5.6-luna-none_v1.1.0/*.txt",
]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def members() -> list[Path]:
    selected = {ROOT / item for item in EXACT}
    for pattern in PATTERNS:
        selected.update(ROOT.glob(pattern))
    missing = [path for path in selected if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"Faltan miembros requeridos: {missing}")
    forbidden = [
        path for path in selected
        if ".local_sources" in path.parts or path.suffix.lower() == ".pdf"
    ]
    if forbidden:
        raise ValueError(f"Fuentes privadas prohibidas en el paquete: {forbidden}")
    return sorted(selected, key=lambda path: path.relative_to(ROOT).as_posix())


def main() -> int:
    selected = members()
    MANIFEST.write_text(
        "".join(
            f"{digest(path)}  {path.relative_to(ROOT).as_posix()}\n"
            for path in selected
        ),
        encoding="utf-8",
    )
    with zipfile.ZipFile(ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED) as package:
        for path in selected:
            package.write(path, path.relative_to(ROOT).as_posix())
        package.write(MANIFEST, MANIFEST.name)
    with zipfile.ZipFile(ARCHIVE) as package:
        bad = package.testzip()
        if bad is not None:
            raise RuntimeError(f"Miembro corrupto: {bad}")
        names = package.namelist()
    print(f"created={ARCHIVE.name} members={len(names)} sha256={digest(ARCHIVE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
