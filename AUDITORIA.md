# Auditoría S06 — CIERRE TÉCNICO / NO APTO PARA ENTREGA

Fecha de auditoría: 2026-10-20 (America/Santiago).

Resultado técnico: **COMPLETO CON EVIDENCIA ASISTIDA**.

Resultado académico: **BLOQUEADO / NO APTO PARA ENTREGA**.

El análisis técnico C1-C3 fue completado y probado, pero R1-R3 prohíben IA
generativa. Las demostraciones nuevas se identifican como asistidas y no
sustituyen las observaciones, fichas ni el contrato/hallazgo personales. Por
ello no se creó `S06_Alvarez.zip`. El único paquete generado es
`S06_Alvarez_REVISION_TECNICA_NO_APTA.zip`, con advertencia explícita y sin los
PDF privados.

## Matriz C1-C4

| Criterio | Conformidad técnica | Admisibilidad académica | Evidencia y pendiente |
|---|---|---|---|
| C1 · R1/R2 | **PASS asistido**: Anexo B aplicado requisito por requisito; R1 = 2/5, R2 = 5/5, mejora +3. | **PENDING individual** | `docs/analisis_asistido_R1_R3.md` y `evidencias/resultados_tecnicos_R1_R3.json`. Falta que el/la estudiante produzca sus observaciones y comparación sin IA. |
| C2 · dos fichas y tres términos | **PASS asistido**: dos YAML completos, razones admitidas, 3/4 herramientas, permisos mínimos, errores, métricas y exactamente tres condiciones con umbrales. | **PENDING individual** | `agents/generador.yaml` y `agents/verificador.yaml` están rotulados como propuestas asistidas no evaluables. Deben rehacerse personalmente para R3. |
| C3 · contrato y defecto | **PASS técnico asistido**: contrato sellado antes de la lectura automatizada actual; 4 aserciones, traza disponible, D-1 confirmado, 0 falsos positivos. | **FAIL · BLOQUEANTE** | El sello solo acredita la ejecución actual, no un contrato personal previo. Falta la secuencia personal sin IA. La extracción textual inicial abarcó el PDF completo, aunque el análisis se limitó a variante 2; no se afirma apertura exclusiva. |
| C4 · skill, banco y descarte | **PASS preservado** | **PASS según registro existente** | Sin nuevas llamadas a modelo. Se conservaron 20 sesiones, VP 10/10 y FP 0/10. El umbral de descarte sigue rotulado como propuesta. |

## Hallazgo técnico C3

`[A-3 v2 · §6 · tabla C.2b · PDF p. 33]` afirma que MAT-2061 se
originó en una falla de red del nodo 2. `[F-1 · MAT-2061 · causa y resolución
· tabla K.3 · PDF p. 5]` registra causa **Sin causa determinada** y menciona
reiniciar el nodo 2 solo como resolución. Clasificación: **D-1 · afirmación sin
respaldo**.

La traza T-3 sí existe: el paso 2 filtra severidad y el paso 3 excluye
MAT-2048 por estado Duplicado. Métricas: 4 aserciones ejecutadas, 3 PASS, 1
defecto confirmado, 1 alerta, 0 falsos positivos, tasa FP 0/1 = 0.0; parada
semántica con 4 de 12 operaciones presupuestadas.

## Contrato automatizado actual

- Archivo: `evidencias/contrato_automatizado_R3.json`.
- Cierre declarado: `2026-10-20T22:51:10-03:00`.
- Sello: `2026-10-20T22:51:26-03:00`.
- SHA-256: `5969c541fc1107562543ef88cdc55577806546833ba83c8a4d9b97f346539948`.
- Ejecución registrada: `2026-10-20T22:52:52-03:00`.

La precedencia anterior es real para esta automatización y no se retrofecha ni
se atribuye al/la estudiante.

## Fuentes privadas

Los tres PDF estuvieron accesibles y fueron revisados textual y visualmente.
`.local_sources/` sigue ignorada y `git ls-files .local_sources/` no devuelve
archivos.

| Archivo | SHA-256 |
|---|---|
| `S06_actividad_estudiante.pdf` | `5abd1950c4dbca337507eb2156b399d414b6b5cf8a8ffb46652a8cc003526dd3` |
| `S06_complemento_estudiante.pdf` | `582de32be1103626301f6ddbcd45f7dc2672b837f083292635f6bfd9ecff7145` |
| `S06_apunte.pdf` | `e06da4071bfe5f3b82802ba02e26df3237ba5c0ebbd67af89e3effa6c4726be7` |

El CSV de `fixtures/` se usó para recálculo determinista, no como sustituto de
la guía, transcripciones, Anexo B o Anexo C.

## Preservación de R4

No se volvió a ejecutar el banco ni se realizaron llamadas de modelo. Los
hashes se mantuvieron:

| Artefacto | SHA-256 |
|---|---|
| `skills/cuadrar-tiempos-de-incidente/SKILL.md` | `b77ff89aa9356d8533c568a7abd162bc8447af0422d2132fa1980264ac35b443` |
| `evals/activacion.jsonl` | `bd22ed4cd1325f19be83669f7672c40355dd8caa31fe208dc017e029388b60db` |
| `evals/resultados_activacion.jsonl` | `0d7cf73a77d3c9948ace90cbc9a82fd50d01a655e68c10ffc91ad46d38505270` |
| `evals/reporte_activacion.json` | `fc29a8bf26b6959b80adf4af8fa4a3091b3b8c220608859cd00f6a7b9977476a` |

## Validaciones ejecutadas

```text
python -m pytest -q
................... [100%]
19 passed in 0.43s
```

```text
python -c "... yaml.safe_load ..."
2 YAML válidos
```

```text
sha256sum -c evidencias/contrato_automatizado_R3.sha256
evidencias/contrato_automatizado_R3.json: OK
```

```text
python -m compileall -q .
# salida vacía; código 0
```

```text
python skills/cuadrar-tiempos-de-incidente/scripts/tabla_incidentes.py ...
# código 0; status=ok, row_count=4, total_minutos=330
```

```text
python /home/chop/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  skills/cuadrar-tiempos-de-incidente
Skill is valid!
```

## Requisitos pendientes

1. Completar personalmente R1 y R2 con observaciones propias, dos mediciones
   n/5 y comparación, sin copiar el análisis asistido.
2. Producir personalmente las dos fichas R3 bajo la política de la actividad.
3. Aportar un contrato R3 personal auténticamente anterior a abrir Anexo C y
   ejecutar el hallazgo sin IA generativa. El sello automatizado no satisface
   esta condición.
4. Completar la matrícula; no se inventó.
5. Repetir la auditoría académica. Solo si todas las compuertas pasan se puede
   crear `S06_Alvarez.zip`.
