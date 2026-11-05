# Mantenimiento del repositorio

**Última revisión de esta guía:** 2026-11-05  
**Frecuencia:** revisión trimestral de enlaces y dependencias; revisión semestral de herramientas de laboratorio.

## Calendario recomendado

| Elemento | Frecuencia | Qué revisar |
|---|---|---|
| Wazuh | Cada 6 meses y antes de reconstruir el laboratorio | Versiones soportadas, avisos de seguridad, compatibilidad Docker/arquitectura, interfaz y campos. La guía usa Wazuh 4.9.0: no actualizar sin probar la nueva versión. |
| Docker Desktop / Engine | Cada 6 meses | Compatibilidad macOS/Windows/Linux, arquitectura, consumo, requisitos y condiciones de licencia. |
| Python y librerías | Trimestral | Versiones soportadas, dependencias obsoletas, vulnerabilidades y reproducibilidad. |
| Power BI Desktop / servicio | Cada 6 meses | Windows virtualizado, funciones DAX/Power Query, licencia, RLS y compartición. |
| MITRE ATT&CK | Cada 6 meses | Cambios de técnicas, subtécnicas, identificadores y descripciones; conservar la versión consultada. |
| Enlaces externos | Trimestral | URL rota, redirecciones, contenido movido y cambios de documentación. |
| GitHub Actions | Trimestral | Versiones de actions, runtimes obsoletos, permisos mínimos, secretos y workflows. |
| Política de datos sintéticos | Anual o ante cambio de riesgo | Controles PII, secretos, generación y proceso de publicación. |

Las frecuencias son recomendaciones, no fechas oficiales de fin de soporte. Comprueba el ciclo de vida publicado por cada proveedor.

## Vigencia de herramientas
- No asumir que una versión fijada seguirá recibiendo soporte.
- Comandos, capturas, menús y campos pueden cambiar; una captura antigua no sustituye una comprobación actual.
- Revalidar actualizaciones mayores en un entorno de prueba y registrar versión, SO, arquitectura, RAM, CPU, disco, ingesta y evidencia.
- No sustituir Wazuh ni cambiar el alcance pedagógico sin aprobación del responsable.
- ELK permanece pendiente/descartado por recursos para el entorno descrito hasta que se autorice una prueba comparable.

## Procedimiento de actualización
1. Abrir una rama de trabajo y describir el motivo.
2. Revisar README, plan, guías, glosario, dependencias y evaluaciones afectadas.
3. Consultar documentación oficial y anotar fecha, versión y enlaces.
4. No modificar el currículo ni los prerrequisitos fijados sin aprobación explícita.
5. Aplicar el cambio mínimo; conservar decisiones aprobadas.
6. Comprobar enlaces, rutas Markdown, tablas, Mermaid, ejemplos y scripts pertinentes.
7. Revisar que no se incluyan PII, secretos, credenciales ni logs de producción.
8. Actualizar fecha de revisión y estado de auditoría.
9. Solicitar revisión para cambios de seguridad, privacidad, dependencias o evaluación.
10. Registrar evidencia de validación; no marcar como probado lo que solo se revisó visualmente.

## Registro de mantenimiento

| Fecha | Componente | Versión revisada | Resultado / acción |
|---|---|---|---|
| 2026-11-05 | Wazuh | 4.9.0 | Validación física documentada en checklist; próxima revisión recomendada: 2027-05 |
| 2026-11-05 | Documentación Sprint 3 | N/A | Glosario, mapa de dependencias, política de datos y trackers creados |

## Criterio de publicación
Un cambio está listo cuando tiene propósito claro, rutas y enlaces revisados, ejemplos seguros, evidencia verificable y revisión de alcance. No sincronizar calendarios ni automatizaciones como parte de este mantenimiento.
