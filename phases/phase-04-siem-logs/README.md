# Fase 4 — Logs y análisis de datos de seguridad

> **Aviso de fase:** Día 1 incluye instalación (~1 h extra), el resto no. Si no se requiere instalar una herramienta en esta fase, utiliza ese tiempo para verificar versiones y abrir los archivos de práctica.


## Objetivo

Analizar datos sintéticos de eventos para producir consultas, tablas agregadas, métricas de calidad e informes reproducibles. El dato es el objetivo; la seguridad es el dominio de aplicación.

## Secuencia de estudio

| Días | Tema | Evidencia de datos |
|---|---|---|
| 53–56 | Estructura, tiempo, calidad y categorías de eventos | Diccionario, perfilado y tablas de calidad |
| 57–60 | Filtrado, agregación y análisis temporal | Consultas y tablas por tipo, resultado e intervalo |
| 61–65 | Comparación de patrones, contexto y criterios de riesgo | Matrices de conteos, métricas e informe |
| 66–70 | Cobertura, retención, minimización y síntesis | Tablas analíticas y reporte ejecutivo |

## Plataforma SIEM: decisión pendiente

Splunk Cloud Trial queda descartado como solución única porque no es local ni reproducible sin coste. La herramienta SIEM **no está decidida**. Las candidatas son **Wazuh (local, open source)** y **ELK (local, open source)**. La decisión queda pendiente de una prueba real de instalación y consumo de recursos; consulta el [checklist de validación](../../templates/lab-validation-checklist.md).

No se activa una cuenta trial ni se declara compatible una plataforma antes de probarla. Mientras la decisión está pendiente, se pueden estudiar los datasets y scripts locales de esta fase sin afirmar que se ha utilizado un SIEM.

## Laboratorios y datos

- [Laboratorio de análisis de logs](../../labs/phase-04-log-analysis/README.md): eventos sintéticos y análisis reproducible con Python.
- [Checklist de validación](../../templates/lab-validation-checklist.md): registro de versión, SO, setup, RAM, disco y resultado mínimo.

## Esquema sintético de eventos

Campos sugeridos:
`timestamp_utc, event_type, user_alias, source_label, outcome, severity, request_id`.

Los alias y etiquetas son ficticios. No recolectes registros de cuentas o sistemas ajenos.

## Prácticas de análisis

1. Perfila el dataset: filas, campos, nulos, duplicados y timestamps inválidos.
2. Normaliza fechas a UTC y conserva conteos de registros válidos e inválidos.
3. Resume eventos por tipo, resultado, alias ficticio y periodo.
4. Compara grupos temporales y documenta umbrales analíticos como parámetros, no como controles operativos.
5. Cuantifica falsos positivos potenciales y límites del conjunto de datos.
6. Analiza volumen, antigüedad y campos sensibles para producir tablas de calidad y minimización.
7. Presenta hallazgos con cobertura, incertidumbre y limitaciones.

## Evidencias esperadas

- Dataset sintético documentado.
- Consultas reproducibles y tablas agregadas.
- Reporte de calidad de eventos y análisis temporal.
- Tabla de cobertura, falsos positivos potenciales y limitaciones.
- Informe breve de hallazgos basado en evidencia.

La evidencia de cada sesión es un producto de datos (consulta, tabla, dashboard o informe), no una regla operativa, playbook ni respuesta a incidentes.
