# Auditoría S06 — NO_APTO_ENTREGA

Fecha de auditoría: 2026-10-20 (America/Santiago).

Resultado final: **BLOQUEADO / NO_APTO_ENTREGA**.

No se creó `S06_Alvarez.zip`. Las fuentes privadas y las validaciones técnicas
están disponibles, pero no sustituyen las evidencias individuales restringidas.
C3 insuficiente sigue siendo una compuerta bloqueante; además, el banco del
selector ya fue ejecutado y aprobó su umbral, pero no levanta los pendientes
académicos de R1–R3.

## Matriz C1–C4

| Criterio | Estado | Evidencia concreta | Pendiente o fallo |
|---|---|---|---|
| C1 · R1/R2 | PENDING | `bitacora.md` contiene Tabla 6.A con dos filas y `docs/instrucciones_R1_R2.md` documenta el orden. Se localizaron secciones 3.2–3.6 y Anexo B en el complemento privado. | Faltan las observaciones propias, dos cifras n/5 y la comparación personal. No se reconstruyen con IA. |
| C2 · fichas y términos | PENDING | Los dos YAML parsean; el verificador es distinto, adversarial y aislado; ambos contienen semantic, budget y no_progress. Se verificaron complemento §4.3 y el ejemplo del apunte. | Las fichas siguen rotuladas como plantillas, con campos `PENDIENTE` y umbrales nulos. El validador las rechaza como fichas completas. |
| C3 · contrato previo y defecto | FAIL · BLOQUEANTE | La plantilla exige aserción sobre traza, localizadores y tres términos. La variante 2 de Anexo C y F-1 son legibles en la fuente privada. | No existe contrato personal cerrado antes de abrir Anexo C, dos horas auténticas, ejecución de aserciones ni hallazgo personal reproducible. No se retrofechó evidencia. |
| C4 · skill, banco y descarte | PASS | Skill v1.1.0 válida; 6 pruebas específicas y CLI real con 4 filas/330 minutos. Banco 10+10 ejecutado mediante `gpt-5.6-luna`, razonamiento `none`, en 20 sesiones únicas: VP 10/10 y FP 0/10. La corrida fallida v1.0.0 (VP 10/10, FP 4/10) permanece preservada. `descartes.md` contiene umbral >2/20 con método. | Sin pendiente técnico en C4. El umbral de descarte sigue correctamente rotulado como propuesta, no como medición. |

## Fuentes privadas

`.local_sources/` está ignorada por Git y `git ls-files .local_sources/` no
devuelve archivos. Se verificó legibilidad visual y textual de F-1, Anexo B,
Anexo C variante 2 y K.11.

| Archivo | SHA-256 |
|---|---|
| `S06_actividad_estudiante.pdf` | `5abd1950c4dbca337507eb2156b399d414b6b5cf8a8ffb46652a8cc003526dd3` |
| `S06_complemento_estudiante.pdf` | `582de32be1103626301f6ddbcd45f7dc2672b837f083292635f6bfd9ecff7145` |
| `S06_apunte.pdf` | `e06da4071bfe5f3b82802ba02e26df3237ba5c0ebbd67af89e3effa6c4726be7` |

## Autoría y modalidad

- R1–R3 permanecen como andamiaje asistido y no se aprueban académicamente.
- R4–R5 registran asistencia de Codex en `bitacora.md`.
- La matrícula completa permanece pendiente; no se inventó.
- El fixture reproduce F-1 para pruebas, pero no sustituye guía, transcripciones
  ni anexos.

## Validaciones ejecutadas

```text
python -m pytest -q
................ [100%]
16 passed in 0.43s
```

Los 15 tests previamente aprobados se conservaron; se añadió una validación de
K.11 y del estado de evidencia del selector.

```text
python -c "... yaml.safe_load ..."
2 YAML válidos
```

```text
python -c "... json.loads por JSONL ..."
{'evals/activacion.jsonl': 20, 'evals/resultados_activacion.jsonl': 20}
```

```text
python -m compileall -q .
# salida vacía; código 0
```

```text
python skills/cuadrar-tiempos-de-incidente/scripts/tabla_incidentes.py \
  --registro fixtures/registro_F1.csv --sistema 'Matrícula en línea' \
  --desde 2026-03-09 --hasta 2026-03-13 --severidad 'Alta,Crítica' \
  --max-filas 5 --out /tmp/tabla_s06_auditoria_actual.json
# código 0; status=ok, row_count=4, total_minutos=330
```

```text
python /home/chop/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  skills/cuadrar-tiempos-de-incidente
Skill is valid!
```

## Requisitos para levantar el bloqueo

1. Completar personalmente R1 y R2 con observaciones hechas en el orden de la
   actividad, dos mediciones n/5 y comparación.
2. Completar personalmente las dos fichas R3, incluidas razones, contratos y
   umbrales numéricos, y volver a ejecutar su validador.
3. Aportar un contrato R3 auténticamente anterior a la apertura de Anexo C, dos
   marcas horarias reales, aserción sobre traza, resultados y hallazgo con dos
   localizadores. La evidencia no puede retrofecharse.
4. Repetir la auditoría tras completar las evidencias individuales; crear el ZIP
   solo si todas las compuertas pasan.
