# Fase 5 — Gobierno, privacidad y proyecto final

## Objetivo

Demostrar que PharmaTracker puede describirse y revisarse como un flujo de datos controlado: fuentes, propósito, clasificación, calidad, acceso, retención, trazabilidad y riesgos documentados.

## Secuencia de estudio

| Días | Tema | Evidencia mínima |
|---|---|---|
| 71–75 | Roles, inventario, metadatos, linaje y reglas de calidad | Inventario y diccionario de datos |
| 76–80 | Privacidad, retención, acceso, incidentes y riesgos | Matriz de controles |
| 81–83 | Políticas, proveedores y revisión de cumplimiento | Lista de verificación con límites explícitos |
| 84–90 | Arquitectura, extracción, almacenamiento, análisis y auditoría final | Paquete final reproducible |

## Proyecto integrador PharmaTracker

Documenta el flujo desde la fuente autorizada hasta el reporte analítico:
1. Fuente y permiso de uso.
2. Extracción y frecuencia.
3. Validación y normalización.
4. Identificador de origen y trazabilidad.
5. Almacenamiento de observaciones históricas y precio actual derivado.
6. Reglas de acceso y gestión de secretos.
7. Transformaciones analíticas y definiciones de métricas.
8. Reporte de calidad, anomalías y cambios de precio.
9. Retención, eliminación y respuesta a errores.
10. Limitaciones, riesgos residuales y responsables propuestos.

No afirmes que una integración existe si aún no se ha implementado. Separa claramente estado actual, diseño propuesto y trabajo pendiente.

## Matriz de riesgos mínima

Para cada riesgo registra: activo o proceso, escenario, probabilidad, impacto, controles existentes, control propuesto, evidencia, responsable y riesgo residual. Usa escalas definidas y explica por qué asignaste cada valor.

## Gobierno y privacidad

- Identifica propósito y base autorizada para cada fuente; no hagas afirmaciones legales concluyentes.
- Recoge solo campos necesarios para el propósito definido.
- Define propietarios, custodios, usuarios y responsabilidades.
- Documenta reglas de calidad, excepciones y linaje.
- Revisa permisos por necesidad de uso y registra cambios.
- Define retención según necesidad, obligaciones aplicables y política autorizada.
- No subas credenciales, información personal real ni datos confidenciales al repositorio público.

## Entregables finales

- Diagrama de arquitectura y flujo de datos.
- Inventario y clasificación de campos.
- Diccionario de datos y catálogo de métricas.
- Linaje desde la fuente hasta el reporte.
- Reglas de calidad y resultados de pruebas.
- Matriz de acceso y riesgos.
- Procedimiento de gestión de secretos, logs, retención y errores.
- Reporte final con hallazgos, recomendaciones, límites y evidencia reproducible.

## Criterios de aprobación final

El proyecto se considera aprobado solo si otra persona puede seguir la documentación, reproducir las verificaciones disponibles, entender los límites de la solución y distinguir controles implementados de controles propuestos. Las afirmaciones deben estar respaldadas por evidencia; las brechas se documentan, no se ocultan.
