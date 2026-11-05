# Debug — Fase 1

## 1. LEFT JOIN pierde filas

Consulta errónea: LEFT JOIN seguido de WHERE offers.price > 100. El filtro elimina filas sin oferta.

**Solución:** mover el filtro a ON si se deben conservar todos los productos. Verificar conteo de productos y NULLs.

## 2. Conteo inflado

Dos copias del mismo evento aparecen como dos eventos.

**Solución:** definir clave de evento/negocio, medir duplicados antes de deduplicar y conservar conteos de rechazo; no borrar silenciosamente.
