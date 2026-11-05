# Rúbrica de evaluación de evidencias

Aplicar esta misma rúbrica a TODAS las fases (1–5), no solo a las fases con laboratorio. La evidencia debe ser producto de datos: consulta, tabla, dashboard o informe. No se evalúan reglas operativas, playbooks ni acciones de respuesta.

## Niveles

| Nivel | Descripción |
|---|---|
| 1 — Insuficiente | Falta evidencia, no es reproducible o contiene errores que invalidan la conclusión. |
| 2 — En desarrollo | Resultado parcial; faltan validaciones, contexto o limitaciones. |
| 3 — Competente | Correcto, reproducible, contextualizado y responde al objetivo. |
| 4 — Ejemplar | Además, permite auditoría, compara alternativas y comunica incertidumbre y límites. |

## Criterios (1–4 cada uno)
1. Exactitud y calidad: tipos, filtros, claves, fechas, nulos, duplicados y cálculos.
2. Reproducibilidad: fuente, pasos, consulta/código, parámetros y versiones.
3. Interpretación: responde una pregunta y evita inferencias no sustentadas.
4. Comunicación y límites: definiciones, contexto, incertidumbre, privacidad y limitaciones.

Aprobación sugerida: mínimo 12/16 y ningún criterio por debajo de 2. Si no aprueba, corregir y volver a presentar.

## Aplicación por fase

| Fase | Evidencia ejemplo | Verificación específica |
|---|---|---|
| 1 — HTTP/SQL | Consulta de eventos web sintéticos por ruta y estado | JOIN, filtros, granularidad, conteo conciliado y secretos excluidos |
| 2 — Python/APIs | Pipeline CSV/JSON con salida limpia y rechazos | Tipos, nulos, duplicados, excepciones, conteos entrada/salida y trazabilidad |
| 3 — Power BI | Modelo y dashboard de métricas | Granularidad, relaciones, medidas reconciliadas, filtros y límites de RLS |
| 4 — Logs/ATT&CK/Wazuh | Consulta de alerta SSH, tabla log→T1110.001 y dashboard de calidad | Regla 5710/nivel 5, `srcip`, `srcuser`, `rule.mitre.id`, cobertura/nulos/duplicados, reproducibilidad y diferencia entre evento, alerta e incidente |
| 5 — Gobierno | Inventario, linaje, matriz de acceso e informe | Propósito, minimización, reglas de calidad, control existente vs propuesto y riesgo residual |

## Hoja de evaluación
- Fase / sesión:
- Evidencia / ubicación:
- Exactitud y calidad (1–4):
- Reproducibilidad (1–4):
- Interpretación (1–4):
- Comunicación y límites (1–4):
- Total /16:
- Correcciones necesarias:
- Estado: pendiente / en desarrollo / competente / ejemplar.
