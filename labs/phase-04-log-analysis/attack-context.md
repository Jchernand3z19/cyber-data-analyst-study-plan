# Laboratorio — ATT&CK como vocabulario de datos

Objetivo: etiquetar descriptivamente eventos de autenticación observados en Wazuh. No crear reglas, playbooks ni respuesta operativa.

- Táctica: objetivo general del comportamiento.
- Técnica: forma de alcanzar un objetivo.
- Subtécnica: variante específica, solo si hay evidencia suficiente.
- Etiqueta: hipótesis analítica, no atribución ni confirmación de incidente.

Referencia: [MITRE ATT&CK Enterprise](https://attack.mitre.org/matrices/enterprise/) y [T1110.001 — Password Guessing](https://attack.mitre.org/techniques/T1110/001/). Registrar versión y fecha consultada.

## Evento central validado en laboratorio

Se ingirió un log sintético de fallo de autenticación SSH en Wazuh 4.9.0 Single-node. Wazuh generó una alerta asociada a la regla **5710**, nivel **5**, con mapeo automático a **MITRE ATT&CK T1110.001 — Password Guessing**.

| Evidencia | Valor observado |
|---|---|
| Evento | Fallo de autenticación SSH (log sintético) |
| Plataforma | Wazuh 4.9.0 Single-node |
| Regla Wazuh | 5710 |
| Nivel | 5 |
| Técnica MITRE | T1110.001 — Password Guessing |
| Campos para análisis | `srcip`, `srcuser`, `rule.mitre.id` |
| Interpretación | Evento compatible con intento de adivinar contraseña; no demuestra por sí solo acceso exitoso ni intrusión |

## Tabla log → técnica

| ID | Evento observado | Táctica candidata | Técnica/subtécnica | Evidencia disponible | Datos faltantes | Confianza |
|---|---|---|---|---|---|---|
| SSH-01 | Fallo de autenticación SSH; Wazuh rule 5710, nivel 5 | Credential Access | T1110.001 — Password Guessing | Alerta Wazuh y mapeo automático; consultar `srcip`, `srcuser`, `rule.mitre.id` | Frecuencia/ventana completa, contexto del activo, si hubo login exitoso posterior, legitimidad del origen | Media para la clasificación del evento; insuficiente para afirmar incidente |

La etiqueta T1110.001 se conserva como clasificación observada por Wazuh en esta prueba. No generalices que todo fallo SSH corresponde a Password Guessing ni que una alerta prueba un ataque exitoso.

## Ejercicio de análisis

1. Recupera el evento en el dashboard de Wazuh.
2. Registra `srcip`, `srcuser`, `rule.id`, `rule.level` y `rule.mitre.id`.
3. Comprueba si el campo MITRE coincide con T1110.001.
4. Separa el hecho (fallo SSH) de la clasificación (Password Guessing) y de la hipótesis (posible intento repetido).
5. Documenta qué evidencia adicional haría falta para estimar volumen, recurrencia y resultado.

## Preguntas

1. ¿Qué evidencia conecta el log con T1110.001?
2. ¿Por qué la regla 5710 no confirma que alguien haya iniciado sesión?
3. ¿Qué cambia si `srcip` o `srcuser` están vacíos?
4. ¿Qué sesgo aparece al etiquetar todo fallo como ataque?
5. ¿Qué porcentaje de eventos puede clasificarse con los campos disponibles?