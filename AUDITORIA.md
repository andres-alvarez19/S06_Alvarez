# Auditoría S06 · estado consolidado de R1–R5

**Identificación:** matrícula 21004816220; variante 0; P1 Admisión; modalidad autónoma con transcripciones.

## Resultado

| Criterio | Evidencia técnica | Conformidad individual exigida |
|---|---|---|
| C1 / R1–R2 | **Documentado:** 2/5 → 5/5; mejora +3; transcripciones y Anexo B. | El estudiante declara ejecución original sin IA; la reconstrucción técnica posterior sí usó IA. La autoría original no está verificada independientemente por esta auditoría. |
| C2 / agentes | Dos fichas P1 con herramientas, permisos, aislamiento, salidas y tres condiciones de término. | No se atribuye elaboración individual no demostrada. |
| C3 / R3 | **Documentado:** cuatro aserciones, tres PASS, un D-2 y cero falsos positivos. | El estudiante declara ejecución original sin IA. La secuencia de la **verificación posterior** no acredita contrato previo a la primera lectura de Anexo C. |
| C4 / R4–R5 | Banco de activación VP 10/10, FP 0/10; script 4 filas/330 min; banco sintético R5 20/20. | Evidencias de ejecución declaradas según su procedencia. |

La bitácora contiene los resultados y localizadores de R1–R3. **Rectificación:** no existe fundamento en la asistencia documental posterior para afirmar que las rondas originales incumplieron la prohibición de IA. El estudiante declara que las ejecutó sin IA. Se conserva la declaración de asistencia posterior para no confundir períodos ni procedencias. La evidencia disponible tampoco demuestra por sí sola la secuencia experimental original de R3.

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

**Veredicto técnico-documental:** R1–R3 completos en bitácora con procedencia diferenciada. **Restricción de IA:** no se establece incumplimiento de las rondas originales; existe declaración explícita del estudiante de que no usó IA en ellas. **Secuencia R3:** sigue sin demostrarse que el contrato original precediera al primer acceso al Anexo C. Para resolverlo, localizar un contrato original fechado y verificable; en su defecto, solicitar al docente una nueva variante o artefacto no visto, sellar el contrato antes del acceso y ejecutar la verificación prospectiva. Una nueva prueba no puede retrovalidar la secuencia antigua.
