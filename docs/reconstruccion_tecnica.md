# Reconstrucción técnica S06-10

> Documento asistido por IA. Reconstruye técnicamente R1-R3 desde las fuentes
> privadas y pruebas actuales; no representa observación presencial, autoría
> individual ni aprobación académica.

Contexto: variante 2, P2 · Contexto, modalidad autónoma con transcripciones.
Los PDF se consultaron en `.local_sources/`, carpeta ignorada por Git, y no se
incluyen en el paquete.

## Clasificación de procedencia

| Clase | Contenido | Uso permitido |
|---|---|---|
| Fuente observada | Transcripciones P2, esquemas E1-E5, Anexo B, Anexo C v2 y T-3 leídos del complemento privado. | Sustentar la reconstrucción con página, tabla, sección o paso. |
| Reconstrucción asistida | Interpretación de decisiones de P2, conteos n/5, contrato y verificación automatizados. | Demostración técnica, nunca registro personal de R1-R3. |
| Reproducción de prueba | `fixtures/registro_F1.csv`, contrastado con la tabla K.3. | Recálculo determinista; no sustituye los PDF. |
| Sintético declarado | Banco R5 en `fixtures/sinteticos/formato_tablas.json`. | Prueba actual del código; no evidencia de ronda ni producción. |
| Evidencia real de ejecución | Salidas de CLI, pytest, sellos SHA-256 y resultados R4 ya preservados. | Acreditar que los comandos indicados sí se ejecutaron. |

## C1 · Reconstrucción R1 y R2

Fuentes: transcripciones del complemento, PDF pp. 6-13; esquema E2 en las
transcripciones; Anexo B, tabla B.1, PDF p. 28 (impresa 27).

| Ronda | Datos recibidos por P2 | Supuestos/decisiones y descartes | Resultado técnico |
|---|---|---|---|
| R1 | Mensaje libre de P1 y F-1 completo. El mensaje pide incidentes graves de matrícula, semana del 9, tabla corta y tickets visibles. | P2 interpreta graves como Alta/Crítica y la semana como 9-13. Descarta correo, fecha 16 y severidades Media/Baja, pero incluye MAT-2048 aunque observa que es duplicado. Faltan columnas exactas, unidad minutos, exclusión contractual y total. | 2/5 requisitos sobreviven. |
| R2 | Orden E1, F-1 y esquema E2. | El primer E2 usa `h:mm` donde se exige entero y el validador lo rechaza. El reenvío convierte 85/70/135/40, conserva fuentes y descarta MAT-2048, MAT-2043, MAT-2052 y MAT-2058 con motivo. | 5/5 requisitos sobreviven. |

| Requisito de Anexo B | R1 | R2 | Fundamento |
|---|---:|---:|---|
| R1 Formato | 0 | 1 | En R1 la tabla final no conserva exactamente Ticket/Fecha/Causa/Minutos y usa horas; E2 corrige tipo y unidad. |
| R2 Alcance | 1 | 1 | Sistema, fechas y severidades se mantienen. |
| R3 Exclusión | 0 | 1 | R1 incluye MAT-2048; R2 lo descarta explícitamente. |
| R4 Evidencia | 1 | 1 | Los tickets se conservan literalmente. |
| R5 Presupuesto | 0 | 1 | R1 no termina con total en minutos; R2 entrega cuatro filas y total 330. |

Comparación reconstruida: **R1 = 2/5; R2 = 5/5; mejora = +3**. La primera
pérdida de formato, exclusión y presupuesto ocurre en P1 → P2 cuando el mensaje
libre omite esos campos del contrato. Esta medición es asistida, no personal.

## C2 · Agentes

`agents/generador.yaml` y `agents/verificador.yaml` son propuestas técnicas
asistidas. Declaran razón admitida, contratos de entrada/salida, herramientas
enumeradas, permisos mínimos, política de contexto aislado, errores, métrica y
tres condiciones operacionales: semántica, presupuesto y no progreso. El
verificador es distinto y `adversarial_to` apunta al generador.

## C3 · Verificación actual

El contrato `evidencias/contrato_cierre_integral_R3.json` fue creado a las
`2026-10-21T01:59:03Z` y sellado a las `2026-10-21T01:59:21Z` con SHA-256
`aeed90e62939b8217498cc53c94b515a65fd2dd0ef1decab98c6721e6d319e5c`.
El acceso de esta ejecución a la fuente comenzó a las `2026-10-21T01:59:31Z`
y el recálculo quedó capturado a las `2026-10-21T01:59:42Z`.

El Anexo C ya había sido leído durante S06-09. Por eso este orden temporal solo
demuestra que el contrato precedió a la **nueva verificación S06-10**; no prueba
precedencia histórica ni reemplaza el contrato personal exigido.

| Aserción | Veredicto | Dos localizadores exactos |
|---|---|---|
| S10-F1-01 | PASS: MAT-2041, MAT-2047, MAT-2055, MAT-2061; 4 filas; 330 min; MAT-2048 excluido. | F-1 · cuatro tickets · campos de filtro/duración; F-1 · MAT-2048 · estado. |
| S10-ART-01 | PASS: C.2a conserva cuatro tickets y omite el duplicado. | A-3 v2 · C.2a · PDF p. 32; F-1 · MAT-2048 · K.3 · PDF p. 5. |
| S10-ART-02 | **DEFECTO D-1**: §6 atribuye una falla de red no sustentada. | A-3 v2 · §6/C.2b · PDF p. 33; F-1 · MAT-2061 · causa/resolución · K.3 · PDF p. 5. |
| S10-T3-01 | PASS: paso 2 filtra severidad y paso 3 excluye el duplicado. | T-3 v2 · C.2c · paso 2 · PDF p. 34; T-3 v2 · C.2c · paso 3 · PDF p. 34. |

Métricas actuales: 4 aserciones, 3 PASS, 1 defecto confirmado, 1 alerta, 0
falsos positivos, tasa FP 0/1 y 4 de 12 operaciones. La parada fue semántica.

## C4 y R5

R4 se preservó sin llamadas nuevas: 20 sesiones independientes, VP 10/10 y FP
0/10. R5 mantiene el descarte del formateador como agente. Para cerrar su
denominador se ejecutó el banco sintético declarado de 20 casos: 20 pasaron, 0
fallaron y el umbral de reapertura `fallos > 2/20` no se activó. Es una prueba
técnica actual, no una métrica de producción ni una observación histórica.

## Condición final

El conjunto queda **COMPLETO_TECNICO**. La **CONFORMIDAD_ACADEMICA** de R1-R3
sigue pendiente porque esas rondas prohíben IA generativa y requieren trabajo
personal; la matrícula también permanece pendiente. El paquete técnico puede
crearse con esta advertencia, pero no debe llamarse entrega académica aprobada.
