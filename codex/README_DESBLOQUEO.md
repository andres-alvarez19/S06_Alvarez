# Recuperación del bloqueo de S06

## Estado reportado
- Implementación local de Codex: 15 pruebas pasadas y script de R4: 4 filas, 330 minutos.
- Banco: 20 peticiones preparadas, **0 peticiones realmente evaluadas**.
- R1–R3 pendientes de autoría individual; C3 es bloqueante.
- Los cambios locales de Codex aún **no aparecen** en GitHub `main` (verificar `git status` y sincronizar).

## Fuentes
Los tres PDF originales y las cuatro descripciones K.11 se distribuyen **separadamente** en un ZIP privado. Extraer en `.local_sources/` (carpeta ignorada por Git), no publicarlos en GitHub.

Archivos esperados:
- `.local_sources/S06_actividad_estudiante.pdf`
- `.local_sources/S06_complemento_estudiante.pdf`
- `.local_sources/S06_apunte.pdf`
- `.local_sources/catalogo_K11.json`

Anexo B, Anexo C y transcripciones están **dentro** del complemento, no son documentos independientes.

## Reanudar
1. Guardar y subir los cambios locales de la primera ejecución. Si hay cambios en GitHub desde el clone: hacer `git commit`, `git pull --rebase origin main`, `git push`, resolviendo conflictos si aparecen.
2. Incorporar las fuentes privadas dentro de `.local_sources/`.
3. Ejecutar `codex/contracts/08_desbloqueo_fuentes_banco.json`.
4. Ejecutar un **selector real** (nueva solicitud/contexto por petición) para las 20 peticiones de `evals/activacion.jsonl`; reportar proveedor/modelo. Sin credenciales/selector, no hay cifras de VP ni FP auténticas.
5. Ejecutar QA y actualizar `AUDITORIA.md`. No marcar apto hasta resolver R1–R3 bajo las reglas de la guía.

El contenido evaluable de R1–R3 no se puede atribuir falsamente al estudiante. Las fuentes por sí solas no crean contrato previo ni prueba individual.
