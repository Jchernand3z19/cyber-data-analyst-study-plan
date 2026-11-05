# Fase 4 — Logs y análisis de datos de seguridad

> **Aviso de fase:** Día 1 incluye instalación (~1 h extra), el resto no. Wazuh 4.9.0 ya quedó instalado y validado en el entorno de laboratorio; las sesiones posteriores no requieren repetir la instalación.

## Objetivo

Analizar datos sintéticos de eventos para producir consultas, tablas agregadas, métricas de calidad e informes reproducibles. El dato es el objetivo; la seguridad es el dominio de aplicación.

## Plataforma SIEM validada

**Wazuh 4.9.0 Single-node** queda seleccionado para el laboratorio. Entorno: Docker Desktop en macOS Apple Silicon, con 11.72 GiB asignados. Consumo observado aproximado: 2.9 GB (Indexer 1.66 GB, Manager 911 MB, Dashboard 382 MB); CPU inferior al 4%. La ingesta de un log sintético de fallo SSH fue exitosa: regla 5710, nivel 5, mapeo MITRE ATT&CK T1110.001 — Password Guessing.

ELK queda **pendiente / descartado por recursos** para este entorno y alcance; no se ejecutó una prueba comparable y no debe afirmarse que su consumo fue medido. El tiempo exacto de instalación de Wazuh no fue registrado.

Consulta el [checklist de validación](../../templates/lab-validation-checklist.md).

## Secuencia de estudio y evidencias

| Sesiones | Tema | Evidencia |
|---|---|---|
| 53–54 | ATT&CK aplicado al evento SSH real de laboratorio | Mapeo log → Credential Access → T1110.001, con regla 5710, nivel 5, confianza y datos faltantes |
| 55–56 | Wazuh como fuente de datos; consultas sobre la alerta | Captura saneada, consultas por `rule.id`, `srcip`, `srcuser` y `rule.mitre.id`; tabla agregada |
| 57–58 | Calidad y dashboard de reporting | Métricas de completitud, nulos, duplicados y visualización de volumen/regla/origen/usuario/técnica |
| 69 | Triage documental | Ticket sintético; separación de observación, hipótesis y datos faltantes; sin respuesta activa |

## Consultas de referencia

En el explorador de eventos del dashboard, utiliza filtros sobre los campos que el laboratorio confirmó como disponibles:

```text
rule.id:5710
rule.mitre.id:T1110.001
```

Después revisa y agrupa por `srcip` y `srcuser`. Comprueba los nombres y valores reales del documento antes de construir visualizaciones; no supongas que todos los eventos contienen todos los campos.

- [Laboratorio ATT&CK](../../labs/phase-04-log-analysis/attack-context.md)
- [Plantilla de ticket de triage](../../labs/phase-04-log-analysis/triage-data-template.md)
- [Quiz Fase 4](../../assessments/phase-4-quiz.md) · [Debug Fase 4](../../assessments/phase-4-debug.md)
- [Laboratorio de análisis de logs](../../labs/phase-04-log-analysis/README.md)

## Límite analítico

Una alerta de regla 5710 con mapeo T1110.001 documenta cómo Wazuh clasificó el evento observado. No demuestra por sí sola un acceso exitoso, una intrusión ni la identidad de una persona. Las evidencias curriculares son consultas, tablas, dashboard e informes; no reglas operativas, playbooks ni respuesta a incidentes.