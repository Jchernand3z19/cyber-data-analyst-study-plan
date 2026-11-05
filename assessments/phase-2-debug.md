# Debug — Fase 2

## 1. Conversión sin validar

Una celda vacía rompe float(row['price']). **Solución:** validar presencia y formato, capturar error y enviar a rechazos con motivo y referencia; no convertir a cero.

## 2. Deduplicación destructiva

drop_duplicates elimina observaciones del mismo producto en fechas diferentes. **Solución:** definir clave con producto, tienda y timestamp/ID; separar duplicado exacto de conflicto y conciliar conteos.
