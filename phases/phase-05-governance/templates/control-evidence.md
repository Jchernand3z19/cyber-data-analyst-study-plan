# Registro de evidencia de controles

> Completa este registro con resultados reales. No copies secretos, tokens, datos personales ni capturas que los contengan.

| Control ID | Control | Estado | Evidencia verificable | Limitación / riesgo pendiente | Fecha de revisión |
|---|---|---|---|---|---|
| CTL-001 | Credenciales fuera del código fuente | Propuesto | Revisar workflow y configuración de secretos sin revelar valores | No se ha verificado el contenido de los secretos | Pendiente |
| CTL-002 | Acceso mínimo a calendario | Parcialmente implementado | Script usa scope `calendar.events` | Falta revisar permisos efectivos y calendarios compartidos | Pendiente |
| CTL-003 | Datos sintéticos en laboratorios | Implementado en archivos de ejemplo | Revisar muestras del directorio `labs/` | No sustituir por datos reales | Pendiente |
| CTL-004 | Salidas locales excluidas del repositorio | Propuesto | Revisar reglas `.gitignore` y estado Git | Confirmar que no haya outputs ya versionados | Pendiente |

## Cómo registrar evidencia

- Identifica la ruta, comando o pantalla de configuración revisada.
- Registra el resultado, no el valor secreto.
- Distingue prueba ejecutada de inspección estática.
- Si una comprobación no puede realizarse con los permisos disponibles, deja el estado como pendiente.
- Si un secreto pudo exponerse, revócalo y reemplázalo; no lo pegues en el registro.
