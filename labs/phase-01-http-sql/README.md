# Laboratorio — SQL seguro con SQLite

**Fase:** 1 — HTTP, SQL y fundamentos de seguridad.

## Objetivo

Practicar SELECT, filtros, JOIN, agregaciones y consultas parametrizadas con una base SQLite creada en memoria. No se conecta a ningún sistema externo.

## Ejecución

```bash
python3 labs/phase-01-http-sql/sql_basics.py
```

No requiere dependencias externas ni crea una base de datos persistente.

## Actividades

1. Revisa la estructura y los datos sintéticos del script.
2. Ejecuta cada consulta e interpreta el resultado.
3. Compara la consulta parametrizada con una consulta que concatena texto; explica el riesgo sin ejecutar cargas contra sistemas reales.
4. Modifica filtros y agrupaciones y registra el resultado esperado y observado.

## Evidencia

Entrega una explicación de SELECT, JOIN, GROUP BY y parámetros; incluye el resultado de cada consulta y una nota sobre el principio de mínimo privilegio.

Este laboratorio enseña SQL básico; no constituye una prueba completa de seguridad de bases de datos.
