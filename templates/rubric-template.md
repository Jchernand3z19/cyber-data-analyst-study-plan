# Rúbrica de evaluación de evidencias

Usa esta rúbrica para evaluar una evidencia concreta. La evidencia debe ser un producto de análisis de datos: consulta, tabla, dashboard o informe. No se evalúa la creación de reglas operativas, playbooks ni acciones de respuesta.

## Niveles

| Nivel | Descripción |
|---|---|
| Insuficiente | La evidencia falta, no se puede reproducir o contiene errores que invalidan la conclusión. |
| En desarrollo | Hay un resultado parcial; faltan validaciones, contexto o explicación de limitaciones. |
| Competente | El resultado es correcto, reproducible, está contextualizado y responde al objetivo. |
| Ejemplar | Además de competente, permite auditoría clara, compara alternativas y comunica incertidumbre y límites con precisión. |

## Criterios por evidencia

Puntúa cada criterio de 1 a 4 usando los niveles anteriores.

| Criterio | Qué se observa |
|---|---|
| Exactitud y calidad | Tipos, filtros, claves, fechas, nulos, duplicados y cálculos correctos. |
| Reproducibilidad | Fuente, pasos, consulta/código y parámetros suficientes para repetir el resultado. |
| Interpretación | La tabla, métrica o visual responde a una pregunta concreta y evita inferencias no sustentadas. |
| Comunicación y límites | Contexto, definiciones, incertidumbre, privacidad y limitaciones documentadas. |

**Aprobación sugerida:** mínimo 12/16 y ningún criterio por debajo de 2. Si la evidencia es insuficiente, se corrige y vuelve a presentar; no se marca como aprobada.

## Ejemplos de aplicación por fase

### Fase 1 — HTTP, SQL y fundamentos de seguridad

**Evidencia:** consulta SQL sobre eventos web sintéticos que resume códigos HTTP por ruta y método.

- Exactitud: filtros y agregaciones concilian con el dataset.
- Reproducibilidad: consulta SQL y dataset sintético están incluidos.
- Interpretación: tabla explica distribución de estados sin afirmar ataques.
- Comunicación: se anonimizan alias y se explican límites de los datos.

### Fase 4 — Logs y análisis de datos de seguridad

**Evidencia:** consulta sobre eventos sintéticos y tabla agregada de fallos de autenticación por intervalo temporal.

- Exactitud: zona horaria, ventana, conteos y duplicados están tratados correctamente.
- Reproducibilidad: consulta SIEM o análisis equivalente, dataset y parámetros documentados.
- Interpretación: se distingue volumen observado de una conclusión sobre compromiso.
- Comunicación: se informan falsos positivos posibles, cobertura y límites del dataset.

### Fase 5 — Gobierno, privacidad y reporting

**Evidencia:** informe de calidad, inventario y matriz de acceso de un conjunto de datos ficticio.

- Exactitud: campos, clasificación y reglas de calidad son coherentes.
- Reproducibilidad: definiciones y criterios de aceptación están documentados.
- Interpretación: riesgos y métricas se vinculan con el propósito de los datos.
- Comunicación: se distingue control existente de propuesta y se explican límites legales/técnicos.
