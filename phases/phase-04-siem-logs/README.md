# Fase 4 — Logs, detección y fundamentos SIEM

## Objetivo

Analizar eventos sintéticos, identificar patrones explicables, priorizar señales, controlar falsos positivos y redactar hallazgos con evidencia reproducible.

## Secuencia de estudio

| Días | Tema | Evidencia mínima |
|---|---|---|
| 53–56 | Estructura de logs, tiempo, severidad, eventos/alertas/incidentes | Diccionario de campos |
| 57–60 | Fallos de autenticación, entradas sospechosas y anomalías | Reglas sencillas sobre datos sintéticos |
| 61–65 | Falsos positivos, enriquecimiento, correlación y priorización | Tabla de pruebas y razonamiento de riesgo |
| 66–70 | Triage, conservación, minimización e investigación integrada | Informe de caso |

## Plataforma recomendada: Splunk Cloud Platform Trial

El laboratorio Python es una preparación reproducible, no experiencia SIEM. Se propone Splunk Cloud Platform Trial para evitar una instalación local. La guía oficial indica una prueba Cloud de duración limitada (15 días y hasta 5 GB/día en la documentación consultada); crea la cuenta y activa la prueba únicamente al comenzar esta fase. Verifica las condiciones vigentes antes de registrarte. La alternativa Splunk Enterprise Trial dura 60 días, pero requiere instalar software en Windows o Linux; no se asume compatible con macOS ARM ni con Windows ARM emulado.

Recursos: [requisitos del tutorial y duración de pruebas](https://help.splunk.com/en/splunk-enterprise/search/search-tutorial/10.6/part-1-getting-started/what-you-need-for-this-tutorial), [referencia SPL](https://help.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.4/introduction/welcome-to-the-search-reference).

Para aprobar, carga solo el CSV sintético de este repositorio, ejecuta búsquedas, filtros, agregaciones y una regla temporal en la instancia y guarda evidencia saneada.

## Laboratorio SPL

Usa el [guion de consultas Splunk](../../labs/phase-04-log-analysis/splunk-search-lab.md) después de cargar el CSV sintético en la instancia de prueba. Las consultas son plantillas didácticas: ajusta index y sourcetype a los nombres que realmente hayas configurado.

## Laboratorio ejecutable

Complementa esta guía con el [laboratorio de análisis de logs](../../labs/phase-04-log-analysis/README.md), que incluye eventos sintéticos y un script Python para aplicar una regla de detección didáctica.

## Esquema sintético de eventos

Usa campos como:
`timestamp_utc, event_type, user_alias, source_label, outcome, severity, request_id`.

Los alias y etiquetas deben ser ficticios. No recolectes logs de cuentas o sistemas ajenos.

## Laboratorio

Crea eventos ficticios que incluyan:
- autenticaciones exitosas y fallidas;
- varias fallas cercanas en el tiempo para un mismo alias;
- eventos normales que permitan medir falsos positivos;
- una marca temporal malformada;
- una entrada duplicada.

Define una regla explicable, por ejemplo: alertar cuando haya al menos cinco fallos de autenticación para un alias dentro de una ventana de diez minutos. Esta regla es didáctica, no un estándar universal. Registra la ventana, el umbral, los casos detectados y los falsos positivos.

Después:
1. Normaliza marcas temporales a UTC y conserva el dato original sintético cuando sea necesario.
2. Ordena eventos por tiempo y correlaciona solo mediante identificadores disponibles.
3. Separa evento, alerta e incidente.
4. Prioriza por impacto potencial, probabilidad y calidad de evidencia.
5. Escribe un resumen con qué pasó, alcance conocido, evidencia, incertidumbre y siguiente paso.
6. Evita afirmar que una cuenta fue comprometida solo por ver varios fallos.

## Seguridad de logs

Nunca registres contraseñas, tokens de sesión, claves API ni cuerpos completos si contienen datos personales. Aplica minimización, control de acceso y retención definida. Los logs también son datos que requieren protección.

## Entregables

- Dataset de eventos sintéticos.
- Regla de detección documentada y probada con casos positivos y negativos.
- Tabla de falsos positivos y limitaciones.
- Informe de triage con evidencia y nivel de confianza.
- Nota de minimización y retención de los datos.

## Criterios de aprobación

Puedes reproducir la regla Python, explicar el umbral, mostrar al menos un positivo y un negativo, describir falsos positivos y separar observación de hipótesis. Además, debes demostrar consultas nativas en la plataforma SIEM elegida y adjuntar evidencia saneada de búsqueda y agregación. La evaluación no premia alertas dramáticas; premia conclusiones proporcionadas a la evidencia.
