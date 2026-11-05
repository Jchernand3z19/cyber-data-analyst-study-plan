# Quiz — Fase 4: Wazuh y análisis de eventos (10 preguntas)

**Caso base:** Wazuh 4.9.0 Single-node en Docker Desktop/macOS Apple Silicon. Se asignaron 11.72 GiB a Docker Desktop; el stack consumió aproximadamente 2.9 GB (Indexer 1.66 GB, Manager 911 MB, Dashboard 382 MB) y CPU inferior al 4%. Se inyectó un log sintético de fallo SSH; Wazuh generó la regla 5710, nivel 5, con mapeo MITRE ATT&CK T1110.001 — Password Guessing.

Responde usando el caso y el dashboard. No interpretes la alerta como prueba de intrusión.

1. ¿Qué versión y despliegue de Wazuh se validaron?
2. ¿Cuánta RAM se asignó a Docker Desktop y cuál fue el consumo aproximado del stack?
3. ¿Qué componente consumió más memoria: Indexer, Manager o Dashboard? Indica el consumo reportado.
4. ¿Qué evento sintético se inyectó y qué regla de Wazuh lo procesó?
5. ¿Qué significa que la regla 5710 tenga nivel 5? ¿Por qué no equivale a confirmar un incidente?
6. ¿Qué técnica MITRE ATT&CK quedó mapeada y cuál es su nombre?
7. ¿Qué información analítica aportan los campos `srcip` y `srcuser`?
8. ¿Cómo filtrarías en el dashboard la regla 5710 y cómo comprobarías el mapeo mediante `rule.mitre.id`?
9. ¿Qué tres métricas de calidad revisarías para `srcip`, `srcuser` y `rule.mitre.id`?
10. Si el dashboard muestra varios fallos SSH desde una misma IP, ¿qué puedes afirmar y qué contexto adicional necesitas antes de concluir que hubo un ataque exitoso?

## Clave de respuestas

1. Wazuh 4.9.0 Single-node, ejecutado con Docker Desktop en macOS Apple Silicon.
2. 11.72 GiB asignados; consumo total aproximado 2.9 GB.
3. Indexer, aproximadamente 1.66 GB.
4. Un log sintético de fallo de autenticación SSH; regla 5710.
5. Es el nivel de severidad asignado por la regla en esta alerta; no demuestra por sí solo acceso exitoso ni intrusión.
6. T1110.001 — Password Guessing.
7. `srcip` identifica la IP de origen observada y `srcuser` el usuario asociado al evento, si esos campos están presentes.
8. Filtrar por `rule.id:5710` y revisar `rule.mitre.id` para comprobar T1110.001.
9. Completitud/nulos, consistencia de formato y valores ausentes o no normalizados; también duplicados si existe una clave de evento adecuada.
10. Se puede describir el volumen y la IP observada; faltan contexto temporal, legitimidad del origen, eventos de autenticación exitosa y correlación con otras evidencias.