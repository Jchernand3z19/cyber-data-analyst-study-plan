# Plantilla de ticket — caso sintético

Ejercicio documental; no simula respuesta activa ni autoriza acciones.

| Campo | Ejemplo |
|---|---|
| Ticket | CASE-SYN-001 |
| Fecha UTC | 2026-01-15T10:05:00Z |
| Categoría | Autenticación |
| Observación | 6 fallos y 1 éxito en 12 minutos para alias demo |
| Fuente | auth_events_synthetic.csv |
| IDs | E101–E107 |
| Usuario/activo | analyst_demo / endpoint_demo |
| Impacto | No disponible |
| Estado | Pendiente de contexto |
| Evidencia | Tabla por minuto y resultado |
| Interpretación | Actividad inusual; no confirma incidente |
| Datos faltantes | MFA, dispositivo, origen confiable, autorización, historial base, zona horaria |
| Datos sobrantes | Contraseña, token, contenido personal, IP completa si no es necesaria |
| Limitaciones | Dataset sintético, una fuente, sin contexto de identidad/dispositivo |

## Análisis
Distinguir observación, interpretación e hipótesis; cuantificar volumen/ventana/cobertura; indicar datos faltantes y campos a excluir; no proponer bloqueo, contención ni acciones técnicas.
