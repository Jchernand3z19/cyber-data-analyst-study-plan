# Auditoría de las 90 sesiones

**Estado:** auditoría estructural y documental completada; faltan pruebas ejecutadas en el entorno del estudiante y verificación de enlaces externos.  
**Calendario:** pausado. No sincronizar ni programar sesiones hasta cerrar las puertas de preparación y las decisiones técnicas.

## Resultado de revisión estructural

Se revisaron los objetivos, recursos, prácticas y evidencias del plan de sesiones 1–90, las cinco guías de fase, los cuatro README de laboratorios, los scripts y datasets disponibles, el tracker y la guía operativa.

| Bloque | Resultado | Observación / acción |
|---|---|---|
| 1–7 HTTP/web | Requiere ajuste | Incorporar DNS, red y lectura de identidad/autorización; se reordenan las sesiones iniciales |
| 8–18 SQL/seguridad | Adecuado con refuerzo | Buen recorrido SQL; concretar permisos como diseño conceptual en SQLite y no afirmar que SQLite demuestra administración empresarial de roles |
| 19–36 Python/API/calidad | Adecuado con mejoras | Secuencia coherente; mejorar pruebas automatizadas y trazabilidad de rechazos |
| 37–52 Power BI | Condicionado | Modelo y seguridad pertinentes; ejecución real depende de validar Windows virtualizado, Power BI Desktop y licencia |
| 53–70 Logs/SIEM | En diseño, falta validar acceso | Se propone Splunk Cloud Trial y ya se incorporó una guía de SPL; la instancia y consultas aún no se han ejecutado |
| 71–90 Gobierno/proyecto | Adecuado con mejoras | El cierre cubre gobierno y riesgo, pero faltaba una progresión explícita del proyecto; se añade roadmap acumulativo |

## Hallazgos técnicos de laboratorios

- sql_basics.py: usa SQLite en memoria, datos ficticios y parámetros enlazados. Enseña consultas básicas; no simula roles/grants de un motor empresarial. La guía debe dejar claro ese límite.
- validate_prices.py: separa válidos/rechazados y reporta motivos. La clave de duplicidad es producto+tienda+timestamp; es una decisión didáctica, no una clave universal. La fecha se valida en formato UTC literal; no cubre todos los formatos ISO 8601 ni zonas horarias.
- analyze_auth_logs.py: regla de cinco fallos en diez minutos por alias. Deduplica por request_id, no por igualdad completa de fila; los identificadores repetidos se rechazan. Genera una alerta por alias y no conserva una matriz de falsos positivos/negativos. La práctica debe discutir esas limitaciones.
- Laboratorio Power BI: el conjunto usa HNL y facilita conciliación; el ejemplo DAX contiene P-100 con media 122.83, mínimo 119.99 y máximo 125.50. Falta ejecutar el PBIX en Power BI Desktop; los CSV por sí solos no prueban compatibilidad ni RLS.
- No se declara que los scripts hayan sido ejecutados en un entorno de pruebas durante esta auditoría. La revisión de código es estática.

## Correcciones curriculares registradas

- Distribución de 90 minutos del Día 1 corregida.
- Preparación P3 exige prueba de instalación/ejecución de Power BI Desktop en Windows virtualizado.
- Se añade roadmap acumulativo de PharmaTracker.
- Se añade rúbrica común y recuperación.
- Se refuerza en la Fase 1 el contexto DNS/red e identidad/autorización.
- Se propone Splunk Cloud Trial para evitar instalación local y se incorpora laboratorio con consultas SPL; falta validar la instancia al iniciar la fase 4.

## Pendientes que impiden aprobar y activar el calendario

1. Activar y validar Splunk Cloud Trial al iniciar la fase 4 (prueba temporal); ejecutar y guardar evidencia de las consultas SPL del laboratorio.
2. Completar P3: verificar Windows virtualizado y Power BI Desktop real en el Mac; documentar rendimiento y licencia.
3. Ejecutar los cuatro laboratorios desde cero y registrar salidas; verificar que los resultados esperados coinciden con los datasets.
4. Completar comprobación de enlaces externos y revisar permisos/visibilidad del repositorio antes de publicar datos de práctica.
5. El workflow de Calendar y su script se revisaron estáticamente; el script opera en dry-run por defecto y exige confirmación explícita para borrar series heredadas o crear eventos. No ejecutar sincronización hasta aprobación final.
6. Tras las pruebas locales y la verificación de enlaces, cerrar el dictamen y pedir autorización explícita antes de reactivar el calendario.

## Dictamen

**No aprobado todavía para calendario.** La estructura general de 90 sesiones es aprovechable y no requiere aumentar duración por defecto. Las dependencias críticas son la validación de Power BI, la prueba real de Splunk y la ejecución de los laboratorios. La sincronización de calendario tiene ahora protección de dry-run por defecto. Mantener todas las sesiones pendientes hasta que el estudiante complete sus prácticas.
