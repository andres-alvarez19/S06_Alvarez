#!/usr/bin/env python3
"""Crea el ZIP mínimo S06 con inventario SHA-256 y exclusiones explícitas."""

from __future__ import annotations

import hashlib
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT / "S06_Alvarez.zip"
MANIFEST = ROOT / "MANIFEST_SHA256.txt"

EXACT = [
    "bitacora.md",
    "descartes.md",
    "evals/activacion.jsonl",
    "evals/resultados_activacion.jsonl",
    "evals/reporte_activacion.json",
]
PATTERNS = [
    "agents/*.yaml",
    "skills/cuadrar-tiempos-de-incidente/SKILL.md",
    "skills/cuadrar-tiempos-de-incidente/scripts/*.py",
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
    forbidden_parts = {"codex", "tests", "__pycache__", ".local_sources"}
    forbidden = [path for path in selected if forbidden_parts & set(path.parts) or path.suffix.lower() in {".pdf", ".zip"}]
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
