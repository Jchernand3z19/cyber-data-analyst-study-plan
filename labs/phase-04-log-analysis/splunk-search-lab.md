# Laboratorio SIEM — Splunk Cloud y consultas SPL

## Antes de empezar

Activa la prueba de Splunk Cloud únicamente al iniciar la fase 4. Confirma en la página de registro las condiciones, duración y límites vigentes. Usa exclusivamente el archivo sintético sample_auth_events.csv. No cargues logs personales, laborales ni de terceros.

Sigue el tutorial oficial para importar un CSV y abrir Search & Reporting. Define el sourcetype para reconocer los campos CSV. Como el campo de tiempo del archivo se llama timestamp_utc, no asumas que Splunk lo convertirá automáticamente en _time. En las búsquedas temporales usa el rango All time y convierte explícitamente el campo con strptime. Sustituye index y sourcetype por los valores configurados en tu instancia.

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
| eval _time=strptime(timestamp_utc, "%Y-%m-%dT%H:%M:%SZ")
| where isnotnull(_time)
| dedup request_id
| sort 0 _time
| streamstats time_window=10m count AS failures_10m BY user_alias
| where failures_10m >= 5
```

Compara los resultados con analyze_auth_logs.py. Documenta diferencias por orden temporal, límites de ventana, duplicados, selección del rango de tiempo y eventos rechazados. La fila con timestamp inválido se excluye con isnotnull(_time); la segunda fila con request_id repetido se elimina con dedup. No asumas que dos implementaciones son equivalentes solo porque usan el mismo umbral.

## Evidencia requerida

- Captura saneada de la carga de CSV y campos detectados.
- Tres consultas ejecutadas y sus resultados.
- Consulta temporal ejecutada, resultado y comparación con Python.
- Nota sobre rango temporal, falsos positivos y falsos negativos.
- Conclusión que separe evento, alerta e incidente.

## Criterio de aprobación

Otra persona debe poder repetir la ingesta y las consultas con el mismo CSV, obtener resultados compatibles y entender las limitaciones. Si la prueba cloud expiró antes de terminar, registra la limitación; no simules que se ejecutó la consulta.
