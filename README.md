# Ruta de aprendizaje — Security Data Analyst

Programa introductorio de 90 sesiones para desarrollar criterio analítico aplicado al dominio de la seguridad. La prioridad es producir datos interpretables y evidencia reproducible, no operar un SOC.

## Perfil objetivo

- Security Data Analyst
- Junior Security Analyst orientado a datos
- Data Quality Analyst con enfoque en seguridad
- Security Reporting Analyst
- Junior GRC / Data Governance Analyst

## Alcance y no-alcance

Es un programa **INTRODUCTORIO**. No garantiza empleabilidad, no sustituye experiencia real en un SOC y no equivale a una certificación profesional. Tampoco forma administradores de infraestructura ni especialistas de pentesting.

El dato es el objetivo; la seguridad es el dominio de aplicación. Las prácticas usan datos sintéticos, públicos o expresamente autorizados. Cada sesión relacionada con seguridad debe terminar en una evidencia de datos: consulta, tabla, dashboard o informe. No se pide producir reglas operativas, playbooks ni respuestas a incidentes.

## Estado del trabajo

**Sprint 1: CERRADO Y APROBADO. Sprint 2: CERRADO — documentación y evaluación actualizadas; Wazuh 4.9.0 validado físicamente con ingesta real de un log SSH sintético. Sprint 3: NO INICIADO.**

### Decisión SIEM de Fase 4

- **Wazuh 4.9.0 Single-node:** seleccionado y validado en Docker Desktop sobre macOS Apple Silicon.
- Docker Desktop: 11.72 GiB asignados.
- Consumo aproximado: 2.9 GB (Indexer 1.66 GB, Manager 911 MB, Dashboard 382 MB); CPU inferior al 4%.
- Prueba: log sintético de fallo SSH; regla 5710, nivel 5; mapeo MITRE ATT&CK T1110.001 — Password Guessing.
- **ELK:** pendiente / descartado por recursos para este entorno y alcance. No se realizó benchmark equivalente, por lo que no se atribuye un consumo medido a ELK.
- Tiempo exacto de instalación Wazuh: no registrado.

Consulta el [checklist de validación](templates/lab-validation-checklist.md) y la [guía de Fase 4](phases/phase-04-siem-logs/README.md).

## Navegación

- [Plan detallado de las 90 sesiones](curriculum/session-plan.md)
- [Tracker](tracker.md)
- [Rúbrica de evidencias](templates/rubric-template.md)
- [Evaluaciones por fase](assessments/README.md)
- [Checklist de validación de laboratorios](templates/lab-validation-checklist.md)
- [Laboratorios](labs/README.md)
- [Guías por fase](phases/)

## Seguridad y uso responsable

Usa datos sintéticos, públicos o autorizados. No subas contraseñas, tokens, claves API, datos personales ni información confidencial. No ejecutes pruebas contra sistemas de terceros. Diferencia los resultados realmente obtenidos de los ejemplos y de las tareas pendientes.

**No formas analistas de SOC. Formas analistas de datos que entienden el dominio de la seguridad.**