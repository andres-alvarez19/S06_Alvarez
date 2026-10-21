# Reconstrucción técnica S06-11 · variante 0 / P1 Admisión

> Documento asistido por IA. No representa observación presencial ni autoría
> individual de R1-R3. Las casillas personales de `bitacora.md` siguen abiertas.

## Fuentes y asignación

Los tres PDF originales se consultaron desde `.local_sources/`, fuera de Git y
del ZIP. El complemento indica que el último dígito de la matrícula fija puesto
y variante: `0` corresponde a variante 0 y P1 Admisión (PDF pp. 2-3). El SOBRE
P1 está en PDF p. 25; las transcripciones P1, en pp. 6 y 10.

## C1 · medición asistida de R1 y R2

| Ronda | Qué recibe P1 | Decisiones observables en la transcripción | Resultado final |
|---|---|---|---|
| R1 | Encargo literal con sistema, fechas, severidades, cuatro columnas, exclusión de duplicados, ticket exacto, máximo cinco filas y total en minutos. | P1 lo reduce a “incidentes graves”, “semana del 9”, “tabla corta” y tickets visibles. En la frontera P1→P2 desaparecen columnas/fecha/unidad, exclusión explícita y presupuesto exacto. | 2/5 requisitos sobreviven. |
| R2 | El mismo encargo y esquema E1. | P1 conserva objetivo, consumidor, alcance, exclusiones, evidencia, presupuesto y formato en una orden validada. Los puestos posteriores corrigen `h:mm` a enteros antes de entregar. | 5/5 requisitos sobreviven. |

| Requisito de Anexo B | R1 | R2 | Primera pérdida o conservación |
|---|---:|---:|---|
| R1 Formato | 0 | 1 | P1→P2 omite las cuatro columnas exactas y la unidad minutos; la tabla final R1 usa otra estructura y horas. |
| R2 Alcance | 1 | 1 | La cadena conserva matrícula, semana del 9 al 13 y severidad Alta/Crítica. |
| R3 Exclusión | 0 | 1 | P1→P2 omite excluir duplicados; R1 incluye MAT-2048. E1 lo conserva en R2. |
| R4 Evidencia | 1 | 1 | Ambas salidas finales conservan tickets literales. |
| R5 Presupuesto | 0 | 1 | “Tabla corta” pierde el máximo exacto y la línea total; E1 conserva ambos en R2. |

Comparación técnica: **R1 = 2/5; R2 = 5/5; mejora = +3**. Fuente:
transcripciones, PDF pp. 6-13; Anexo B, tabla B.1, PDF p. 28 (impresa 27).

## C2 · fichas coherentes con P1

El primer incremento de P1 es transformar el encargo literal en E1. Por eso la
ficha generadora vigente es `estructurar_encargo_admision`; su verificador
adversarial es `verificar_orden_admision`. Ambas enumeran herramientas,
permisos, aislamiento, fallos, métrica y términos semántico, de presupuesto y
de no progreso. Los esquemas y casos de prueba usan la misma frontera P1→P2.

## C3 · variante 0

La variante 0 se abrió antes de escribir el contrato S06-11 durante esta
corrección. Esa prelectura está declarada: el sello acredita únicamente que el
contrato precedió a la nueva ejecución automatizada, no ceguera histórica.

La ejecución verificó cuatro aserciones. Tres pasaron y una confirmó el defecto:

- `[A-3 v0 · §5 · tabla C.0b · PDF p. 29 (impresa 28)]` afirma que MAT-2041
  se resolvió revirtiendo el certificado a una versión anterior.
- `[F-1 · MAT-2041 · resolución · tabla K.3 · PDF p. 5]` registra que se renovó
  el certificado y se reinició el balanceador.
- Clasificación: **D-2 · cita que no respalda esa afirmación**.
- T-3 v0 (tabla C.0c, PDF p. 30) registra lectura, filtro, exclusión,
  conversión, suma y validación; no aporta una operación que sostenga §5.

Resultado capturado: 4 aserciones, 3 PASS, 1 defecto confirmado, 1 alerta y 0
falsos positivos. Véanse `evidencias/contrato_variante_0_R3.json` y
`evidencias/verificacion_variante_0_R3.json`.

## C4 · preservación

La skill y el banco R4 no dependen de la variante: se preservan la segunda
corrida real, VP 10/10 y FP 0/10. El script determinista sigue devolviendo 4
filas y 330 minutos para el caso F-1. El descarte cuantificado permanece válido.

## Condición

C1-C4 quedan técnicamente verificables con fuentes y ejecuciones reales. La
conformidad académica de R1-R3 permanece pendiente porque la guía prohíbe IA
generativa para esas rondas y exige producción individual.
