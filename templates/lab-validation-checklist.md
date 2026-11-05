# Checklist de validación de laboratorios

Completa una fila con evidencia real antes de declarar una herramienta validada. Documentación consultada el 2026-11-05; los valores publicados son requisitos de referencia, no mediciones de este Mac.

## Comparación SIEM — despliegue local de laboratorio

| Campo | Wazuh all-in-one | Elastic Stack (Elasticsearch + Kibana) |
|---|---|---|
| SO / arquitectura | Validación realizada en Docker Desktop sobre macOS Apple Silicon, Wazuh 4.9.0 Single-node. Los componentes del stack se ejecutaron en contenedores; no fue una instalación nativa de los servicios centrales sobre macOS. | Elasticsearch soporta paquetes Linux, macOS y Windows; Kibana packages Linux, Darwin y Windows. Docker para desarrollo. Confirmar matriz exacta de versión/arquitectura antes de descargar. |
| RAM | Docker Desktop: **11.72 GiB asignados**. Consumo real del stack: **~2.9 GB** (Indexer 1.66 GB, Manager 911 MB, Dashboard 382 MB); CPU observada: **<4%**. Como referencia distinta de la medición local, el quickstart Wazuh recomienda 8 GiB para el escenario all-in-one de 1–25 agentes. | No hay un único mínimo universal para el stack de laboratorio. La guía Docker exige Docker Desktop con al menos 4 GB asignados; Elasticsearch usa heap y memoria fuera del heap. 4 GB es asignación mínima documentada para seguir quickstart, no recomendación de rendimiento. |
| Disco | 50 GB para escenario quickstart de 1–25 agentes y 90 días de datos. El uso real depende de alertas/retención. | No se publica un mínimo universal de disco para el stack local. Reservar 20 GB libres como presupuesto inicial de laboratorio (supuesto operativo, no mínimo oficial); medir índices, volúmenes y crecimiento. |
| Dependencias | Linux 64-bit, privilegios root/sudo, conectividad para paquetes, puertos requeridos, indexer + server + dashboard; agente opcional para el ejercicio de logs locales. | Docker Desktop o paquetes compatibles; Elasticsearch + Kibana misma versión; recursos Docker asignados; configuración de kernel/sistema (p. ej. vm.max_map_count en Linux para escenarios aplicables). |
| Tiempo de instalación | **No registrado en la evidencia recibida.** La duración exacta desde inicio hasta dashboard disponible no se proporciona; no se inventa. | No ejecutado. |
| Facilidad de setup | Media: instalador asistido, pero despliega tres componentes y requiere Linux/recursos/puertos. | Media: Docker quickstart simplifica inicio, pero exige Docker, memoria y versiones coordinadas. |
| Ingesta sintética | **Exitosa**: log sintético de fallo SSH procesado; Wazuh generó regla **5710**, nivel **5**, y mapeo MITRE ATT&CK **T1110.001 — Password Guessing**. | Pendiente: crear índice e indexar documento JSON por API REST; confirmar documento recuperable y campos consultables. |
| Resultado observado | Evento SSH fallido procesado por Wazuh; regla 5710 (nivel 5) y mapeo T1110.001. Campos de análisis: `srcip`, `srcuser`, `rule.mitre.id`. | Documento sintético recuperable desde índice; conteo y campos coinciden con archivo fuente. |
| Limitaciones | Orientado a eventos/alertas de seguridad; componentes centrales demandan RAM/disco; el agente y reglas de Wazuh no serán entregables de aprendizaje. | Más genérico y flexible, pero requiere modelar índices/pipelines; Kibana/Elastic features pueden variar por licencia; más decisiones de configuración. |
| Estado | **VALIDADO** — Wazuh 4.9.0 Single-node en Docker Desktop/macOS Apple Silicon. Ingesta comprobada; consumo y CPU medidos. Tiempo exacto de instalación no aportado. | **Pendiente / descartado por recursos** — no se realizó prueba comparable; se priorizó Wazuh. |

### Decisión de laboratorio
**Wazuh 4.9.0 Single-node queda seleccionado y validado** para este programa, con Docker Desktop en macOS Apple Silicon. Docker Desktop tenía 11.72 GiB asignados; el stack consumió aproximadamente 2.9 GB (Indexer 1.66 GB, Manager 911 MB y Dashboard 382 MB), con CPU inferior al 4%. La ingesta de un log sintético de fallo SSH produjo la regla 5710 (nivel 5) y el mapeo MITRE ATT&CK T1110.001 (Password Guessing).

**ELK queda pendiente / descartado por recursos para este entorno y alcance.** No se instaló ni se comparó en una prueba equivalente; no debe presentarse como benchmark que demuestre mayor consumo de ELK. El tiempo exacto de instalación de Wazuh no fue suministrado y permanece sin medir.

## Registro de validación física — Wazuh 4.9.0

- Entorno: Docker Desktop en macOS, Apple Silicon.
- Memoria asignada a Docker Desktop: 11.72 GiB.
- Despliegue: Wazuh 4.9.0 Single-node.
- Consumo aproximado: 2.9 GB total (Indexer 1.66 GB; Manager 911 MB; Dashboard 382 MB).
- CPU observada: inferior al 4%.
- Ingesta: exitosa; log sintético de fallo SSH.
- Resultado: regla 5710, nivel 5; MITRE ATT&CK T1110.001 — Password Guessing.
- Tiempo de instalación: no registrado en la información entregada.
- Estado: **validado para el laboratorio de aprendizaje**.

## Prueba reproducible para futuras revisiones

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

**Wazuh (validación ya completada):** la prueba local usó Wazuh 4.9.0 Single-node en Docker Desktop/macOS Apple Silicon. El log sintético de fallo SSH produjo la regla 5710 (nivel 5), con mapeo T1110.001. Para repetir, consultar `srcip`, `srcuser` y `rule.mitre.id` en la alerta procesada.

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

