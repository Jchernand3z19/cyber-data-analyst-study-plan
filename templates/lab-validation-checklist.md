# Checklist de validación de laboratorios

Completa una fila con evidencia real antes de declarar una herramienta validada. Documentación consultada el 2026-11-05; los valores publicados son requisitos de referencia, no mediciones de este Mac.

## Comparación SIEM — despliegue local de laboratorio

| Campo | Wazuh all-in-one | Elastic Stack (Elasticsearch + Kibana) |
|---|---|---|
| SO / arquitectura | Componentes centrales en Linux 64-bit; quickstart enumera Ubuntu 16.04–24.04, Amazon Linux, RHEL y otras distribuciones. x86_64 y ARM64 según guía. No instalar servidor central nativo en macOS; usar Linux VM/containers compatibles. | Elasticsearch soporta paquetes Linux, macOS y Windows; Kibana packages Linux, Darwin y Windows. Docker para desarrollo. Confirmar matriz exacta de versión/arquitectura antes de descargar. |
| RAM | Quickstart oficial: 8 GiB recomendados para 1–25 agentes all-in-one. No confundir mínimo del manager aislado con stack completo. | No hay un único mínimo universal para el stack de laboratorio. La guía Docker exige Docker Desktop con al menos 4 GB asignados; Elasticsearch usa heap y memoria fuera del heap. 4 GB es asignación mínima documentada para seguir quickstart, no recomendación de rendimiento. |
| Disco | 50 GB para escenario quickstart de 1–25 agentes y 90 días de datos. El uso real depende de alertas/retención. | No se publica un mínimo universal de disco para el stack local. Reservar 20 GB libres como presupuesto inicial de laboratorio (supuesto operativo, no mínimo oficial); medir índices, volúmenes y crecimiento. |
| Dependencias | Linux 64-bit, privilegios root/sudo, conectividad para paquetes, puertos requeridos, indexer + server + dashboard; agente opcional para el ejercicio de logs locales. | Docker Desktop o paquetes compatibles; Elasticsearch + Kibana misma versión; recursos Docker asignados; configuración de kernel/sistema (p. ej. vm.max_map_count en Linux para escenarios aplicables). |
| Tiempo de instalación | Estimación de planificación: 30–60 min en VM Linux limpia, sin contar descarga lenta ni resolución de fallos. **No medido.** | Estimación de planificación: 20–45 min con Docker quickstart, sin contar descargas lentas ni resolución de fallos. **No medido.** |
| Facilidad de setup | Media: instalador asistido, pero despliega tres componentes y requiere Linux/recursos/puertos. | Media: Docker quickstart simplifica inicio, pero exige Docker, memoria y versiones coordinadas. |
| Ingesta sintética | Pendiente: enviar JSON/NDJSON por método documentado de ingestión/indexación; confirmar documento visible y campos consultables. | Pendiente: crear índice e indexar documento JSON por API REST; confirmar documento recuperable y campos consultables. |
| Resultado esperado | Documento sintético visible con event_id, timestamp, event_type, outcome y source_label; conteo coincide con archivo fuente. | Documento sintético recuperable desde índice; conteo y campos coinciden con archivo fuente. |
| Limitaciones | Orientado a eventos/alertas de seguridad; componentes centrales demandan RAM/disco; el agente y reglas de Wazuh no serán entregables de aprendizaje. | Más genérico y flexible, pero requiere modelar índices/pipelines; Kibana/Elastic features pueden variar por licencia; más decisiones de configuración. |
| Estado | **pendiente** — no instalado ni medido en el equipo del usuario. | **pendiente** — no instalado ni medido en el equipo del usuario. |

### Lectura provisional (no es selección)
El requisito publicado de Wazuh all-in-one es 8 GiB RAM y 50 GB para el escenario 1–25 agentes/90 días. Elastic publica un mínimo de 4 GB asignados a Docker Desktop para su quickstart de desarrollo, pero no un mínimo universal de disco o RAM para un stack completo. No son pruebas equivalentes ni permiten declarar ganador. En un Mac de 24 GB ambos podrían ser candidatos, pero VM/Docker, macOS y otras cargas compiten por recursos; hace falta medirlos. **Decisión: abierta.**

## Prueba reproducible para ambas candidatas

1. Registrar fecha, versión, arquitectura, SO invitado/host y espacio libre antes de empezar.
2. Usar la misma VM Linux o entorno Docker limpio, mismo límite de CPU/RAM y mismo dataset.
3. Medir tiempo desde inicio de instalación hasta dashboard/servicio disponible.
4. Registrar RAM idle y pico durante arranque e ingesta; registrar disco antes/después.
5. Ingerir exactamente 5 eventos sintéticos (sin datos reales), cada uno con event_id único, timestamp UTC, event_type, outcome y source_label.
6. Consultar los cinco documentos; comparar conteo, campos y timestamps contra CSV fuente.
7. Reiniciar y comprobar persistencia; registrar errores y tiempo de recuperación.
8. Guardar captura/log saneado y completar el registro siguiente.

### Registro de prueba (duplicar por candidata)
- Fecha / versión:
- Host / SO invitado / arquitectura:
- Método de instalación:
- CPU/RAM asignada:
- RAM idle / pico:
- Disco antes / después:
- Inicio / fin / minutos medidos:
- Ingesta: 5 enviados / ___ consultables:
- Campos y conteos conciliados:
- Reinicio/persistencia:
- Errores:
- Evidencia adjunta:
- Estado: **pendiente** hasta completar todos los pasos; **validado** solo si instala, ingiere, consulta y persiste; **bloqueado** si un impedimento reproducible lo impide.

## Procedimiento de ingesta sintética

**Elastic:** iniciar Elasticsearch y Kibana con el quickstart oficial de Docker; crear un índice de laboratorio; indexar JSON por API REST; ejecutar una consulta de búsqueda y una agregación por event_type. No exponer el puerto a Internet.

**Wazuh:** completar quickstart all-in-one en Linux; para prueba de ingestión usar el mecanismo documentado de recepción/indexación soportado por la versión seleccionada y verificar documento en el indexer. Si la ingesta directa de JSON requiere agente/configuración adicional, registrar el paso como dependencia y no simular éxito.

## Fuentes oficiales
- Wazuh [Quickstart y requisitos](https://documentation.wazuh.com/current/quickstart.html)
- Wazuh [Installation guide](https://documentation.wazuh.com/current/installation-guide/index.html)
- Elastic [Install Elasticsearch](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/installing-elasticsearch)
- Elastic [Install Kibana](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/install-kibana)
- Elastic [Docker quickstart](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/install-kibana-with-docker)
- Elastic [JVM memory guidance](https://www.elastic.co/docs/reference/elasticsearch/jvm-settings)

## Otras herramientas
| Herramienta | SO | Setup | Estado |
|---|---|---|---|
| SQLite + CLI | macOS | Por medir | pendiente |
| Python + cliente HTTP | macOS | Por medir | pendiente |
| Power BI Desktop | Windows virtualizado en Mac | Por medir | pendiente |

