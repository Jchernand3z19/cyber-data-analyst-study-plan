# Fase 2 — Python, APIs y calidad de datos

## Objetivo

Crear un pipeline pequeño y reproducible que reciba datos sintéticos o de una API pública autorizada, los valide, transforme y registre resultados sin filtrar secretos ni información sensible.

## Secuencia de estudio

| Días | Tema | Evidencia mínima |
|---|---|---|
| 19–20 | Variables, tipos, condiciones, bucles, funciones y errores | Script pequeño con entradas controladas |
| 21–22 | CSV/JSON, limpieza, nulos y duplicados | Antes/después y resumen de calidad |
| 23–25 | HTTP, APIs, paginación, límites y secretos | Cliente de API con configuración segura |
| 26–30 | Esquemas, logging, pruebas, errores y linaje | Validaciones, pruebas y registro de ejecución |
| 31–36 | Anomalías, integridad, pipeline y revisión | Pipeline reproducible con reporte de calidad |

## Laboratorio base

Usa un archivo CSV sintético con campos:
`product_id,store_id,observed_at,price,currency`.

Incluye deliberadamente:
- una fila válida;
- un precio nulo;
- un precio negativo;
- una fila duplicada;
- una fecha con formato inválido;
- una moneda no permitida.

Escribe un script que:
1. lea el archivo;
2. cuente filas iniciales;
3. valide campos obligatorios, tipos, rangos y formato de fecha;
4. separe registros válidos e inválidos;
5. detecte duplicados usando una clave de negocio documentada;
6. escriba resultados separados y un resumen sin datos sensibles;
7. finalice con un estado claro si la calidad no cumple los criterios.

No descartes silenciosamente filas: registra el motivo de rechazo y conserva una forma de rastrear el registro sintético original.

## Consumo responsable de APIs

- Usa solo APIs públicas o autorizadas y respeta sus términos.
- Define timeout, maneja códigos de estado y limita reintentos.
- Respeta límites de tasa; usa backoff cuando corresponda.
- No intentes evadir autenticación, CAPTCHA ni controles de acceso.
- Guarda credenciales fuera del código, por ejemplo en variables de entorno.
- No imprimas tokens ni encabezados de autorización en logs.

## Calidad y observabilidad

Mide como mínimo:
- **Completitud:** proporción de valores obligatorios presentes.
- **Validez:** proporción de valores que cumplen reglas.
- **Unicidad:** duplicados respecto de la clave elegida.
- **Consistencia:** reglas entre campos relacionadas.
- **Trazabilidad:** origen, momento de extracción y versión de transformación.

Cada ejecución debe dejar conteos de entrada, salida, rechazo y duplicados; fecha/hora; versión del script; y errores resumidos. No incluyas secretos ni datos personales.

## Entregables

- Script Python ejecutable y comentado.
- CSV sintético de entrada.
- Salida limpia, salida de rechazos y reporte de calidad.
- Pruebas para entradas válidas, inválidas, vacías y errores inesperados.
- README con pasos de ejecución y limitaciones conocidas.

## Criterios de aprobación

Puedes explicar cada función, reproducir la ejecución desde cero, demostrar que los registros inválidos no desaparecen sin explicación, probar al menos tres casos límite y verificar que los logs no contienen secretos. Si algo no se ejecutó, documéntalo como pendiente; no afirmes que pasó.
