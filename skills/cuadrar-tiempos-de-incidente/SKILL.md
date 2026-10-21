---
name: cuadrar-tiempos-de-incidente
description: "Úsala exclusivamente para filtrar un CSV de incidentes ya suministrado por sistema, rango de fechas y severidad, excluir filas marcadas explícitamente como duplicadas, convertir h:mm y totalizar minutos con evidencia literal. No la uses para investigar causas raíz, inferir duplicados por similitud, consultar monitoreo vivo ni procesar planillas ajenas a incidentes; si la petición no solicita ese filtrado y totalización exactos, esta skill no aplica."
metadata:
  version: 1.1.0
  provenance:
    source: fixtures/registro_F1.csv
    source_note: F-1 contrastado con S06_complemento_estudiante.pdf tabla K.3 y Anexo A, disponible solo en .local_sources/; el fixture no sustituye la guía ni otros anexos.
    ai_assistance: Borrador y script preparados por Codex durante S06-04.
  evaluation:
    status: passed
    evidence: La validación local y 6 pruebas funcionales pasaron; el CLI produjo 4 filas y 330 minutos. La versión 1.0.0 obtuvo VP 10/10 y FP 4/10; la versión 1.1.0 obtuvo VP 10/10 y FP 0/10 en 20 sesiones independientes con gpt-5.6-luna/none el 2026-10-20. Esto no equivale a aprobación docente.
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

