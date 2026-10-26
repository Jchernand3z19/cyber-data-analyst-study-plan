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

Puedes reproducir la regla, explicar el umbral, mostrar al menos un positivo y un negativo, describir falsos positivos y separar observación de hipótesis. La evaluación no premia alertas dramáticas; premia conclusiones proporcionadas a la evidencia.
