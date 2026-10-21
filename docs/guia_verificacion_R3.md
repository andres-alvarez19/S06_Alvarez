# Guía de verificación adversarial R3

Plantilla para variante 2, P2 · Contexto. No es evidencia individual y no
contiene un defecto descubierto por IA. R3 prohíbe IA generativa.

## Orden verificable

1. Sin abrir Anexo C, escribir y cerrar el contrato previo.
2. Registrar una marca horaria auténtica de cierre del contrato.
3. Abrir Anexo C y registrar una segunda marca horaria auténtica, posterior a
   la primera.
4. Ejecutar cada aserción contra el artefacto o la traza indicada.
5. Registrar resultados y localizadores exactos, incluidos los negativos.
6. Aplicar las condiciones de término y calcular las métricas desde el registro.

Como los PDF, Anexo C, la guía D-1 a D-5 y las transcripciones no están en el
repositorio, este orden no se ha ejecutado aquí.

## Contrato previo

Completar antes de abrir Anexo C:

| Campo | Valor individual |
|---|---|
| Identificador del contrato | PENDIENTE |
| Variante y puesto | 2 · P2 Contexto |
| Marca horaria de cierre | PENDIENTE: hora auténtica |
| Aserción verificable | PENDIENTE |
| Artefacto o traza | PENDIENTE: al menos una aserción debe referirse a traza |
| Operación | PENDIENTE: qué se abre, recalcula o compara |
| Resultado esperado | PENDIENTE |
| Localizador previsto | PENDIENTE |
| Presupuesto | PENDIENTE: límite cuantitativo definido antes de ejecutar |
| Umbral de no progreso | PENDIENTE: número entero de intentos sin evidencia nueva |
| Marca horaria de apertura de Anexo C | PENDIENTE: hora auténtica posterior |

## Tabla 6.B

| Aserción | Artefacto/traza | Qué abre, recalcula o compara | Resultado | Localizador |
|---|---|---|---|---|
| PENDIENTE: aserción sobre traza | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE |

No escribir `PASS`, `FAIL` ni un hallazgo hasta efectuar la comparación real.

## Formato de hallazgo

```text
ID: H-<n>
Aserción: <id de la aserción del contrato previo>
Esperado: [A-3 v2 · §<n>] <texto observado en la fuente>
Observado: [F-1 · <ticket> · <campo>] <valor literal>
        o: [T-3 · paso <n>] <evento literal de la traza>
Operación: <apertura, recálculo o comparación efectuada>
Clasificación: <defecto confirmado | falso positivo>
Evidencia: <localizador reproducible>
```

El CSV F-1 puede aportar un valor literal de registro, pero no reemplaza A-3,
T-3 ni Anexo C. Sin ambos lados no existe un hallazgo confirmado.

## Métricas

- Defectos confirmados: conteo de hallazgos cuyo contraste fue reproducido.
- Falsos positivos: alertas descartadas tras comprobar ambos lados.
- Tasa de falsos positivos: `falsos_positivos / alertas_totales`, solo cuando el
  denominador sea mayor que cero.

No registrar una tasa si la ejecución no produjo el numerador y denominador.

## Condiciones de término

El contrato previo debe fijar valores concretos para las tres condiciones:

1. **Parada semántica verificable:** todas las aserciones contractuales tienen
   resultado y localizador reproducible.
2. **Presupuesto agotado:** se alcanzó el límite cuantitativo predefinido de
   operaciones, artefactos o tiempo; no se inventa después de observar datos.
3. **No progreso:** se alcanzó el umbral numérico predefinido de intentos
   consecutivos sin evidencia nueva.

