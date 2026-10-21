# Auditoría S06 — NO_APTO_ENTREGA

Fecha de auditoría: 2026-10-20 (fecha del entorno de ejecución).

Resultado final: **BLOQUEADO / NO_APTO_ENTREGA**.

No se creó `S06_Alvarez.zip`. Las pruebas de software pasan, pero no sustituyen
las evidencias individuales restringidas ni levantan las compuertas C2, C3 y C4.
C3 insuficiente exige reentrega según el manifiesto.

## Matriz C1–C4

| Criterio | Estado | Evidencia concreta | Pendiente o fallo |
|---|---|---|---|
| C1 · R1/R2 | PENDING | `bitacora.md` contiene Tabla 6.A con dos filas R1/R2 y columnas requeridas; `docs/instrucciones_R1_R2.md` documenta el método. | Ambas filas conservan observaciones, cifras n/5 y comparación como PENDIENTE. Faltan PDF y Anexo B. |
| C2 · fichas y términos | PENDING | `agents/generador.yaml` y `agents/verificador.yaml` parsean; el verificador es distinto, adversarial e aislado; ambos enumeran semantic, budget y no_progress. | Son plantillas no evaluables: conservan PENDIENTE y umbrales nulos. `tests/test_agents.py` confirma que el validador las rechaza como completas. Faltan complemento §4.3 y apunte. |
| C3 · contrato previo y defecto | FAIL · BLOQUEANTE | `docs/guia_verificacion_R3.md` y Tabla 6.B preparan aserción sobre traza y localizadores `[A-3 v2 · §n]`, `[F-1 · ticket · campo]`, `[T-3 · paso n]`. | No existe contrato previo ejecutado, dos horas auténticas, Anexo C, resultado, localizador observado ni hallazgo real. Exige reentrega. |
| C4 · skill, banco y descarte | FAIL | Skill válida, CLI funcional, 6 pruebas específicas y corrida real con 4 filas/330 minutos. Banco definido con 10 positivos + 10 negativos (5 cercanos). `descartes.md` propone umbral >2/20 con método y denominador. | `evals/resultados_activacion.jsonl` tiene 0 resultados; VP/FP son nulos porque faltan K.11 y evaluación real. El umbral de descarte no fue ejecutado. |

## Autoría y modalidad

- R1–R3 están rotulados como plantillas asistidas y pendientes. No se aprueban
  académicamente ni se atribuyen a la persona estudiante.
- R4–R5 registran asistencia de Codex en `bitacora.md`.
- La matrícula completa permanece pendiente; no se inventó.
- Los tres PDF declarados por el manifiesto no están en el repositorio. El CSV
  de `fixtures/` reproduce F-1 para pruebas y no sustituye guía, transcripciones,
  Anexo B ni Anexo C.

## Validaciones ejecutadas

```text
python -m pytest -q
............... [100%]
15 passed in 0.41s
```

```text
python -c "from pathlib import Path; import yaml; files=list(Path('agents').glob('*.yaml')); [yaml.safe_load(p.read_text(encoding='utf-8')) for p in files]; print(f'{len(files)} YAML válidos')"
2 YAML válidos
```

```text
python -c "from pathlib import Path; import json; files=list(Path('evals').glob('*.jsonl')); counts={str(p):len([json.loads(line) for line in p.read_text(encoding='utf-8').splitlines() if line.strip()]) for p in files}; print(counts)"
{'evals/activacion.jsonl': 20, 'evals/resultados_activacion.jsonl': 0}
```

```text
python -m compileall -q .
# salida vacía; código 0
```

```text
python skills/cuadrar-tiempos-de-incidente/scripts/tabla_incidentes.py --registro fixtures/registro_F1.csv --sistema 'Matrícula en línea' --desde 2026-03-09 --hasta 2026-03-13 --severidad 'Alta,Crítica' --max-filas 5 --out /tmp/tabla_s06_auditoria.json
# código 0; status=ok, row_count=4, total_minutos=330
```

## Requisitos para levantar el bloqueo

1. Incorporar o facilitar los tres PDF originales, Anexo B, Anexo C y las
   transcripciones aplicables; no reemplazarlos con F-1.
2. Completar personalmente R1 y R2 con dos mediciones, cifras n/5 y comparación.
3. Completar personalmente las fichas R3 con razones, contratos y umbrales
   numéricos; volver a ejecutar su validador.
4. Ejecutar R3 en el orden prescrito, con dos marcas horarias auténticas,
   aserción sobre traza, localizadores y al menos un hallazgo real reproducible.
5. Recuperar las cuatro descripciones originales K.11 y correr los 20 casos de
   activación de forma independiente, conservando evaluador/modelo y elecciones.
6. Recalcular VP/FP desde esos resultados. Si no cumple VP ≥ 9/10 y FP ≤ 1/10,
   versionar la descripción, corregirla y repetir los veinte casos.
7. Repetir esta auditoría. Crear el ZIP solo si todas las compuertas pasan con
   evidencia auténtica.

