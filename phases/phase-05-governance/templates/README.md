# Kit de gobierno de datos — PharmaTracker

Plantillas educativas para documentar un proyecto de datos con información ficticia. No son políticas corporativas ni asesoría legal. Completa cada archivo con evidencia verificable; si un control aún no existe, escribe **Propuesto** o **Pendiente**, nunca **Implementado**.

## Archivos

| Archivo | Uso |
|---|---|
| [data-inventory.csv](data-inventory.csv) | Inventario de conjuntos de datos y propósito |
| [data-dictionary.csv](data-dictionary.csv) | Definición y clasificación de campos |
| [access-matrix.csv](access-matrix.csv) | Roles, permisos y justificación |
| [data-lineage.csv](data-lineage.csv) | Trazabilidad desde la fuente hasta el reporte |
| [quality-rules.csv](quality-rules.csv) | Reglas y criterios de aceptación |
| [risk-register.csv](risk-register.csv) | Riesgos, controles y riesgo residual |
| [retention-register.csv](retention-register.csv) | Retención y eliminación |
| [control-evidence.md](control-evidence.md) | Evidencia, estado y limitaciones de controles |

## Instrucciones

1. Conserva los ejemplos ficticios o sustitúyelos solo por datos sintéticos.
2. Asigna un identificador estable a cada conjunto de datos, campo, regla y riesgo.
3. Define escalas de probabilidad e impacto antes de puntuar riesgos.
4. En permisos, aplica mínimo privilegio y documenta quién aprobó cada acceso.
5. No incluyas nombres, correos, identificadores personales, credenciales ni datos de clientes reales.
6. No establezcas plazos legales de retención por intuición: documenta la política autorizada aplicable o deja el plazo como pendiente de validación.
7. Revisa que los conteos y definiciones coincidan entre inventario, diccionario, linaje y reglas de calidad.

## Estados permitidos

- **Propuesto:** diseño recomendado, aún no implementado.
- **Implementado:** existe configuración o procedimiento y hay evidencia reproducible.
- **Pendiente:** falta información, aprobación o ejecución.
- **No aplica:** justificado por escrito.

## Criterio de salida

Otra persona debe poder identificar qué datos existen, para qué se usan, quién puede acceder, cómo se transforman, qué controles están probados y qué riesgos siguen abiertos.
