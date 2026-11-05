# Laboratorio SIEM — Splunk Cloud y consultas SPL

## Antes de empezar

Activa la prueba de Splunk Cloud únicamente al iniciar la fase 4. Confirma en la página de registro las condiciones, duración y límites vigentes. Usa exclusivamente el archivo sintético sample_auth_events.csv. No cargues logs personales, laborales ni de terceros.

Sigue el tutorial oficial para importar un CSV y abrir Search & Reporting. Define el sourcetype de forma que Splunk reconozca los campos CSV. En los ejemplos siguientes sustituye index y sourcetype por los valores configurados en tu instancia.

## Consultas iniciales

Búsqueda de autenticaciones fallidas:

```spl
index=main sourcetype=auth_events event_type=authentication outcome=failure
```

Conteo por alias:

```spl
index=main sourcetype=auth_events event_type=authentication outcome=failure
| stats count AS failures BY user_alias
| sort - failures
```

Conteo por tipo y resultado:

```spl
index=main sourcetype=auth_events
| stats count BY event_type outcome
```

## Detección temporal

Prueba una ventana móvil de diez minutos, agrupada por alias:

```spl
index=main sourcetype=auth_events event_type=authentication outcome=failure
| sort 0 _time
| streamstats time_window=10m count AS failures_10m BY user_alias
| where failures_10m >= 5
```

Compara los resultados con analyze_auth_logs.py. Documenta diferencias por orden temporal, límites de ventana, duplicados, selección del rango de tiempo y eventos rechazados. No asumas que dos implementaciones son equivalentes solo porque usan el mismo umbral.

## Evidencia requerida

- Captura saneada de la carga de CSV y campos detectados.
- Tres consultas ejecutadas y sus resultados.
- Consulta temporal ejecutada, resultado y comparación con Python.
- Nota sobre rango temporal, falsos positivos y falsos negativos.
- Conclusión que separe evento, alerta e incidente.

## Criterio de aprobación

Otra persona debe poder repetir la ingesta y las consultas con el mismo CSV, obtener resultados compatibles y entender las limitaciones. Si la prueba cloud expiró antes de terminar, registra la limitación; no simules que se ejecutó la consulta.
