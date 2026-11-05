# Laboratorios reproducibles

Los laboratorios complementan las guías de fase con ejercicios ejecutables. Todos los datos incluidos son ficticios y no representan personas, empresas, cuentas ni sistemas reales.

## Laboratorios disponibles

| Fase | Laboratorio | Recursos |
|---|---|---|
| 1 | HTTP y SQL | [Guía y práctica SQLite](phase-01-http-sql/README.md) |
| 2 | Python y calidad de datos | [Guía, CSV y validador](phase-02-data-quality/README.md) |
| 3 | Power BI y modelo analítico | [Guía, CSV y medidas DAX](phase-03-power-bi/README.md) |
| 4 | Logs y detección | [Guía, eventos sintéticos y analizador Python](phase-04-log-analysis/README.md), [guía de consultas SPL de referencia](phase-04-log-analysis/splunk-search-lab.md; consulta de sintaxis, no plataforma SIEM validada) |
| 5 | Gobierno y proyecto final | [Guía de fase 5](../phases/phase-05-governance/README.md) y [plantillas de gobierno](../phases/phase-05-governance/templates/README.md). |

## Verificación local de scripts

Desde la raíz del repositorio, ejecuta `bash labs/verify-labs.sh`. El script corre SQLite, valida los conteos esperados del CSV de calidad y comprueba los resultados del analizador de logs. Requiere Python 3 y no instala dependencias externas. Los resultados se escriben en carpetas `output/` ignoradas por Git. Este chequeo no valida Power BI Desktop ni valida una plataforma SIEM. La selección de SIEM sigue pendiente entre Wazuh y ELK.

## Reglas

- Ejecuta los ejemplos localmente en un entorno controlado.
- No reemplaces los archivos sintéticos por datos privados o no autorizados.
- Revisa los resultados y explica cada regla antes de considerarla útil.
- Los scripts son material didáctico, no herramientas de producción ni productos SIEM.
- Los resultados se generan en carpetas locales `output/`; no es necesario subirlos al repositorio.
- No marques sesiones como aprobadas solo por ejecutar un script: completa también la explicación y evaluación de la sesión.
