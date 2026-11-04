# Auditoría del programa — Security Data Analyst

**Estado:** auditoría inicial en curso  
**Alcance:** estructura técnica, coherencia pedagógica, materiales, laboratorios y automatizaciones.  
**Regla:** no sincronizar el currículo con Google Calendar hasta cerrar las auditorías y validar las correcciones.

## Hallazgos iniciales

| ID | Área | Hallazgo | Prioridad | Acción requerida |
|---|---|---|---|---|
| AUD-001 | Coherencia operativa | El programa establece 90 minutos, pero `lessons/TEMPLATE.md` conserva una estructura de 60 minutos. | Alta | Alinear plantilla, lecciones y evaluaciones a 90 minutos. |
| AUD-002 | Automatización | `.github/workflows/study-reminder.yml` conserva el horario anterior de 19:00 Honduras y textos de 60 minutos. | Alta | Actualizar o rediseñar el recordatorio para 08:00–09:30; verificar también su lógica y frecuencia. |
| AUD-003 | SIEM | La fase 4 practica detección principalmente con Python y CSV. No hay todavía una práctica guiada suficiente con una plataforma SIEM y su lenguaje de consulta. | Alta | Elegir una plataforma viable y añadir ingestión, consultas, detección, investigación y evidencia reproducible. |
| AUD-004 | Fundamentos de seguridad | La progresión cubre HTTP y controles de datos, pero necesita revisar la cobertura de redes, identidad y acceso, arquitectura básica y fuentes de telemetría. | Alta | Añadir los fundamentos estrictamente necesarios para interpretar datos de seguridad, sin convertir la ruta en pentesting o administración avanzada. |
| AUD-005 | Proyecto integrador | PharmaTracker aparece como ejemplo en fases tempranas, pero el trabajo formal de arquitectura y gobierno se concentra al final. | Media | Definir entregables incrementales por fase y mantener una arquitectura acumulativa. |
| AUD-006 | Evaluación | El plan define evidencia y preguntas, pero no existe todavía una rúbrica uniforme con criterios, umbral de aprobación, recuperación y evaluación práctica. | Alta | Diseñar rúbricas observables y evaluaciones acumulativas por fase. |
| AUD-007 | Power BI | El plan contempla Power BI Desktop y el usuario utilizará un entorno/emulador Windows en Mac. | Media | Mantener Power BI Desktop y validar antes de la fase 3 rendimiento, compatibilidad, archivos, conectividad y acceso al entorno. |
| AUD-008 | Consistencia documental | README y tracker contienen secuencias literales de caracteres `\\n` en algunos párrafos/listados; hay formato que requiere limpieza. | Media | Corregir formato y validar enlaces internos y rutas. |
| AUD-009 | Diseño de sesiones | Las 90 sesiones tienen objetivos, recursos, práctica y evidencia, pero la carga real de cada actividad no está demostrada en todas las sesiones. | Alta | Estimar y probar el tiempo de las prácticas; dividir o simplificar cuando no quepan en 90 minutos. |
| AUD-010 | Recursos | Los enlaces y referencias están seleccionados, pero falta verificar vigencia, pertinencia exacta y accesibilidad de cada recurso. | Media | Validar recursos por sesión y sustituir enlaces genéricos o desactualizados. |

## Criterios de cierre

1. Cada sesión tiene objetivo observable, prerrequisitos, explicación, práctica reproducible, evidencia y evaluación.
2. La secuencia desarrolla competencias progresivas propias de analítica de seguridad.
3. Los laboratorios se ejecutan desde cero en el entorno previsto y producen resultados comprobables.
4. Las herramientas elegidas son accesibles y sus limitaciones están documentadas.
5. PharmaTracker integra las competencias sin afirmar que funcionalidades propuestas ya están implementadas.
6. Horarios, duración, tracker, plantillas y automatizaciones no se contradicen.
7. Se revisan enlaces, rutas, formato, seguridad y consistencia del repositorio.
8. Google Calendar permanece sin cambios hasta la aprobación final del currículo.

## Orden de trabajo

1. Auditoría técnica de scripts, laboratorios, workflows y estructura.
2. Auditoría pedagógica de prerrequisitos, secuencia, profundidad y carga horaria.
3. Diseño de competencias y rúbricas de evaluación.
4. Corrección de las 90 sesiones y materiales relacionados.
5. Pruebas de ejecución, enlaces y coherencia documental.
6. Aprobación final del plan; después, preparar la sincronización del calendario.

## Límites de esta revisión inicial

Los hallazgos anteriores son una revisión estática de los documentos consultados. No certifican que todos los scripts, enlaces, workflows o entornos hayan sido ejecutados y probados. Cada prueba pendiente debe registrarse como tal.
