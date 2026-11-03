# Laboratorio — Modelo analítico para Power BI

**Fase:** 3 — Power BI y analítica segura.

## Objetivo

Crear un modelo estrella sencillo en Power BI usando archivos CSV sintéticos, definir medidas DAX y comprobar los resultados con cálculos independientes.

## Archivos

- [Productos](sample_products.csv)
- [Tiendas](sample_stores.csv)
- [Observaciones de precio](sample_price_observations.csv)
- [Referencia de medidas DAX](measures.dax.md)

## Preparación

1. En Power BI Desktop, importa los tres CSV.
2. Verifica tipos de datos y claves en Power Query.
3. Crea la relación DimProduct[ProductKey] 1:* FactPriceObservation[ProductKey].
4. Crea la relación DimStore[StoreKey] 1:* FactPriceObservation[StoreKey].
5. Crea una tabla calendario en Power BI y relaciónala con Date.
6. Comprueba que no existan claves duplicadas en las dimensiones ni observaciones sin correspondencia.

## Precauciones

El ejemplo usa una sola moneda (HNL) para que las medidas sean comparables. No mezcles monedas sin una regla explícita de conversión y fecha de tipo de cambio. La tabla contiene observaciones, no una tabla de precios actuales: cualquier indicador de precio debe respetar la fecha y granularidad.

## Evidencia

Documenta el diagrama del modelo, tipos de datos, medidas, una conciliación manual de al menos tres filas y una captura del informe con datos ficticios. No publiques archivos con información real o sensible.
