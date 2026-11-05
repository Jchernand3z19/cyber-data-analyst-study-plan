# Debug — Fase 4: Wazuh

## Ejercicio único — la alerta esperada no aparece

**Situación:** se repite la práctica del log sintético de fallo SSH, pero el dashboard no muestra la alerta esperada. El archivo JSON que se está usando contiene:

```json
{
  "timestamp": "2026-11-05T14:00:00Z",
  "agent": { "name": "lab-mac" },
  "data": {
    "srcip": "192.0.2.25",
    "srcuser": "analyst-test",
    "protocol": "ssh"
  },
  "rule": {
    "id": 5710,
    "level": 5,
    "mitre": { "id": "T1110.001" }
  },
}
```

**Tareas**
1. Identifica el error de formato JSON.
2. Explica por qué un JSON malformado puede impedir que el documento se procese o indexe.
3. Corrige el JSON y valida que los campos `srcip`, `srcuser` y `rule.mitre.id` estén presentes.
4. Si el JSON ya es válido pero la alerta no aparece, enumera comprobaciones de datos: origen de ingesta, timestamp/rango temporal, índice seleccionado, campos disponibles y filtro aplicado.
5. Distingue entre un documento que contiene `rule.id: 5710` y una alerta realmente generada por el motor de reglas de Wazuh. No fabriques ni fuerces una alerta.

## Solución razonada

- El error es la coma final después del objeto `rule`; JSON no permite una coma antes del cierre del objeto raíz.
- El documento corregido elimina esa coma.
- La presencia de `rule.id` en un JSON de ejemplo no prueba que Wazuh haya ejecutado la regla 5710. Para validar la detección de laboratorio, debe consultarse el evento procesado por Wazuh y su alerta resultante.
- Si el documento está indexado pero no aparece, revisar intervalo temporal, índice/data view, filtros y nombres reales de campos.
- Si el evento no se procesa, revisar el método de ingesta y el formato que espera esa vía; registrar la limitación en vez de declarar éxito.