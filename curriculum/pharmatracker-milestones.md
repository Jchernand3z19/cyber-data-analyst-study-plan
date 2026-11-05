# PharmaTracker — proyecto incremental del curso

## Alcance y límites

PharmaTracker es un caso didáctico de análisis de observaciones de precios de productos farmacéuticos. No es una aplicación clínica ni un sistema de gestión de pacientes. Se trabaja exclusivamente con datos sintéticos o fuentes públicas cuyo uso esté permitido. No se recopilan datos de pacientes, recetas, historiales médicos ni información personal.

El proyecto evoluciona durante las cinco fases. Cada hito reutiliza y amplía los entregables anteriores. Un diseño propuesto no se presenta como una integración implementada.

## Hitos por fase

| Fase | Hito acumulativo | Entregables verificables | Puerta de calidad |
|---|---|---|---|
| 1 — sesiones 1–18 | Definir el flujo y el modelo relacional seguro | Diagrama cliente/API/almacenamiento; glosario HTTP y DNS; esquema SQLite; consultas SELECT/JOIN/agregaciones; matriz de roles y controles | Explicar origen, granularidad, claves, permisos y límites de las conclusiones |
| 2 — sesiones 19–36 | Construir una ingesta reproducible | CSV sintético; script de validación; salidas aceptadas/rechazadas; pruebas; reporte de calidad; registro de linaje | Reproducir desde cero y conciliar conteos de entrada, aceptados, rechazados y duplicados |
| 3 — sesiones 37–52 | Construir analítica verificable y segura | Modelo estrella; Power Query; medidas DAX; conciliación independiente; diseño de informe; matriz de acceso/RLS | Reconciliar al menos tres métricas y demostrar límites de RLS y permisos |
| 4 — sesiones 53–70 | Incorporar observabilidad y análisis de eventos | Dataset sintético de eventos; consultas de búsqueda/filtrado/agregación en una plataforma SIEM seleccionada; regla; falsos positivos; informe de triage | Ejecutar consultas en la plataforma real elegida y distinguir evento, alerta e incidente |
| 5 — sesiones 71–90 | Consolidar gobierno y auditoría | Arquitectura; inventario; clasificación; diccionario; linaje; calidad; acceso; riesgos; retención; informe final y guía de reproducción | Una persona distinta puede seguir la guía, reproducir verificaciones y distinguir controles reales de propuestas |

## Contrato de datos didáctico

- Producto: identificador sintético, nombre genérico de ejemplo, marca ficticia, presentación y categoría.
- Tienda: identificador ficticio, nombre de demostración y ciudad.
- Observación: producto, tienda, instante UTC, precio, moneda, fuente y referencia de origen.
- Evento de seguridad: timestamp UTC, tipo, alias ficticio, etiqueta de origen, resultado, severidad e identificador de solicitud.

La observación de precio es histórica. El precio actual, si se calcula, debe derivarse mediante una regla explícita y documentada; no se sobrescribirá el historial.

## Registro de estado

Para cada entregable, registrar: estado (pendiente/en diseño/implementado/verificado), fecha, evidencia, limitaciones y responsable. No declarar una fuente conectada, un control desplegado ni una prueba ejecutada sin evidencia.
