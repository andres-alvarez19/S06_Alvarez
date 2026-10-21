# Auditoría S06-10 · cierre integral

Fecha de auditoría: 2026-10-20 (America/Santiago; ejecución UTC 2026-10-21).

- Estado técnico: **COMPLETO_TECNICO**.
- Conformidad académica: **PENDIENTE R1-R3**.
- Paquete: `S06_Alvarez.zip` es un paquete técnico auditable, **no** una
  declaración de aprobación académica.

La separación anterior es deliberada. R1-R3 prohíben IA generativa y siguen
requiriendo producción personal; S06-10 autoriza crear el ZIP técnico siempre
que la reconstrucción asistida y las restricciones de autoría sean visibles.
La matrícula no fue inventada y permanece pendiente.

## Matriz C1-C4

| Criterio | COMPLETO_TECNICO | CONFORMIDAD_ACADEMICA | Evidencia |
|---|---|---|---|
| C1 · R1/R2 | **PASS asistido**: R1 2/5, R2 5/5, mejora +3, con primera pérdida y referencias a Anexo B. | **PENDIENTE individual** | `docs/reconstruccion_tecnica.md`; complemento PDF pp. 6-13 y 28. |
| C2 · fichas | **PASS asistido**: dos YAML sin PENDIENTE, contratos, herramientas enumeradas, permisos, aislamiento, errores, métricas y tres términos numéricos. | **PENDIENTE individual** | `agents/generador.yaml`, `agents/verificador.yaml`, `tests/test_agents.py`. |
| C3 · contrato/hallazgo | **PASS asistido**: contrato S06-10 sellado antes de la verificación actual; 4 aserciones, T-3, defecto D-1, 0 FP y dos localizadores por resultado. | **FAIL/PENDIENTE bloqueante para aprobación** | `evidencias/contrato_cierre_integral_R3.*`, `evidencias/verificacion_cierre_integral_R3.json`. No se afirma precedencia histórica: Anexo C ya había sido leído en S06-09. |
| C4 · skill/banco/descarte | **PASS**: CLI 4 filas/330 min; R4 preservado VP 10/10 y FP 0/10; R5 ejecutado en banco sintético declarado, 20/20 pass y 0 fallos. | **PASS según registros existentes** | Skill/script, evidencia R4 cruda y `evals/reporte_formato_tablas.json`. |

## Procedencia de datos

| Clase | Artefactos | Declaración |
|---|---|---|
| Fuente original observada | Tres PDF en `.local_sources/` | Privados, legibles, revisados textual y visualmente; fuera de Git y del ZIP. |
| Reconstrucción asistida | `docs/reconstruccion_tecnica.md`, YAML y contratos R3 | No es observación presencial ni autoría individual. |
| Reproducción | `fixtures/registro_F1.csv` | Reproduce F-1 para recálculo; no sustituye guía, transcripciones ni anexos. |
| Sintético | `fixtures/sinteticos/formato_tablas.json` | `generated=true`, `synthetic=true`, motivo, generador, timestamp y alcance explícitos. |
| Ejecución real | Salidas R4, R5, CLI, pytest, hashes y ZIP | Corresponde a comandos efectivamente ejecutados; no se extrapola a producción. |

## Fuentes privadas

| Archivo | SHA-256 |
|---|---|
| `S06_actividad_estudiante.pdf` | `5abd1950c4dbca337507eb2156b399d414b6b5cf8a8ffb46652a8cc003526dd3` |
| `S06_complemento_estudiante.pdf` | `582de32be1103626301f6ddbcd45f7dc2672b837f083292635f6bfd9ecff7145` |
| `S06_apunte.pdf` | `e06da4071bfe5f3b82802ba02e26df3237ba5c0ebbd67af89e3effa6c4726be7` |

`git ls-files .local_sources/` no devuelve archivos. La revisión visual cubrió
Anexo B (PDF p. 28) y Anexo C variante 2 (PDF pp. 32-34).

## Cronología verificable C3 actual

1. Contrato creado: `2026-10-21T01:59:03Z`.
2. Contrato sellado: `2026-10-21T01:59:21Z`.
3. Acceso actual a fuente: `2026-10-21T01:59:31Z`.
4. Recálculo capturado: `2026-10-21T01:59:42Z`.

SHA-256 del contrato:
`aeed90e62939b8217498cc53c94b515a65fd2dd0ef1decab98c6721e6d319e5c`.
Esta cronología solo acredita S06-10; no se retrofecha ni se atribuye al/la
estudiante.

Hallazgo H-1: `[A-3 v2 · §6 · C.2b · PDF p. 33]` atribuye a MAT-2061
una falla de red del nodo 2. `[F-1 · MAT-2061 · causa/resolución · K.3 · PDF
p. 5]` registra `Sin causa determinada` y el reinicio solo como resolución.
Clasificación: **D-1 · afirmación sin respaldo**. La traza se localiza en
`[T-3 v2 · paso 2 · C.2c · PDF p. 34]` y `[T-3 v2 · paso 3 · C.2c · PDF
p. 34]`.

## Preservación R4

No hubo nuevas llamadas de modelo. Los hashes antes y después coinciden:

| Artefacto | SHA-256 |
|---|---|
| `skills/cuadrar-tiempos-de-incidente/SKILL.md` | `b77ff89aa9356d8533c568a7abd162bc8447af0422d2132fa1980264ac35b443` |
| `evals/activacion.jsonl` | `bd22ed4cd1325f19be83669f7672c40355dd8caa31fe208dc017e029388b60db` |
| `evals/resultados_activacion.jsonl` | `0d7cf73a77d3c9948ace90cbc9a82fd50d01a655e68c10ffc91ad46d38505270` |
| `evals/reporte_activacion.json` | `fc29a8bf26b6959b80adf4af8fa4a3091b3b8c220608859cd00f6a7b9977476a` |

## Validaciones ejecutadas

```text
python -m pytest -q -k 'not paquete_zip'
24 passed, 1 deselected in 0.46s
```

```text
python -m pytest -q
25 passed in 0.45s
```

```text
python -m compileall -q .
# código 0; sin salida de error
```

```text
sha256sum -c evidencias/contrato_automatizado_R3.sha256 \
  evidencias/contrato_cierre_integral_R3.sha256
# ambos: OK
```

```text
python /home/chop/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  skills/cuadrar-tiempos-de-incidente
# Skill is valid!
```

```text
python codex/tools/evaluar_formato_tablas.py ...
# 20 casos, 20 pass, 0 fallos, reopen_triggered=false
```

```text
python codex/tools/crear_paquete.py
# 83 miembros; SHA-256 del ZIP se registra en codex/reports/S06-10.json

unzip -t S06_Alvarez.zip
# No errors detected in compressed data
```

El test del paquete abre el ZIP, comprueba cada entrada contra
`MANIFEST_SHA256.txt`, exige README/auditoría y rechaza PDFs o rutas
`.local_sources/`.

## Contenido y condición final

El ZIP incluye bitácora, fichas, schemas, skill/script, bancos y evidencia
cruda R4 final, banco/resultados sintéticos R5, contratos/resultados R3,
documentación, pruebas, contratos Codex, informes S06-00…09, README de
procedencia y manifiesto SHA-256. No incluye PDFs privados.

Resultado final: **COMPLETO_TECNICO**. Para convertirlo en entrega académica
aprobable siguen faltando las observaciones personales R1/R2, las fichas y la
secuencia personal R3 sin IA generativa, además de la matrícula.
