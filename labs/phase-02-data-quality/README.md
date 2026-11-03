# Laboratorio — Validación de calidad de datos

**Fase:** 2 — Python, APIs y calidad de datos.

## Objetivo

Leer observaciones sintéticas de precios, validar campos, separar registros aceptados y rechazados y generar un resumen reproducible.

## Requisitos

- Python 3.9 o superior.
- No requiere paquetes externos.

## Ejecución

Desde la raíz del repositorio:

```bash
python3 labs/phase-02-data-quality/validate_prices.py
```

El script lee `sample_prices.csv` y crea `output/valid_rows.csv`, `output/rejected_rows.csv` y `output/quality_report.json`.

## Reglas aplicadas

- Campos obligatorios: product_id, store_id, observed_at, price y currency.
- Fecha en formato ISO 8601 `YYYY-MM-DDTHH:MM:SSZ`.
- Precio numérico mayor que cero.
- Monedas permitidas en este ejemplo: HNL y USD.
- Duplicado según product_id + store_id + observed_at.
- Se conserva el primer registro válido de cada clave; duplicados y filas inválidas se rechazan con motivo.

## Interpretación

Compara filas de entrada, válidas, rechazadas y duplicadas. Una tasa alta de aceptación no garantiza que el origen sea correcto; las reglas son solo las definidas para este ejercicio. Antes de adaptar el script a un proyecto real, acuerda reglas de negocio, zona horaria, moneda y clave de unicidad.

## Evidencia sugerida

Guarda el resumen de ejecución y responde:
1. ¿Qué proporción de registros fue rechazada y por qué?
2. ¿Qué limitaciones tiene la clave usada para detectar duplicados?
3. ¿Qué regla cambiarías si una tienda registra varios precios para el mismo producto en el mismo segundo?
