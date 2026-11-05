# Ruta de aprendizaje — Security Data Analyst

Programa introductorio de 90 sesiones para desarrollar criterio analítico aplicado al dominio de la seguridad. La prioridad es producir datos interpretables y evidencia reproducible, no operar un SOC.

## Perfil objetivo

El programa está orientado a perfiles híbridos:
- Security Data Analyst
- Junior Security Analyst orientado a datos
- Data Quality Analyst con enfoque en seguridad
- Security Reporting Analyst
- Junior GRC / Data Governance Analyst

## Alcance y no-alcance

Es un programa **INTRODUCTORIO**. No garantiza empleabilidad, no sustituye experiencia real en un SOC y no equivale a una certificación profesional. Tampoco forma administradores de infraestructura ni especialistas de pentesting.

El dato es el objetivo; la seguridad es el dominio de aplicación. Las prácticas usan datos sintéticos, públicos o expresamente autorizados. Cada sesión relacionada con seguridad debe terminar en una evidencia de datos: consulta, tabla, dashboard o informe. No se pide producir reglas operativas, playbooks ni respuestas a incidentes.

## Cómo empezar en 10 minutos

1. Clona el repositorio:
   `git clone https://github.com/Jchernand3z19/security-data-analyst-learning-path.git`
2. Entra en la carpeta:
   `cd security-data-analyst-learning-path`
3. Lee el [Día 0](phases/phase-00-foundations/README.md) y realiza el diagnóstico inicial.
4. Si el diagnóstico indica que ya tienes la base, aplica los umbrales para omitir la Fase 0 o la Fase 1.
5. Abre la [primera sesión](lessons/day-01-http-client-server.md) y registra evidencia solo después de realizar la práctica.

Estos diez minutos sirven para orientarte y abrir el material; las instalaciones se realizan en los puntos indicados abajo y pueden requerir tiempo adicional.

## Semana base

La distribución solicitada suma ocho bloques (4 normales + 1 laboratorio + 1 repaso + 2 libres), por lo que se organiza como un **ciclo de 8 días**, no como una semana de siete días. Los días libres son descanso real.

| Bloque | Tipo | Actividad |
|---|---|---|
| 1 | Normal | Sesión regular |
| 2 | Normal | Sesión regular |
| 3 | Laboratorio — miércoles | Laboratorio práctico; reemplaza la sesión normal, no se suma |
| 4 | Normal | Sesión regular |
| 5 | Normal | Sesión regular |
| 6 | Repaso — sábado | Consolidación y evidencia de datos; reemplaza la sesión normal |
| 7 | Libre — no tocar | Descanso |
| 8 | Libre — no tocar | Descanso |

Los rótulos miércoles y sábado son anclas de tipo de actividad; al aplicar el ciclo de ocho bloques, no se debe forzar que coincidan con una semana calendario. Los laboratorios reemplazan bloques normales, nunca se añaden como carga extra. En Fase 4, máximo dos laboratorios por semana y nunca en días consecutivos.

## Instalación

La instalación se concentra en el primer día de cada etapa que la necesita:
- **Día 0 global:** herramientas base y verificación del entorno.
- **Inicio de Fase 3:** Power BI Desktop y el entorno Windows requerido para utilizarlo.
- **Inicio de Fase 4:** instalación de la plataforma SIEM que se elija, solo después de la prueba de viabilidad.

**Aviso al inicio de cada fase: Día 1 incluye instalación (~1 h extra), el resto no.** Si no hay instalación necesaria, ese tiempo se usa para comprobar versiones y abrir los archivos de práctica. La decisión de SIEM sigue pendiente; consulta [checklist de validación](templates/lab-validation-checklist.md).

## Tiempo realista

Los **90 minutos son el bloque de aprendizaje, no la jornada completa**. La estructura es 10/20/35/15/10 minutos: recuperación, explicación, práctica guiada, ejercicio individual y evidencia/reflexión. Añade **+setup/evidencia si aplica**. El primer día de una fase puede requerir aproximadamente una hora adicional de instalación; no se debe recortar la práctica para aparentar que terminó en 90 minutos.

## Coste total

**Coste total: 0 € en software**, utilizando herramientas gratuitas y alternativas open-source. No se presupuestan licencias de pago ni trials como dependencia del curso. Hardware, electricidad y conexión a internet quedan excluidos. La selección final de SIEM queda abierta entre Wazuh y ELK y no se considera validada hasta probar instalación y consumo de recursos.

## Frase guía

**No formas analistas de SOC. Formas analistas de datos que entienden el dominio de la seguridad.**

## Ruta de las 90 sesiones

| Fase | Días | Enfoque | Guía |
|---|---:|---|---|
| 1 | 1–18 | Redes, HTTP, SQL y fundamentos de seguridad | [Fase 1](phases/phase-01-http-sql/README.md) |
| 2 | 19–36 | Python, APIs y calidad de datos | [Fase 2](phases/phase-02-python-apis/README.md) |
| 3 | 37–52 | Power BI y analítica segura | [Fase 3](phases/phase-03-power-bi/README.md) |
| 4 | 53–70 | Logs y análisis de datos de seguridad | [Fase 4](phases/phase-04-siem-logs/README.md) |
| 5 | 71–90 | Gobierno, privacidad y reporting | [Fase 5](phases/phase-05-governance/README.md) |

## Diagnóstico del programa

- **SIEM:** Splunk Cloud Trial queda descartado como solución única porque no es local ni reproducible sin coste. La herramienta no está decidida. Wazuh (local, open source) y ELK (local, open source) siguen como candidatas; falta prueba real de instalación y consumo de recursos.
- **Power BI:** la fase conserva Power BI como herramienta de aprendizaje. La validación de la instalación y uso se registra en el checklist de laboratorios; no se sustituye por otro BI.
- **Calendario:** la sincronización permanece pausada hasta una revisión humana específica. El repositorio y el material pueden estudiarse sin activar el calendario.

## Navegación

- [Día 0 / Fase 0 opcional](phases/phase-00-foundations/README.md)
- [Test de nivel inicial](templates/initial-level-assessment.md)
- [Plan detallado de las 90 sesiones](curriculum/session-plan.md)
- [Tracker](tracker.md)
- [Rúbrica de evidencias](templates/rubric-template.md)
- [Checklist de validación de laboratorios](templates/lab-validation-checklist.md)
- [Laboratorios](labs/README.md)
- [Guías por fase](phases/)

## Seguridad y uso responsable

Usa datos sintéticos, públicos o autorizados. No subas contraseñas, tokens, claves API, datos personales ni información confidencial. No ejecutes pruebas contra sistemas de terceros. Diferencia los resultados realmente obtenidos de los ejemplos y de las tareas pendientes.
