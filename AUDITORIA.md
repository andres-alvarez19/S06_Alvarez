# Auditoría S06-11 · variante 0 / P1 Admisión

Fecha: 2026-10-20 (America/Santiago; ejecución UTC 2026-10-21).

- Matrícula: **21004816220**.
- Estado técnico: **PASS ASISTIDO C1-C4**.
- Conformidad académica: **PENDIENTE R1-R3**.
- Elegibilidad del ZIP: **SÍ para entrega técnica transparente**, porque contiene
  únicamente la estructura exigida y evidencia real del banco; **NO equivale a
  aprobación académica** ni sustituye las casillas individuales pendientes.

## Fuentes originales

| Archivo privado | SHA-256 |
|---|---|
| `S06_actividad_estudiante.pdf` | `5abd1950c4dbca337507eb2156b399d414b6b5cf8a8ffb46652a8cc003526dd3` |
| `S06_complemento_estudiante.pdf` | `582de32be1103626301f6ddbcd45f7dc2672b837f083292635f6bfd9ecff7145` |
| `S06_apunte.pdf` | `e06da4071bfe5f3b82802ba02e26df3237ba5c0ebbd67af89e3effa6c4726be7` |

La revisión textual y visual cubrió asignación (complemento PDF pp. 2-3),
transcripciones P1 (pp. 6 y 10, con cadena completa pp. 6-13), SOBRE P1
(p. 25), Anexo B (p. 28) y Anexo C variante 0 (pp. 29-30). Los PDF no están
versionados ni empaquetados.

## Matriz C1-C4

| Criterio | Estado técnico | Estado académico | Evidencia |
|---|---|---|---|
| C1 | **PASS asistido**: R1 2/5; R2 5/5; +3. | Pendiente individual. | `docs/reconstruccion_variante_0_p1.md`; complemento pp. 6-13 y 28. |
| C2 | **PASS asistido**: dos fichas P1 completas y tres términos en cada una. | Pendiente individual. | `agents/*.yaml`, schemas/casos y pruebas. |
| C3 | **PASS asistido**: 4 aserciones; 3 PASS; 1 D-2; 0 FP. | Pendiente individual; hubo prelectura declarada. | Contrato, sello y verificación `variante_0_R3`. |
| C4 | **PASS registrado**: VP 10/10, FP 0/10, script determinista y descarte cuantificado. | PASS según registros existentes. | Skill/script, banco y resultados preservados. |

## C3 · cronología y hallazgo

1. Primera apertura de variante 0 para corregir S06-11: anterior al contrato;
   se declara expresamente y no se le asigna una hora inventada.
2. Contrato creado: `2026-10-21T02:50:39Z`.
3. Contrato sellado: `2026-10-21T02:51:00Z`.
4. Nueva ejecución automatizada: `2026-10-21T02:51:44.040891Z`.

SHA-256 del contrato:
`ac89bc7126715a41f52e6ae7700570abdee1be24142551b60a41dfaca2bba288`.

Hallazgo: `[A-3 v0 · §5 · C.0b · PDF p. 29 (impresa 28)]` afirma que
MAT-2041 se resolvió revirtiendo el certificado. `[F-1 · MAT-2041 · resolución
· K.3 · PDF p. 5]` registra renovación del certificado y reinicio del
balanceador. Clasificación: **D-2 · cita que no respalda esa afirmación**.
`[T-3 v0 · pasos 1-6 · C.0c · PDF p. 30 (impresa 29)]` no contiene una acción
que produzca la resolución falsa.

## Preservación R4

No se reevaluó el banco porque la descripción de la skill no cambió y es
independiente del puesto/variante. Se conservaron los hashes de S06-10:

| Artefacto | SHA-256 |
|---|---|
| `skills/cuadrar-tiempos-de-incidente/SKILL.md` | `b77ff89aa9356d8533c568a7abd162bc8447af0422d2132fa1980264ac35b443` |
| `evals/activacion.jsonl` | `bd22ed4cd1325f19be83669f7672c40355dd8caa31fe208dc017e029388b60db` |
| `evals/resultados_activacion.jsonl` | `0d7cf73a77d3c9948ace90cbc9a82fd50d01a655e68c10ffc91ad46d38505270` |
| `evals/reporte_activacion.json` | `fc29a8bf26b6959b80adf4af8fa4a3091b3b8c220608859cd00f6a7b9977476a` |

## Paquete mínimo

El ZIP se construye con `bitacora.md`, las dos fichas, `SKILL.md`, su script,
el banco de activación, resultados/reporte necesarios para respaldar las
métricas y `descartes.md`, más `MANIFEST_SHA256.txt`. Se excluyen `codex/`,
`tests/`, schemas, fuentes privadas, caches, logs y ZIP anteriores.

Las salidas exactas de pruebas, miembros y hash final quedan registradas en
`codex/reports/S06-11.json` después de la ejecución final.
