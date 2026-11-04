# Ruta de aprendizaje — Security Data Analyst

Ruta estructurada de **90 sesiones de aprendizaje**, más preparación inicial para desarrollar competencias de **Security Data Analyst**, con énfasis en análisis de datos, calidad, seguridad, detección y gobierno. **PharmaTracker** funciona como proyecto integrador para aplicar los conceptos a un flujo de datos controlado.

> Este repositorio está orientado a analítica de seguridad y gobierno de datos. No es un curso de pentesting ni una ruta para desarrollar herramientas ofensivas. Las prácticas de seguridad se realizan con datos sintéticos, sistemas propios o recursos expresamente autorizados.

## Objetivos del plan

Al finalizar, deberías poder:

- Interpretar tráfico y respuestas HTTP y consultar datos relacionales de forma segura.
- Crear procesos reproducibles con Python y APIs, aplicando validaciones y controles de calidad.
- Modelar y analizar datos con Power BI, documentando métricas y accesos.
- Analizar logs, construir reglas explicables y comunicar hallazgos sin exagerar la evidencia.
- Documentar gobierno, privacidad, trazabilidad, riesgos y controles de un proyecto de datos.

## Ruta de aprendizaje

| Fase | Días | Enfoque | Guía |
|---|---:|---|---|
| 1 | 1–18 | HTTP, SQL y fundamentos de seguridad | [Abrir fase 1](phases/phase-01-http-sql/README.md) |
| 2 | 19–36 | Python, APIs y calidad de datos | [Abrir fase 2](phases/phase-02-python-apis/README.md) |
| 3 | 37–52 | Power BI y analítica segura | [Abrir fase 3](phases/phase-03-power-bi/README.md) |
| 4 | 53–70 | Logs, detección y fundamentos SIEM | [Abrir fase 4](phases/phase-04-siem-logs/README.md) |
| 5 | 71–90 | Gobierno, privacidad y proyecto final | [Abrir fase 5](phases/phase-05-governance/README.md) |

## Navegación rápida

- [Diseño operativo y preparación](curriculum/README.md) — herramientas, duración y estructura de cada sesión.\n- [Plan detallado de las 90 sesiones](curriculum/session-plan.md) — objetivos, recursos, prácticas y evidencias.\n- [Tracker de las 90 sesiones](tracker.md) — fuente oficial del estado de cada día.
- [Lección del día 1](lessons/day-01-http-client-server.md) — primera sesión desarrollada paso a paso.
- [Registros diarios](daily-logs/README.md) — formato y reglas para guardar evidencia aprobada.
- [Laboratorios y scripts](labs/README.md) — prácticas reproducibles con datos sintéticos.
- [Integración con Google Calendar](integrations/google-calendar/README.md) — configuración y funcionamiento de recordatorios.
- [Workflow de sincronización de calendario](.github/workflows/sync-study-calendar.yml).

## Progreso

**Estado inicial del tracker:** 0 de 90 sesiones aprobadas. Las casillas solo se marcan después de completar la práctica, presentar evidencia y superar la evaluación. El número no se actualiza automáticamente: el tracker es el registro que debe mantenerse manualmente y con evidencia.

| Fase | Sesiones | Estado |
|---|---:|---|
| 1. HTTP, SQL y seguridad | 18 | ⬜ Pendiente |
| 2. Python, APIs y calidad | 18 | ⬜ Pendiente |
| 3. Power BI y analítica segura | 16 | ⬜ Pendiente |
| 4. Logs y SIEM | 18 | ⬜ Pendiente |
| 5. Gobierno y proyecto final | 20 | ⬜ Pendiente |
| **Total** | **90** | **0/90 aprobadas al inicio** |

Actualiza este resumen cuando cambie el estado de las sesiones en [tracker.md](tracker.md). No marques una fase como terminada hasta aprobar su evaluación.

## Rutina de estudio

- **Días:** lunes a sábado.
- **Horario:** 19:00–20:00, hora de Honduras (`America/Tegucigalpa`).
- **Duración:** 60 minutos por sesión.

Distribución sugerida:

1. 10 min — repaso y recuperación de conocimientos previos.
2. 20 min — explicación y estudio del tema.
3. 20 min — práctica guiada o laboratorio.
4. 10 min — evidencia, reflexión y dudas.

Los recordatorios de Google Calendar se crean mediante GitHub Actions. La automatización administra eventos; no marca lecciones como completadas ni evalúa el aprendizaje.

## Método de evaluación

1. Completar la lectura y la práctica indicada.
2. Guardar evidencia reproducible y anotar dudas.
3. Realizar 2–3 preguntas de razonamiento y diagnóstico.
4. Repasar los criterios que no se dominen.
5. Marcar la sesión como aprobada solo cuando exista evidencia y se supere la evaluación.

Si una sesión queda incompleta, se retoma antes de avanzar. No se inventan fechas, resultados ni evidencias.

## Estructura del repositorio

```text
.
├── .github/workflows/       # Automatizaciones de estudio y calendario
├── daily-logs/              # Evidencia de sesiones aprobadas
├── integrations/
│   └── google-calendar/     # Sincronización con Google Calendar
├── labs/                    # Laboratorios reproducibles y datos sintéticos
├── lessons/                 # Lecciones desarrolladas por día\n├── curriculum/              # Diseño operativo y plan detallado de 90 sesiones
├── phases/                  # Guías, prácticas y entregables por fase
└── tracker.md               # Seguimiento oficial de las 90 sesiones
```

## Seguridad y uso responsable

Consulta también la [política y lista de verificación de seguridad](SECURITY.md) antes de añadir archivos o cambiar permisos.

- Utiliza únicamente datos públicos, sintéticos o cuyo uso esté autorizado.
- No subas contraseñas, tokens, claves API, archivos de credenciales ni datos personales o confidenciales.
- No escanees, ataques ni automatices pruebas contra sistemas de terceros sin autorización explícita.
- Distingue siempre entre resultados ejecutados, ejemplos didácticos, hipótesis y trabajo pendiente.
- Revisa los permisos y la información antes de publicar cualquier evidencia.

## Alcance y limitaciones

Este plan es una ruta de aprendizaje y un proyecto de práctica; no equivale a una certificación profesional ni garantiza dominio laboral por completar 90 días. Las herramientas, APIs y controles deben probarse en el entorno correspondiente y documentarse con sus limitaciones.

---

**Regla principal:** aprender, practicar, verificar y documentar. Nunca marcar como completado algo que no se haya realizado.
