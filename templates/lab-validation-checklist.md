# Checklist de validación de laboratorios

Completa una fila con evidencia real antes de declarar una herramienta validada. No supongas compatibilidad, consumo ni disponibilidad de una cuenta.

| Campo | SQL cliente | APIs | Power BI | SIEM |
|---|---|---|---|---|
| Herramienta / versión | SQLite + cliente CLI o GUI; versión por registrar | Python + cliente HTTP; versiones por registrar | Power BI Desktop; versión por registrar | Herramienta SIEM: no decidida. Candidatas: Wazuh (local, open source), ELK (local, open source). Splunk Cloud Trial: descartado (no local, no reproducible sin coste). Estado: pendiente de prueba de instalación y consumo de recursos. |
| SO | macOS; versión por registrar | macOS; versión por registrar | Windows virtualizado en Mac; versión por registrar | Por probar en entorno local |
| Cuenta necesaria | No para SQLite local | Depende de la API; preferir endpoint público sin cuenta | Cuenta Microsoft según funciones utilizadas; validar antes de fase | Por determinar según candidata |
| Límites del trial | No aplica a SQLite local | Revisar cuota/límites del endpoint elegido | No asumir trial; confirmar licencia y funciones requeridas | No se ha seleccionado ni validado plataforma SIEM. |
| Alternativa si falla | Otro cliente SQLite gratuito | API pública de demostración o fixture JSON local | Resolver bloqueo de Power BI Desktop; no sustituirlo por otro BI | Wazuh o ELK, sujeto a prueba real. |
| Tiempo real de setup | Por medir | Por medir | Por medir | Por medir |
| Consumo de recursos (RAM/disco) | Por medir | Por medir | Por medir | Por medir |
| Resultado esperado | Abrir DB sintética, ejecutar SELECT/JOIN y exportar resultado | Obtener JSON, validar esquema y generar tabla de calidad | Importar CSV, transformar, modelar y verificar medidas | **Estado: pendiente de prueba de instalación y consumo de recursos.** |
| Estado | Pendiente | Pendiente | Pendiente | Pendiente |

## Registro de prueba

Para cada herramienta registra fecha, versión exacta, sistema operativo, pasos ejecutados, tiempo de instalación, RAM máxima aproximada, espacio en disco, errores y evidencia (captura o log saneado). Usa solo estas etiquetas de estado: **validado / pendiente / bloqueado**.

No cambies una herramienta a “validado” por leer la documentación o porque la instalación parezca posible. Debe abrir, ejecutar el ejercicio mínimo y producir el resultado esperado en el entorno previsto.
