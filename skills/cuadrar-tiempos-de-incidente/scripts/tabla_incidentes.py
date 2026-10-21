#!/usr/bin/env python3
"""Filtra el registro F-1 y totaliza duraciones h:mm de forma determinista."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import date
from pathlib import Path
from typing import NoReturn


REQUIRED_FIELDS = {
    "ticket",
    "fecha",
    "sistema",
    "severidad",
    "duracion_hmm",
    "estado",
    "causa",
    "resolucion",
}


class InputError(ValueError):
    """Error de entrada que se comunica como JSON estructurado."""

    def __init__(self, code: str, message: str, **details: object) -> None:
        super().__init__(message)
        self.code = code
        self.message = message
        self.details = details


def parse_date(value: str, field: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise InputError("invalid_date", f"{field} no es una fecha ISO válida", value=value) from exc


def parse_hmm(value: str, *, row_number: int) -> int:
    parts = value.split(":")
    if len(parts) != 2 or not all(part.isdigit() for part in parts):
        raise InputError(
            "invalid_duration",
            "duracion_hmm debe tener formato h:mm",
            row_number=row_number,
            value=value,
        )
    hours, minutes = (int(part) for part in parts)
    if minutes >= 60:
        raise InputError(
            "invalid_duration",
            "los minutos deben estar entre 00 y 59",
            row_number=row_number,
            value=value,
        )
    return hours * 60 + minutes


def read_rows(path: Path) -> list[dict[str, str]]:
    try:
        handle = path.open("r", encoding="utf-8", newline="")
    except OSError as exc:
        raise InputError("unreadable_record", "no se pudo abrir el registro", path=str(path)) from exc
    with handle:
        reader = csv.DictReader(handle)
        fields = set(reader.fieldnames or [])
        missing = sorted(REQUIRED_FIELDS - fields)
        if missing:
            raise InputError("missing_fields", "faltan campos requeridos", missing=missing)
        return [dict(row) for row in reader]


def build_table(
    *,
    registro: Path,
    sistema: str,
    desde: date,
    hasta: date,
    severidades: set[str],
    max_filas: int,
) -> dict[str, object]:
    if desde > hasta:
        raise InputError("invalid_range", "--desde no puede ser posterior a --hasta")
    if max_filas < 1:
        raise InputError("invalid_budget", "--max-filas debe ser al menos 1", max_filas=max_filas)
    if not severidades:
        raise InputError("invalid_severity", "--severidad debe contener al menos un valor")

    selected: list[dict[str, object]] = []
    for row_number, row in enumerate(read_rows(registro), start=2):
        row_date = parse_date(row["fecha"].strip(), f"fecha en fila {row_number}")
        if row["estado"].strip().casefold().startswith("duplicado de"):
            continue
        if row["sistema"].strip() != sistema:
            continue
        if not desde <= row_date <= hasta:
            continue
        if row["severidad"].strip() not in severidades:
            continue
        minutes = parse_hmm(row["duracion_hmm"].strip(), row_number=row_number)
        selected.append(
            {
                "ticket": row["ticket"],
                "fecha": row["fecha"],
                "sistema": row["sistema"],
                "severidad": row["severidad"],
                "duracion_hmm": row["duracion_hmm"],
                "duracion_minutos": minutes,
                "estado": row["estado"],
                "causa": row["causa"],
                "resolucion": row["resolucion"],
            }
        )

    if len(selected) > max_filas:
        raise InputError(
            "row_budget_exceeded",
            "las coincidencias superan --max-filas; no se truncó la salida",
            matched_rows=len(selected),
            max_filas=max_filas,
        )

    filters = {
        "sistema": sistema,
        "desde": desde.isoformat(),
        "hasta": hasta.isoformat(),
        "severidades": sorted(severidades),
        "max_filas": max_filas,
    }
    if not selected:
        return {
            "status": "not_answerable",
            "reason": "no_matching_records",
            "filters": filters,
            "row_count": 0,
            "total_minutos": 0,
            "rows": [],
        }
    return {
        "status": "ok",
        "filters": filters,
        "row_count": len(selected),
        "total_minutos": sum(int(row["duracion_minutos"]) for row in selected),
        "rows": selected,
    }


def write_json(payload: dict[str, object], out: Path | None) -> None:
    encoded = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if out is None:
        sys.stdout.write(encoded)
        return
    try:
        out.write_text(encoded, encoding="utf-8")
    except OSError as exc:
        raise InputError("unwritable_output", "no se pudo escribir la salida", path=str(out)) from exc


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--registro", required=True, type=Path)
    result.add_argument("--sistema", required=True)
    result.add_argument("--desde", required=True)
    result.add_argument("--hasta", required=True)
    result.add_argument("--severidad", required=True, help="Lista separada por comas")
    result.add_argument("--max-filas", required=True, type=int)
    result.add_argument("--out", type=Path)
    return result


def fail(error: InputError, out: Path | None) -> NoReturn:
    payload: dict[str, object] = {
        "status": "error",
        "error": {"code": error.code, "message": error.message, **error.details},
    }
    try:
        write_json(payload, out)
    except InputError:
        sys.stderr.write(json.dumps(payload, ensure_ascii=False) + "\n")
    raise SystemExit(2)


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        payload = build_table(
            registro=args.registro,
            sistema=args.sistema.strip(),
            desde=parse_date(args.desde, "--desde"),
            hasta=parse_date(args.hasta, "--hasta"),
            severidades={value.strip() for value in args.severidad.split(",") if value.strip()},
            max_filas=args.max_filas,
        )
        write_json(payload, args.out)
    except InputError as error:
        fail(error, args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

