# Codex · S06

Lee `codex/manifest.json` y ejecuta cada contrato en orden. Cada JSON es una especificación de tarea, no una tarea que se inicia automáticamente por existir en GitHub.

Contexto: variante 2, P2 Contexto, autónoma. No inventar matrícula, horas, auditorías, llamadas a herramientas, resultados de pruebas ni métricas.

R1-R3: el complemento prohíbe IA generativa. Solo preparar estructura y, opcionalmente, demostraciones etiquetadas como asistidas; no sustituir los resultados individuales ni ocultar autoría.

R4-R5: IA permitida para borradores con registro real de uso. Crear script funcional, ejecutar banco y calcular métricas desde salidas capturadas.

Cada contrato genera un informe en `codex/reports/<id>.json` con estado passed/partial/blocked/failed, outputs, comandos y pruebas. No declarar passed si faltan fuentes o pruebas.

Si los PDFs originales no están accesibles en Codex, indicarlo. El CSV de `fixtures/` reproduce F-1 pero no sustituye la guía, transcripciones ni Anexo C. No fabricar respuesta con fuente inexistente.

Meta banco: 10 positivos y 10 negativos (3 cercanos), VP >= 9/10 y FP <= 1/10. C3 insuficiente => reentrega. ZIP solo si auditoría declara elegibilidad real.
