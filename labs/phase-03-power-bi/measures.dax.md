# Medidas DAX de referencia

Crea estas medidas después de importar y relacionar las tablas del laboratorio.

```dax
Observation Count =
COUNTROWS ( FactPriceObservation )

Average Observed Price =
AVERAGE ( FactPriceObservation[Price] )

Minimum Observed Price =
MIN ( FactPriceObservation[Price] )

Maximum Observed Price =
MAX ( FactPriceObservation[Price] )

Products Observed =
DISTINCTCOUNT ( FactPriceObservation[ProductKey] )
```

## Validación manual

Para P-100, los precios del conjunto son 125.50, 119.99 y 123.00 HNL. La media esperada es 122.83 HNL (redondeada a dos decimales), el mínimo 119.99 y el máximo 125.50.

El contexto de filtro cambia los resultados. Filtra por producto, tienda y fecha para comprobar que las medidas responden como esperas. Estas medidas describen observaciones; no representan necesariamente el precio actual.
