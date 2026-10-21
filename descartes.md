# Descartes de agentes — R5

## D-01 · Formateador-totalizador de tabla de incidentes

- **Componente considerado:** agente dedicado únicamente a convertir `h:mm` a
  minutos, sumar filas y emitir JSON con formato estable.
- **Hacia:** código determinista del arnés en
  `skills/cuadrar-tiempos-de-incidente/scripts/tabla_incidentes.py`, invocado
  por la skill `cuadrar-tiempos-de-incidente`.
- **Decisión:** no crear un agente adicional.

### Por qué no es agente

De las razones admisibles enumeradas por el contrato S06-06, este componente no
cumple, al menos, las siguientes:

- **Responsabilidad propia verificable:** no toma una decisión autónoma; aplica
  una transformación aritmética determinista que ya tiene pruebas unitarias.
- **Permisos distintos:** no necesita fuentes, lectura ni escritura diferentes
  de las que ya requiere el script de la skill.
- **Verificación adversarial:** no contrasta la salida de otro agente ni busca
  defectos; separar el formateo no crearía independencia adversarial.
- **Traspaso deliberado:** su entrada y salida son parte continua de una misma
  operación local, sin una frontera de responsabilidad que justifique handoff.

La alternativa conserva identificadores y causas literales, falla ante campos o
formatos inválidos y no trunca al superar el presupuesto. Esas propiedades son
comprobables como código y no requieren memoria, contexto propio ni autonomía.

### Medición que lo reabre

**Umbral definido:** reabrir la decisión si **más de 2 de 20**
tablas del banco específico de formato fallan validación por una ambigüedad que
no pueda resolverse con reglas deterministas y requiera una especialización con
contrato propio.

- **Denominador:** 20 casos versionados del banco sintético declarado
  `fixtures/sinteticos/formato_tablas.json`; cada caso contiene filtros y salida
  esperada o invariante.
- **Numerador:** casos cuya salida viole el esquema, el conteo de filas o la suma
  recalculada, después de excluir fallos de entrada ya cubiertos por errores
  estructurados.
- **Método:** ejecutar los 20 casos, validar JSON, comprobar
  `row_count == len(rows)` y recalcular `total_minutos`; conservar resultados
  caso a caso antes de contar fallos.
- **Regla falsable:** `fallos > 2` reabre el análisis; `fallos <= 2` no lo reabre
  por este criterio.

### Ejecución técnica S06-10

El banco se generó con `generated=true` y `synthetic=true` y se ejecutó sobre
la reproducción F-1. Resultado real de la ejecución actual: **20/20 casos
pasaron, 0/20 fallaron**, por lo que `fallos > 2/20` no se activó. La salida
caso a caso está en `evals/resultados_formato_tablas.jsonl` y el resumen en
`evals/reporte_formato_tablas.json`.

Esta cifra valida el comportamiento técnico del script frente al banco
sintético; no se presenta como observación de una ronda pasada, medición de
producción ni evidencia individual.

## Fuente y limitación

La lista de siete razones se verificó en
`.local_sources/S06_actividad_estudiante.pdf`, apartado “Las razones admitidas
para que un agente exista”, y se contrastó con la figura 6.1 del apunte. Las
fuentes privadas permanecen ignoradas por Git. El criterio `>2/20` fue
ejecutado únicamente como prueba técnica sintética y se mantiene separado de
cualquier evidencia académica o de producción.

