# Laboratorio — ATT&CK como vocabulario de datos

Objetivo: etiquetar descriptivamente eventos sintéticos. No crear reglas, playbooks ni respuesta operativa.

- Táctica: objetivo general del comportamiento.
- Técnica: forma de alcanzar un objetivo.
- Subtécnica: variante específica, solo si hay evidencia suficiente.
- Etiqueta: hipótesis analítica, no atribución ni confirmación de incidente.

Referencia: [MITRE ATT&CK Enterprise](https://attack.mitre.org/matrices/enterprise/) y [Techniques](https://attack.mitre.org/techniques/). Registrar versión y fecha consultada.

## Dataset sintético

| ID | Evento observado | Táctica candidata | Técnica | Datos faltantes | Confianza |
|---|---|---|---|---|---|
| E01 | 4 fallos de autenticación | Credential Access (hipótesis) | Sin clasificar | Origen, identidad, ventana, contexto | Baja |
| E02 | Proceso no habitual | Execution (hipótesis) | Sin clasificar | Nombre, usuario, proceso padre | Baja |
| E03 | Cambio de grupo | Privilege Escalation (hipótesis) | Sin clasificar | Actor, autorización, estado previo | Baja |
| E04 | Conexión saliente | Command and Control (hipótesis) | Sin clasificar | Proceso, destino validado, DNS | Baja |
| E05 | Login exitoso desde origen nuevo | Sin clasificar | Sin clasificar | MFA, dispositivo, historial | Baja |

No fuerces una etiqueta. Produce tabla log→técnica con justificación, evidencia faltante y confianza; CSV clasificado; informe breve con cobertura, porcentaje sin clasificar e incertidumbre.

## Preguntas
1. ¿Qué etiquetas son hipótesis?
2. ¿Qué sesgo aparece al etiquetar todo fallo como ataque?
3. ¿Cómo cambia cobertura si exiges evidencia más fuerte?
