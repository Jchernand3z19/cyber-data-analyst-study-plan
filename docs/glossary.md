# Glosario — datos y seguridad

Definiciones orientadas a un perfil que analiza datos dentro del dominio de seguridad. Se prioriza el uso práctico en este programa.

| Término | Definición (perfil híbrido) | Sesión o fase donde se aplica |
|---|---|---|
| API | Interfaz para intercambiar datos entre sistemas mediante solicitudes y respuestas. | 23–24; Fase 2 |
| Alerta | Registro generado cuando un evento cumple una condición analítica; no prueba por sí sola un incidente. | 53–58; Fase 4 |
| Anonimización | Transformación destinada a impedir razonablemente la identificación; debe evaluarse el riesgo de reidentificación. | 48; Fases 3 y 5 |
| ATT&CK (MITRE) | Base de conocimiento que organiza tácticas, técnicas y subtécnicas adversarias; se usa para clasificar datos, no atribuir actores. | 53–54; Fase 4 |
| Autenticación | Proceso para comprobar una identidad declarada. | 4; Fase 1 |
| Autorización | Determinación de qué recursos o acciones puede utilizar una identidad. | 4; Fase 1 |
| Cardinalidad | Relación entre claves de tablas, por ejemplo uno-a-muchos. | 37–38; Fase 3 |
| Catálogo de datos | Inventario de datasets y metadatos que permite descubrirlos y entender su uso. | 73; Fase 5 |
| Clasificación de datos | Asignación de categorías según sensibilidad, propósito o requisitos de manejo. | 47, 72, 86; Fases 3 y 5 |
| Completitud | Grado en que los campos requeridos tienen valores utilizables. | 22, 32, 57, 75; Fases 2, 4 y 5 |
| CSV | Formato de texto tabular separado por delimitadores. | 21; Fase 2 |
| Dashboard | Presentación visual de métricas y dimensiones para responder preguntas analíticas. | 43–44, 58; Fases 3 y 4 |
| Dataset | Conjunto organizado de datos con estructura y propósito definidos. | Todas las fases |
| DAX | Lenguaje de expresiones para medidas y cálculos en modelos tabulares de Power BI. | 40–42; Fase 3 |
| Deduplicación | Identificación y tratamiento de registros repetidos según una clave o regla documentada. | 22, 33, 57; Fases 2 y 4 |
| Dimensión | Tabla o atributo que aporta contexto para analizar hechos, por ejemplo fecha, producto o categoría. | 37–38; Fase 3 |
| ETL | Extract, Transform, Load: extraer datos, transformarlos y cargarlos en un destino. | 21–22, 34; Fase 2 |
| Evento | Registro de una acción o condición observada por un sistema, como un fallo de autenticación. | 16, 27, 53–58; Fases 1, 2 y 4 |
| Faker | Biblioteca Python para generar datos ficticios plausibles; sus resultados deben revisarse para evitar coincidencias con personas reales. | Fases 2 y 4; política de datos sintéticos |
| Falso positivo potencial | Resultado que parece relevante según una regla, pero puede no representar el fenómeno buscado. | 61; Fase 4 |
| Granularidad | Nivel de detalle que representa cada fila de una tabla o hecho. | 37; Fase 3 |
| Hash | Resultado de una función de resumen; no equivale automáticamente a cifrado ni anonimización. | Concepto complementario; Fase 5 |
| JOIN | Operación SQL que combina filas de tablas relacionadas mediante una condición, normalmente claves. | 10; Fase 1 |
| JSON | Formato de texto para representar objetos y colecciones de datos estructurados. | 6, 21, 26; Fases 1 y 2 |
| Linaje de datos | Registro del origen, transformaciones, versiones y destinos de un dato. | 30, 50, 74; Fases 2, 3 y 5 |
| Log | Registro cronológico generado por una aplicación, sistema o dispositivo; su interpretación depende de campos, zona horaria y calidad. | 16, 27, 53–70; Fases 1, 2 y 4 |
| Metadatos | Datos que describen otros datos: propietario, formato, fecha, versión, fuente o clasificación. | 50, 73–74, 81; Fases 3 y 5 |
| MITRE ATT&CK T1110.001 | Subtécnica Password Guessing, asociada en el laboratorio al evento SSH sintético procesado por Wazuh con regla 5710; no demuestra acceso exitoso. | 53–56; Fase 4 |
| Modelo dimensional | Organización analítica de hechos y dimensiones para facilitar consultas y reporting. | 37–38; Fase 3 |
| Nulo (NULL) | Ausencia de un valor conocido; no equivale a cero, cadena vacía ni falso. | 22, 57; Fases 2 y 4 |
| PII / dato personal identificable | Información que identifica o puede contribuir a identificar a una persona, directa o indirectamente. | 47–49, 68, 72–77; Fases 3–5 |
| Pipeline | Secuencia reproducible de pasos que mueve y transforma datos desde una fuente hasta una salida. | 34–35, 84–85; Fases 2 y 5 |
| Power Query | Herramienta de conexión y transformación de datos utilizada en Power BI. | 39; Fase 3 |
| RLS | Row-Level Security: control que limita las filas visibles para un usuario según rol o contexto. | 45; Fase 3 |
| SIEM | Plataforma que centraliza y permite consultar eventos y alertas de seguridad; aquí Wazuh se usa como fuente analítica. | 53–58; Fase 4 |
| Seudonimización | Sustitución de identificadores directos por seudónimos; puede existir reidentificación con información adicional. | 48; Fases 3 y 5 |
| Tabla de hechos | Tabla que registra observaciones o eventos medibles a una granularidad definida. | 37–38; Fase 3 |
| Táctica | Categoría de objetivo adversario en ATT&CK; describe el propósito general de una técnica. | 53–54; Fase 4 |
| Técnica / subtécnica | Descripción de un comportamiento adversario; la subtécnica concreta una variante. | 53–54; Fase 4 |
| Transformación | Operación que modifica estructura, formato, tipo o contenido de datos mediante reglas explícitas. | 21–22, 30, 39; Fases 2 y 3 |
| IOC | Indicator of Compromise: observable como IP o hash que puede asociarse con actividad maliciosa; necesita contexto y vigencia. | Vocabulario contextual; Fases 4 y 5 |
| Wazuh | Plataforma open-source utilizada en el laboratorio como SIEM; la ruta consulta sus alertas sin enseñar administración operativa. | 53–58; Fase 4 |
| Calidad de datos | Adecuación de los datos a su uso, medida con completitud, validez, consistencia, unicidad y actualidad. | 22, 32–33, 57, 75; Fases 2, 4 y 5 |

## Nota
Cuando un término tenga un significado más amplio en la industria, esta tabla prioriza el uso de las actividades del programa. Registra definiciones adicionales en tus evidencias.
