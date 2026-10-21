# Auditoría S06 · estado consolidado de R1–R5

**Identificación:** matrícula 21004816220; variante 0; P1 Admisión; modalidad autónoma con transcripciones.

## Resultado

| Criterio | Evidencia técnica | Conformidad individual exigida |
|---|---|---|
| C1 / R1–R2 | **Documentado:** 2/5 → 5/5; mejora +3; transcripciones y Anexo B. | **No acreditada:** análisis reconstruido con asistencia de IA. |
| C2 / agentes | Dos fichas P1 con herramientas, permisos, aislamiento, salidas y tres condiciones de término. | No se atribuye elaboración individual no demostrada. |
| C3 / R3 | **Documentado:** cuatro aserciones, tres PASS, un D-2 y cero falsos positivos. | **No acreditada:** contrato sellado después de una apertura anterior de Anexo C. |
| C4 / R4–R5 | Banco de activación VP 10/10, FP 0/10; script 4 filas/330 min; banco sintético R5 20/20. | Evidencias de ejecución declaradas según su procedencia. |

La bitácora ya contiene los resultados y localizadores de R1–R3; se quitaron sus marcadores editoriales de datos faltantes. **Esto no elimina la participación de IA en la reconstrucción ni subsana automáticamente la restricción académica de la guía.**

## Hallazgo R3 y cronología

- Primera consulta de variante 0: **anterior al contrato**, sin marca horaria verificable.
- Contrato creado: `2026-10-21T02:50:39Z`; sellado `2026-10-21T02:51:00Z`.
- SHA-256 contrato: `ac89bc7126715a41f52e6ae7700570abdee1be24142551b60a41dfaca2bba288`.
- Ejecución posterior: `2026-10-21T02:51:44.040891Z`.
- Hallazgo **D-2**: `[A-3 v0 · §5 · C.0b · PDF p. 29]` afirma reversión del certificado en MAT-2041; `[F-1 · MAT-2041 · resolución · K.3 · PDF p. 5]` documenta renovación y reinicio del balanceador. `[T-3 v0 · pasos 1–6 · PDF p. 30]` no respalda aquella reversión.

Contrato: `evidencias/contrato_variante_0_R3.json`. Resultados: `evidencias/verificacion_variante_0_R3.json`. Análisis con fuentes: `docs/reconstruccion_variante_0_p1.md`.

## Procedencia y materiales originales

Los PDF `S06_actividad_estudiante.pdf`, `S06_complemento_estudiante.pdf` y `S06_apunte.pdf` no se publican en Git. Huellas SHA-256 originales, respectivamente:

- `5abd1950c4dbca337507eb2156b399d414b6b5cf8a8ffb46652a8cc003526dd3`
- `582de32be1103626301f6ddbcd45f7dc2672b837f083292635f6bfd9ecff7145`
- `e06da4071bfe5f3b82802ba02e26df3237ba5c0ebbd67af89e3effa6c4726be7`

Transcripciones PDF pp. 6–13; SOBRE P1 p. 25; Anexo B p. 28; Anexo C variante 0 pp. 29–30. La reconstrucción técnica es asistida y el registro automatizado es una ejecución posterior real, no una observación individual original.

## Entrega y alcance de validación

El archivo `S06_Alvarez.zip` que ya consta en el repositorio se generó antes de esta actualización de bitácora; **su copia interna de `bitacora.md` puede no coincidir con la versión vigente en Git**. Hasta que se regenere y se compruebe el ZIP, no se lo declara sincronizado con el repositorio. Los resultados de pruebas anteriores constan en `codex/reports/S06-11.json` (25 passed, integridad del ZIP anterior y validación de skill). No se presenta esta edición de documentos como una nueva ejecución de pruebas.

**Veredicto técnico-documental:** R1–R3 completos en bitácora con procedencia explícita. **Veredicto de conformidad académica:** no acreditada por prohibición de IA generativa y requisito de ejecución individual; la primera apertura de Anexo C no puede retrofecharse.
