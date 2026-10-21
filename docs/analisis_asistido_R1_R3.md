# Análisis técnico asistido R1-R3

> **Autoría y alcance.** Documento generado con asistencia de IA para el cierre
> técnico S06-09. No representa observaciones hechas por el/la estudiante en
> sala, no sustituye la bitácora individual y no vuelve admisibles las rondas
> R1-R3, donde la guía prohíbe IA generativa.

Contexto: variante 2, puesto P2 · Contexto, modalidad autónoma con
transcripciones. Los PDF originales estuvieron accesibles en `.local_sources/`
y permanecen fuera de Git.

## Fuentes y localizadores

- `S06_actividad_estudiante.pdf`, PDF pp. 3-5: puesto P2, requisitos generales,
  mazo D-1 a D-5 y procedimiento de R1-R3.
- `S06_complemento_estudiante.pdf`, PDF pp. 6-13 (impresas 5-12):
  transcripciones R1/R2, esquemas E1-E5 y conteo de supervivencia.
- `S06_complemento_estudiante.pdf`, PDF p. 28 (impresa 27): Anexo B, tabla B.1.
- `S06_complemento_estudiante.pdf`, PDF pp. 32-34 (impresas 31-33): Anexo C,
  variante 2, tablas C.2a-C.2c.
- `S06_apunte.pdf`, PDF pp. 2-3 y 14-15: razones admitidas y ficha de agente.
- `fixtures/registro_F1.csv`: reproducción comprobable de F-1 para pruebas; no
  reemplaza el PDF, las transcripciones ni los anexos.

SHA-256 de las fuentes privadas:

| Fuente | SHA-256 |
|---|---|
| actividad | `5abd1950c4dbca337507eb2156b399d414b6b5cf8a8ffb46652a8cc003526dd3` |
| complemento | `582de32be1103626301f6ddbcd45f7dc2672b837f083292635f6bfd9ecff7145` |
| apunte | `e06da4071bfe5f3b82802ba02e26df3237ba5c0ebbd67af89e3effa6c4726be7` |

## C1 · R1 y R2, lectura técnica

### Tabla 6.A asistida

Esta tabla describe hechos visibles en las transcripciones; no se presenta
como la experiencia personal solicitada por la actividad.

| Ronda | Qué recibió P2 | Decisiones implícitas o corrección | Qué descartó | Supervivencia técnica |
|---|---|---|---|---|
| R1 | Mensaje libre de P1 y F-1 completo. El mensaje pide incidentes graves de matrícula, semana del 9, tabla corta y tickets visibles. | Interpretó “graves” como Alta/Crítica; reconstruyó el intervalo 9-13; eligió campos y formato sin contrato; incluyó MAT-2048 aunque lo identificó como duplicado; transmitió reinicio del nodo 2 y aguas abajo se convirtió indebidamente en hipótesis causal. Faltaban columnas exactas, exclusión de duplicados, unidad minutos, máximo de filas y línea total. | Correo institucional, MAT-2066 por fecha y severidades Media/Baja. | **2/5** |
| R2 | Orden E1 íntegra, F-1 y esquema E2. | El primer envío usó `h:mm` donde E2 exigía entero y fue rechazado. El segundo convirtió 85, 70, 135 y 40 minutos, añadió fuente por fila y explicitó descartes. | MAT-2048 por duplicado; MAT-2043/MAT-2058 por Media; MAT-2052 por Baja. La consulta ya estaba acotada por sistema y fecha a ocho tickets. | **5/5** |

### Evaluación requisito por requisito contra Anexo B

| Requisito B.1 | R1 | R2 | Evidencia y primera pérdida en R1 |
|---|---:|---:|---|
| R1 · Formato: cuatro columnas y minutos | 0 | 1 | K.4 usa Ticket/Severidad/Causa/Duración, omite Fecha y expresa horas. La precisión se pierde en P1 → P2, donde el mensaje libre omite columnas y unidad. |
| R2 · Alcance: sistema, fecha y severidad | 1 | 1 | Las filas finales de ambas rondas pertenecen a Matrícula en línea, 9-13 de marzo, Alta/Crítica. |
| R3 · Exclusión de duplicados | 0 | 1 | K.4 incluye MAT-2048. La exclusión desaparece en P1 → P2 y P2 incorpora el duplicado. |
| R4 · Ticket exacto por fila | 1 | 1 | K.4 y K.6 conservan identificadores coincidentes con F-1. |
| R5 · Máximo cinco filas y línea total en minutos | 0 | 1 | K.4 tiene cinco filas, pero no termina con línea total en minutos. “Tabla corta” en P1 → P2 perdió el límite y la línea total. |

Comparación: **R1 2/5 frente a R2 5/5; mejora de 3 requisitos**. Los
esquemas vuelven verificables formato, exclusión y presupuesto. El rechazo del
primer E2 demuestra además que el contrato detecta una unidad/tipo incorrectos
antes de propagar la salida.

## C2 · Dos fichas técnicas propuestas

`agents/generador.yaml` y `agents/verificador.yaml` quedaron completas como
propuestas asistidas y no evaluables en R3. Ambas incluyen:

- una razón admitida nombrada;
- tres o cuatro herramientas enumeradas y permisos sin efectos laterales;
- formato de error con códigos y carga mínima;
- condiciones de término semántica, de presupuesto y de no progreso con
  umbrales enteros;
- métrica verificable y evaluaciones propuestas.

El verificador tiene id distinto, `adversarial_to` apunta al generador, recibe
solo contrato/artefacto/F-1/T-3 y excluye razonamiento y memoria del generador.

## C3 · Contrato automatizado y defecto de variante 2

### Precedencia y sello

El contrato `evidencias/contrato_automatizado_R3.json` se escribió antes de la
lectura automatizada actual del artefacto de variante 2. Se selló el
2026-10-20T22:51:26-03:00 con SHA-256
`5969c541fc1107562543ef88cdc55577806546833ba83c8a4d9b97f346539948`.

Esta precedencia acredita **solo esta ejecución automatizada asistida**. No
demuestra que existiera el contrato personal requerido antes de una apertura
original de Anexo C y no se retrofecha como tal.

### Resultados de las aserciones selladas

| Aserción | Resultado | Evidencia |
|---|---|---|
| A-F1-01 · recalcular selección | PASS | F-1 produce MAT-2041, MAT-2047, MAT-2055 y MAT-2061; 4 filas, 330 minutos; MAT-2048 excluido por duplicado. |
| A-ART-01 · trazabilidad y duplicados | PASS | [A-3 v2 · C.2a · PDF p. 32] frente a [F-1 · MAT-2048 · estado]. |
| A-ART-02 · no inventar causalidad | **FAIL · defecto confirmado** | [A-3 v2 · §6 · PDF p. 33] frente a [F-1 · MAT-2061 · causa y resolución · PDF p. 5]. |
| A-T3-01 · decisión reproducible en traza | PASS | [T-3 v2 · paso 2] filtra severidad y [T-3 v2 · paso 3] excluye MAT-2048 con resultado explícito. |

Hallazgo `H-1`: A-3 v2 §6 afirma que MAT-2061 se originó en una falla de red
del nodo 2. F-1 registra `Sin causa determinada`; reiniciar el nodo 2 aparece
solo en la resolución. La cita declarada por A-3 apunta precisamente a
resolución y no sostiene la causalidad. Clasificación: **D-1, afirmación sin
respaldo**.

Métricas capturadas: 4 aserciones ejecutadas, 3 PASS, 1 defecto confirmado,
1 alerta, 0 falsos positivos, tasa FP `0/1 = 0.0`. La parada fue semántica:
las cuatro aserciones quedaron con resultado y localizadores; se usaron 4 de
12 operaciones presupuestadas.

### Limitación procedimental

La primera extracción de texto se ejecutó sobre el PDF complemento completo.
El análisis y todos los resultados anteriores usan únicamente la variante 2,
pero no sería veraz afirmar que la herramienta solo abrió esas páginas. La
revisión visual posterior sí se acotó a las páginas 32-34.

## Admisibilidad académica

El cierre técnico C1-C3 es reproducible como demostración asistida. La entrega
académica continúa bloqueada: faltan observaciones propias de R1/R2 y un
contrato/hallazgo personal de R3 producido bajo la secuencia exigida y sin IA
generativa. Las fichas y este documento no deben copiarse como autoría
individual.
