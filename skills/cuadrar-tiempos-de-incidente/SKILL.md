---
name: cuadrar-tiempos-de-incidente
description: "Filtra un registro CSV F-1 de incidentes por sistema, fechas y severidad, excluye duplicados y cuadra duraciones h:mm en minutos; úsala cuando pidan ‘cuánto tiempo se cayó’ o una tabla auditable de incidentes. No la uses para investigar causas, deduplicar por similitud ni consultar sistemas vivos: deriva esos casos a investigación operativa con sus fuentes autorizadas."
metadata:
  version: 1.0.0
  provenance:
    source: fixtures/registro_F1.csv
    source_note: Transcripción de prueba declarada por fixtures/README.md; no sustituye el complemento S06.
    ai_assistance: Borrador y script preparados por Codex durante S06-04.
  evaluation:
    status: approved
    evidence: Validador oficial aprobado; 6 pruebas pasaron y el CLI produjo 4 filas y 330 minutos el 2026-10-20.
---

# Cuadrar tiempos de incidente

## Cuándo aplica

Usa esta skill para producir una tabla reproducible desde un CSV compatible con
F-1 cuando la petición identifica filtros de sistema, rango inclusivo de fechas
y severidades. También aplica a preguntas coloquiales como “cuádreme las caídas
de matrícula de esta semana” si esos filtros pueden expresarse sin inferencias.

No aplica a análisis causal, diagnóstico, búsqueda en servicios externos,
reconstrucción de campos ausentes ni agrupación probabilística de incidentes.
Para esos casos, entrega el registro a un flujo de investigación operativa que
tenga las fuentes y permisos correspondientes.

## Procedimiento

1. Confirma que el archivo tenga las columnas exigidas por el script.
2. Ejecuta `scripts/tabla_incidentes.py` con `--registro`, `--sistema`, `--desde`,
   `--hasta`, `--severidad`, `--max-filas` y `--out`.
3. Conserva tickets y causas literalmente. No completes causas desconocidas.
4. Excluye registros cuyo estado sea `Duplicado de ...`.
5. Interpreta `h:mm` como horas y minutos, nunca como número decimal.
6. Si no hay coincidencias, conserva `not_answerable`; si se supera el límite o
   el CSV es inválido, conserva el error estructurado sin truncar datos.

## Verificaciones

- Comprueba `row_count` contra la longitud de `rows`.
- Recalcula `total_minutos` como suma de `duracion_minutos`.
- Confirma que fechas límite sean inclusivas y que sistema/severidad coincidan
  exactamente tras eliminar espacios exteriores.
- Conserva el archivo fuente sin modificaciones.

## Prohibido

- Ampliar la allowlist, permisos o fuentes disponibles.
- Escribir fuera del sandbox autorizado.
- Truncar silenciosamente al alcanzar `--max-filas`.
- Inferir causas, estados, tickets, fechas o duraciones desconocidas.
- Presentar el fixture como evidencia de una ejecución operativa real.

