# Debug — Fase 4

## 1. Periodos inconsistentes

Se mezclan horas locales y UTC. **Solución:** conservar timestamp original y zona, convertir a UTC antes de agrupar, reportar fechas inválidas/sin zona.

## 2. Etiquetado excesivo

Todo fallo de login se etiqueta como acceso inicial confirmado. **Solución:** separar observación e hipótesis, marcar confianza baja y pedir contexto; no atribuir ni confirmar incidente.
