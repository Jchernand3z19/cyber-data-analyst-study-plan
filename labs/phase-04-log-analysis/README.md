# Laboratorio — Análisis básico de logs

**Fase:** 4 — Logs, detección y fundamentos SIEM.

## Objetivo

Normalizar y analizar eventos ficticios para identificar posibles patrones de autenticación fallida. La regla es didáctica y no demuestra por sí sola un compromiso.

## Ejecución

Desde la raíz del repositorio:

```bash
python3 labs/phase-04-log-analysis/analyze_auth_logs.py
```

El script lee `sample_auth_events.csv` y genera `output/alerts.csv` y `output/analysis_report.json`.

## Regla didáctica

Genera una alerta cuando un alias acumula al menos cinco fallos dentro de una ventana móvil de diez minutos. Los eventos con fecha inválida se reportan como rechazados; los duplicados exactos se ignoran para no contar dos veces la misma evidencia.

## Preguntas

1. ¿Por qué una alerta no equivale a un incidente confirmado?
2. ¿Qué falsos positivos puede generar esta regla?
3. ¿Qué contexto adicional necesitarías antes de escalar el hallazgo?
4. ¿Qué información sensible no debe incluirse en un log?
