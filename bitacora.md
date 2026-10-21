# Bitácora S06

- Variante: **2**
- Puesto: **P2 · Contexto**
- Modalidad: **autónoma con transcripciones**
- Matrícula completa: **PENDIENTE DE COMPLETAR POR EL/LA ESTUDIANTE**

> Las secciones R1–R3 son una plantilla. No contienen observaciones, inferencias,
> marcas horarias ni hallazgos generados por IA. Deben completarse personalmente
> a partir de la guía, las transcripciones y los anexos originales.

## Tabla 6.A — R1 y R2

| Ronda | Puesto | Qué recibí | Qué inferí (campo del contrato faltante) | Qué descarté | Supervivencia n/5 |
|---|---|---|---|---|---|
| R1 | P2 · Contexto | PENDIENTE: observación propia | PENDIENTE: inferencia propia y campo faltante | PENDIENTE | PENDIENTE |
| R2 | P2 · Contexto | PENDIENTE: observación propia | PENDIENTE: esquema E2 y campo faltante | PENDIENTE | PENDIENTE |

Comparación R1/R2: **PENDIENTE DE MEDICIÓN PERSONAL**.

> **Referencia técnica asistida (no evaluable como trabajo individual):**
> `docs/analisis_asistido_R1_R3.md` aplica Anexo B a las transcripciones y
> obtiene 2/5 en R1 y 5/5 en R2. Es una demostración producida por IA; no se
> copia a esta tabla como observación propia.

## Tabla 6.B — R3

### Contrato previo (completar antes de abrir Anexo C)

- Marca horaria de cierre del contrato: **PENDIENTE (hora auténtica)**
- Aserción: **PENDIENTE**
- Artefacto o traza esperada: **PENDIENTE**
- Operación de verificación: **PENDIENTE**
- Resultado esperado: **PENDIENTE**
- Localizador previsto: **PENDIENTE**
- Marca horaria de apertura del Anexo C: **PENDIENTE (hora auténtica posterior)**

| Aserción | Artefacto/traza | Qué abre, recalcula o compara | Resultado | Localizador |
|---|---|---|---|---|
| PENDIENTE: incluir al menos una aserción sobre traza | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE |

Hallazgo que enfrenta `[A-3 v2 · §n]` con `[F-1 · ticket · campo]` o
`[T-3 · paso n]`: **PENDIENTE DE VERIFICACIÓN PERSONAL**.

Condición de término observada y métricas de defectos/falsos positivos:
**PENDIENTE DE EJECUCIÓN PERSONAL**.

> **Referencia técnica asistida (no evaluable como trabajo individual):** el
> contrato automatizado actual fue sellado en
> `evidencias/contrato_automatizado_R3.json` antes de la lectura automatizada
> actual de la variante 2. Su ejecución y el defecto D-1 confirmado están en
> `docs/analisis_asistido_R1_R3.md`. Esta precedencia no demuestra el contrato
> personal original ni levanta el pendiente de R3.

## R4 — Skill y banco de activación

Uso de IA registrado: el 2026-10-20 Codex preparó el borrador de la skill, el
script determinista, las pruebas y el banco de peticiones. Los resultados que
figuren como ejecutados deben proceder de comandos realmente corridos y quedar
referenciados en `codex/reports/`.

- Ejecución funcional real de S06-04: `6 passed`; el CLI devolvió 4 filas y 330
  minutos para Matrícula en línea, 9–13 de marzo, Alta/Crítica. Evidencia en
  `codex/reports/S06-04.json`.
- Descripción evaluada: versión final `1.1.0` del frontmatter de
  `skills/cuadrar-tiempos-de-incidente/SKILL.md`.
- Catálogo: las cuatro descripciones literales de K.11 fueron verificadas en el
  PDF privado y en `.local_sources/catalogo_K11.json`.
- Evaluador y condiciones: `codex-cli 0.163.0`, modelo `gpt-5.6-luna`,
  razonamiento `none`, veinte sesiones efímeras independientes, secuenciales y
  sin historial compartido. Cada registro conserva hora, id de sesión,
  referencia y SHA-256 de la salida cruda.
- Primera corrida, versión `1.0.0`: **VP 10/10, FP 4/10**; no alcanzó el umbral.
  Se conserva en `evals/history/20261021T013145Z_gpt-5.6-luna-none_v1.0.0/`.
- Reescritura: se estrechó la descripción a filtrado y totalización exactos de
  un CSV suministrado y se añadió `ninguna-skill` para peticiones sin coincidencia.
- Segunda corrida, versión `1.1.0`: **VP 10/10, FP 0/10**; cumple VP ≥ 9/10 y
  FP ≤ 1/10. Los veinte resultados están en
  `evals/resultados_activacion.jsonl` y las salidas crudas en el directorio
  indicado por `evals/reporte_activacion.json`.

## R5 — Descarte

Uso de IA registrado: el 2026-10-20 Codex preparó un borrador de descarte y su
criterio cuantitativo de reapertura. En S06-10 el umbral se ejecutó sobre un
banco sintético declarado de 20 casos: 20 pasaron y 0 fallaron. Este resultado
es una prueba técnica actual, no una medición histórica o de producción. Las
siete razones se contrastaron con la guía privada. Véase `descartes.md`.

## Cierre integral técnico S06-10

Uso de IA registrado: Codex generó una reconstrucción técnica a partir de las
transcripciones y anexos privados, creó y selló un contrato nuevo para la
verificación automatizada actual, ejecutó las aserciones y preparó el paquete.
No se completaron las casillas personales de R1-R3 ni se inventó matrícula.

- Fuente observada: PDF privado del complemento, con referencias de página,
  tabla, sección y paso; no se publica.
- Reconstrucción asistida: `docs/reconstruccion_tecnica.md`; no es observación
  presencial ni autoría individual.
- Ejecución real actual: contrato y sello en
  `evidencias/contrato_cierre_integral_R3.*`, resultados en
  `evidencias/verificacion_cierre_integral_R3.json`.
- Fixture reproducido: `fixtures/registro_F1.csv`; no sustituye anexos.
- Fixture sintético declarado: `fixtures/sinteticos/formato_tablas.json`, con
  `generated=true`, `synthetic=true`, motivo, generador y timestamp real.
- Banco sintético R5 ejecutado: 20/20 casos pasaron; 0 fallos; el umbral
  propuesto `fallos > 2/20` no se activó. Es prueba técnica actual, no una
  medición histórica o de producción.
- R4 se preservó sin llamadas nuevas al modelo: VP 10/10, FP 0/10 y hashes
  idénticos a S06-09.

Estado: **COMPLETO_TECNICO**. Conformidad académica: **PENDIENTE R1-R3** por la
prohibición de IA generativa y por falta de producción personal; el ZIP técnico
no equivale a una entrega aprobada.

