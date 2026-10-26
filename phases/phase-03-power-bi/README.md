# Fase 3 — Power BI y analítica segura

## Objetivo

Construir un modelo analítico comprensible y verificable para PharmaTracker, con métricas reconciliadas y controles que reduzcan la exposición de información.

## Secuencia de estudio

| Días | Tema | Evidencia mínima |
|---|---|---|
| 37–39 | Granularidad, modelo dimensional, relaciones y Power Query | Diagrama de modelo y pasos de transformación |
| 40–44 | DAX, contexto de filtro, métricas y navegación | Medidas verificadas con cálculos independientes |
| 45–49 | RLS, privilegio mínimo, clasificación, anonimización y exportación | Matriz de acceso y revisión de riesgos |
| 50–52 | Definiciones, accesibilidad y evaluación | Diccionario de métricas y reporte final |

## Modelo sugerido

Trabaja con datos sintéticos:
- **DimProduct:** ProductKey, Brand, ProductName, Presentation.
- **DimStore:** StoreKey, StoreName, City.
- **DimDate:** DateKey, Date.
- **FactPriceObservation:** ProductKey, StoreKey, DateKey, Price, Currency, SourceRecordId.

Define explícitamente la granularidad de FactPriceObservation: una observación de precio por producto, tienda y momento de captura. No mezcles en una misma fila el precio actual y todo el historial sin una regla clara.

## Prácticas

1. Importa datos sintéticos con Power Query y registra los pasos de limpieza.
2. Verifica tipos, claves, duplicados y filas rechazadas.
3. Construye relaciones uno-a-muchos cuando la clave del lado dimensión sea única.
4. Crea medidas de precio mínimo, máximo y promedio; define qué hacer cuando hay monedas distintas.
5. Calcula la variación entre observaciones comparables, sin confundir cambio real con cambio de presentación o moneda.
6. Reconcilia las medidas con cálculos independientes sobre una muestra pequeña.
7. Diseña filtros por fecha, ciudad, tienda, marca y presentación.
8. Documenta qué visuales pueden revelar datos innecesarios.

## Seguridad y gobierno

- RLS filtra filas para roles definidos, pero no sustituye la administración de permisos del workspace, modelo y exportación.
- Prueba cada rol con una cuenta o mecanismo de prueba autorizado; no des por hecho que una regla DAX funciona por su apariencia.
- Minimiza columnas y oculta campos técnicos cuando no aporten al análisis, sin confundir ocultar con proteger.
- Evita publicar informes con datos sensibles o enlaces de acceso amplio.
- Documenta definiciones, propietario, fuente, frecuencia de actualización y limitaciones de cada indicador.

## Entregables

- Diagrama del modelo y definición de granularidad.
- Consultas de Power Query documentadas.
- Medidas DAX con resultado esperado sobre un ejemplo pequeño.
- Diccionario de métricas y reglas de conciliación.
- Matriz de permisos y riesgos de exportación.
- Capturas o archivos de evidencia sin datos sensibles.

## Criterios de aprobación

Debes explicar relaciones y contexto de filtro, reconciliar las métricas, demostrar qué acceso concede cada rol y señalar límites de RLS. No se considera segura una solución solo porque un campo esté oculto o un informe se vea correcto.
