# Test de nivel inicial

Este diagnóstico ayuda a decidir si puedes omitir la Fase 0 o la Fase 1. Responde sin consultar documentación. En preguntas de opción múltiple selecciona una respuesta. En las preguntas de aplicación, escribe una respuesta breve.

## Preguntas (24)

1. ¿Qué identifica una dirección IP en una red?
2. ¿Qué función cumple un puerto TCP/UDP?
3. ¿TCP y UDP ofrecen exactamente el mismo tipo de entrega? Explica brevemente.
4. ¿Qué resuelve DNS?
5. En una tabla, ¿qué representa una fila?
6. ¿Para qué sirve una clave primaria?
7. ¿Qué problema puede causar una clave duplicada en una dimensión?
8. En JSON, ¿qué diferencia hay entre un objeto y un array?
9. ¿Qué representa una etiqueta HTML?
10. ¿Qué diferencia hay entre cliente y servidor?
11. ¿Qué suele indicar un código HTTP 200?
12. ¿Qué diferencia básica existe entre 401 y 403?
13. ¿Qué método HTTP se utiliza habitualmente para recuperar un recurso?
14. ¿Qué es una cabecera HTTP?
15. ¿Qué devuelve normalmente una consulta SQL SELECT?
16. ¿Qué hace WHERE en SQL?
17. ¿Para qué se utiliza JOIN?
18. ¿Qué función cumple GROUP BY?
19. ¿Por qué es preferible parametrizar una consulta SQL?
20. ¿Qué diferencia existe entre autenticación y autorización?
21. ¿Qué dato no debería aparecer en un log: conteo de eventos, timestamp, token de sesión o tipo de evento?
22. ¿Qué significa que un dato sea sintético?
23. Un CSV tiene 100 filas; 8 tienen fecha inválida. ¿Qué conteo mínimo debes informar?
24. Tienes eventos con timestamp, tipo y resultado. ¿Qué producto de datos sencillo crearías para comparar resultados por día?

## Clave de corrección

1. Identifica una interfaz/dispositivo dentro de una red IP (según contexto).
2. Identifica el servicio o aplicación/proceso de destino dentro del host.
3. No. TCP ofrece entrega orientada a conexión y mecanismos de orden/fiabilidad; UDP es datagramas sin garantía equivalente.
4. Traduce nombres de dominio a registros como direcciones IP.
5. Un registro que representa una observación/entidad según la granularidad definida.
6. Identificar de forma única cada fila.
7. Puede multiplicar filas en una relación y distorsionar agregaciones.
8. Objeto: pares clave-valor; array: colección ordenada de valores.
9. Define un elemento/estructura del documento.
10. El cliente inicia una solicitud; el servidor procesa y responde.
11. Solicitud procesada correctamente.
12. 401: falta autenticación válida; 403: acceso no permitido.
13. GET.
14. Metadato de solicitud/respuesta, como tipo de contenido o caché.
15. Un conjunto de filas/columnas resultante.
16. Filtra filas según una condición.
17. Combina filas relacionadas entre tablas mediante una condición.
18. Agrupa filas para calcular agregaciones.
19. Separa valores de la instrucción y reduce el riesgo de alterar la consulta.
20. Autenticación verifica quién eres; autorización determina qué puedes hacer.
21. Token de sesión.
22. Creado artificialmente para pruebas, sin representar datos reales de personas/sistemas.
23. 100 filas recibidas, 92 válidas y 8 inválidas (o una salida equivalente que conserve ambos conteos).
24. Una tabla agregada por día y resultado, con conteos y definición de periodo.

## Umbrales de decisión

- **Omitir Fase 0:** al menos 8/10 en preguntas 1–10 y respuestas coherentes en al menos 2 de las preguntas 23–24. Si no, completa las sesiones opcionales 0.1–0.6 según brechas.
- **Omitir Fase 1:** al menos 12/14 en preguntas 11–24, incluyendo obligatoriamente las preguntas 12, 19 y 20, y entregar una consulta SQL breve que use SELECT, WHERE y JOIN correctamente. La decisión debe revisarse con una evidencia práctica, no solo con el puntaje.
- Si no se alcanza el umbral de Fase 1, cursa la Fase 1 completa o acuerda una revisión de brechas antes de saltar sesiones.
