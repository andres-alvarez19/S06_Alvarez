# Bitácora S06 · consolidación documental de R1–R5

- Variante: **0**
- Puesto: **P1 · Admisión**
- Modalidad: **autónoma con transcripciones**
- Matrícula: **21004816220**
- Alcance del registro: **análisis documental y verificaciones técnicas posteriores**.

**Procedencia y límite de autoría:** las observaciones de R1–R3 se obtuvieron analizando transcripciones y evidencias conservadas, con asistencia de IA. No se presentan como observaciones personales realizadas durante la dinámica ni como rondas nuevas sin IA. Esta bitácora no modifica las transcripciones históricas. La guía de actividad exige producción individual sin IA generativa para dichas rondas; por tanto, su acreditación académica sigue sin demostrarse.

## Tabla 6.A · R1 y R2

| Ronda | Puesto | Qué recibió según transcripción | Qué se infiere de la evidencia (campo perdido o corregido) | Qué se descartó / omitió | Supervivencia n/5 |
|---|---|---|---|---|---|
| R1 | P1 · Admisión | Encargo literal: Matrícula en línea, 9–13 de marzo de 2026, severidades Alta/Crítica, columnas Ticket/Fecha/Causa/Minutos sin servicio, excluir duplicados, tickets exactos, hasta cinco filas y total en minutos. | P1 transmitió a P2 una instrucción libre sobre «incidentes graves», «semana del 9» y «tabla corta». En la frontera P1→P2 se perdieron el formato y unidad exactos, exclusión explícita y la regla de total/presupuesto. | No se transmitieron explícitamente esas restricciones; el resultado R1 incluyó el duplicado MAT-2048 y no conservó la línea de total en minutos. | **2/5** |
| R2 | P1 · Admisión | El mismo encargo literal y esquema E1. | P1 emitió una orden tipada que preservó objetivo, consumidor, alcance, exclusiones, evidencia, presupuesto y formato. En la cadena posterior se rechazó una duración en h:mm y se corrigió a minutos enteros. | MAT-2048 se excluyó como duplicado; se filtraron fechas y severidades fuera de alcance. | **5/5** |

**Comparación comprobable:** R1 **2/5**, R2 **5/5**, diferencia **+3**. La inferencia proviene de las transcripciones P1 y de la tabla B.1 del Anexo B, no de una observación presencial del estudiante.

| Requisito B.1 | R1 | R2 | Comprobación |
|---|---:|---:|---|
| Formato: cuatro columnas y minutos | 0 | 1 | R1 cambia columnas y expresa duraciones en horas; R2 usa estructura y unidad exigidas. |
| Alcance: sistema, fecha y severidad | 1 | 1 | Se mantiene Matrícula en línea, 9–13 de marzo y Alta/Crítica. |
| Exclusión de duplicados | 0 | 1 | R1 incluye MAT-2048; R2 lo excluye. |
| Ticket literal como evidencia | 1 | 1 | Ambas rondas conservan identificadores comprobables. |
| Máximo cinco filas y línea total en minutos | 0 | 1 | R1 carece de total final en minutos; R2 reporta 4 filas y 330 minutos. |

**Localizadores:** `S06_complemento_estudiante.pdf`, transcripciones PDF pp. 6–13, SOBRE P1 p. 25, Anexo B tabla B.1 p. 28; soporte técnico `docs/reconstruccion_variante_0_p1.md`.

## Tabla 6.B · R3 · verificación documentada

### Contrato existente y secuencia verificable

- **Creación del contrato técnico:** `2026-10-21T02:50:39Z`.
- **Sellado del contrato:** `2026-10-21T02:51:00Z`.
- **SHA-256 del contrato:** `ac89bc7126715a41f52e6ae7700570abdee1be24142551b60a41dfaca2bba288`.
- **Primera apertura histórica de Anexo C:** ocurrió antes de crear este contrato; **hora exacta no acreditada**. No se inventa ni se afirma revisión a ciegas.
- **Ejecución automatizada posterior al sello:** `2026-10-21T02:51:44.040891Z`.
- **Artefactos:** `evidencias/contrato_variante_0_R3.json` y `evidencias/verificacion_variante_0_R3.json`.
- **Criterio de término declarado:** cuatro aserciones con veredicto y dos localizadores; máximo doce operaciones; detener tras dos operaciones sin avance. La ejecución cerró por término semántico, con cuatro operaciones contabilizadas.

| Aserción | Artefacto/traza | Operación ejecutada | Resultado | Localizadores |
|---|---|---|---|---|
| S11-F1-01: selección y duración válidas | F-1 | Filtrar sistema, fechas, severidades, estado; convertir duraciones y sumar | **PASS**: MAT-2041, MAT-2047, MAT-2055, MAT-2061; 4 filas, 330 min; MAT-2048 descartado | F-1 · tabla K.3 · PDF p. 5 |
| S11-ART-01: salida bajo contrato | A-3 v0 · C.0a | Comparar encabezados, filas y total con B.1 y F-1 | **PASS**: 4 columnas, 4 filas, 330 min | A-3 v0 · C.0a · PDF p. 29; B.1 · PDF p. 28 |
| S11-ART-02: afirmación con cita que realmente la sustente | A-3 v0 · §5; F-1 | Confrontar afirmación de resolución y campo de resolución de MAT-2041 | **DEFECTO D-2 CONFIRMADO**: la cita no respalda reversión de certificado | A-3 v0 · C.0b · §5 · PDF p. 29; F-1 · MAT-2041 · resolución · K.3 · PDF p. 5 |
| S11-T3-01: ejecución consistente con traza | T-3 v0 · C.0c | Contrastar pasos trazados con operaciones declaradas | **PASS**: pasos de lectura, filtro, exclusión, conversión, suma y validación trazados; no hay acción que sostenga la resolución falsa | T-3 v0 · pasos 1–6 · PDF p. 30; A-3 v0 · C.0b · PDF p. 29 |

### Hallazgo localizado

**H-R3-01 · D-2 (cita sin respaldo):** `[A-3 v0 · §5 · C.0b · PDF p. 29]` sostiene que el incidente MAT-2041 fue resuelto revirtiendo el certificado. `[F-1 · MAT-2041 · resolución · K.3 · PDF p. 5]` registra, en cambio, **renovación del certificado y reinicio del balanceador**. `[T-3 v0 · pasos 1–6 · C.0c · PDF p. 30]` tampoco aporta una acción que pruebe la reversión. Se trata de un defecto localizado en la fundamentación, no de un fallo demostrado del filtro de filas.

**Métricas técnicas registradas:** 4 aserciones, 3 PASS, 1 defecto confirmado, 1 alerta y **0 falsos positivos** (0/1 alertas); 4/12 operaciones presupuestadas. El resultado corresponde a la verificación automatizada posterior, no a una ejecución individual histórica.

## R4 · Skill y banco de activación

La skill, el script determinista y el banco de peticiones fueron preparados con asistencia de IA y ejecutados con trazas conservadas. La versión inicial 1.0.0 obtuvo VP 10/10 y FP 4/10. Tras ajustar la descripción para acotar la activación, la versión 1.1.0 obtuvo **VP 10/10 y FP 0/10**, en veinte sesiones independientes, según `evals/resultados_activacion.jsonl`, `evals/reporte_activacion.json` y el histórico. El CLI verificó 4 filas, 330 minutos y exclusión de MAT-2048. Esta sección no declara nuevas ejecuciones.

## R5 · Descarte

El formateo exacto y la totalización se conservan como script determinista, no como nuevo agente. En el banco sintético declarado de 20 casos se registraron 20 PASS y 0 fallos. El umbral de reapertura documentado, **más de 2 fallos en 20 casos**, no se activó. Las evidencias y razones se detallan en `descartes.md` y `codex/reports/S06-10.json`.

## Estado final y limitaciones

- **R1–R3, documentación técnica:** **COMPLETA** con datos, medidas, contratos, localizadores y límites de procedencia.
- **R4–R5, resultados técnicos existentes:** conservados, sin alegar ejecuciones nuevas.
- **Acreditación individual sin IA de R1–R3:** **NO ACREDITADA**. No puede resolverse alterando texto ni suprimiendo declaraciones de procedencia.
- **Ceguera original en R3:** **NO ACREDITADA** por apertura anterior al contrato. El sello solo precede a la nueva verificación.
- **Fuentes privadas:** se citan por localizador; permanecen fuera de Git y del ZIP.

Se evita llamar «pendiente» a una casilla que tiene un resultado técnico documentado, sin convertir ese resultado en evidencia académica que no existe.
