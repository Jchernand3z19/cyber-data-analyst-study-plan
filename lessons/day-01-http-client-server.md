# Día 1 — Cliente-servidor, HTTP y ciclo de una solicitud

**Estado:** pendiente. Esta guía no constituye evidencia de haber completado la sesión.

## Objetivo

Al terminar, podrás explicar cómo un cliente solicita un recurso, cómo un servidor responde y qué información se encuentra en los componentes principales de HTTP.

## Plan de 60 minutos

- **10 min — Recuperación:** escribe lo que ya sabes sobre navegador, servidor y página web. Si no sabes algo, anótalo sin buscar la respuesta todavía.
- **20 min — Estudio:** lee los conceptos y el ejemplo de abajo.
- **20 min — Práctica:** analiza la solicitud y respuesta sintéticas y completa la tabla.
- **10 min — Evidencia:** guarda tus respuestas y dudas en un borrador local para revisarlas. No marques el día como aprobado hasta superar la evaluación.

## Conceptos

- **Cliente:** software que inicia una solicitud; por ejemplo, un navegador.
- **Servidor:** sistema que recibe la solicitud y devuelve una respuesta.
- **HTTP:** protocolo de comunicación de solicitud y respuesta.
- **Método:** indica la acción solicitada, como `GET` para recuperar un recurso.
- **Ruta y query string:** identifican el recurso y pueden incluir parámetros, por ejemplo `/products?category=tablets`.
- **Cabeceras:** metadatos sobre la solicitud o respuesta, como el tipo de contenido esperado.
- **Código de estado:** indica el resultado general de la solicitud; por ejemplo, `200` suele indicar éxito, `404` recurso no encontrado y `500` error interno.
- **Cuerpo:** contenido opcional que se envía con una solicitud o respuesta; puede ser JSON, HTML u otro formato.

## Ejemplo sintético

Este ejemplo es ficticio; no se ha enviado a ningún servidor.

Solicitud:
```http
GET /products?category=tablets HTTP/1.1
Host: example.test
Accept: application/json
```

Respuesta:
```http
HTTP/1.1 200 OK
Content-Type: application/json
Cache-Control: no-store

{"items":[{"id":"P-100","name":"Sample tablet"}]}
```

## Práctica

Completa una tabla con estas columnas: elemento, valor del ejemplo, función y qué podrías concluir sin especular.

1. Identifica método, ruta, parámetro, host y cabecera `Accept`.
2. Identifica el código de estado y el tipo de contenido de la respuesta.
3. Explica qué parte es metadato y qué parte es el cuerpo.
4. Describe qué significaría recibir `404` en lugar de `200`.
5. Explica por qué el código `200` no demuestra por sí solo que el dato sea correcto, actualizado o completo.
6. Relaciona este flujo con PharmaTracker: el cliente podría pedir datos de productos y el proceso de análisis debería validar la respuesta antes de guardarla.

## Evidencia esperada

Un archivo de notas con la tabla completada, las respuestas a los seis puntos y al menos dos dudas o limitaciones identificadas. Si trabajas con una petición real, usa únicamente un recurso público y permitido; no compartas cookies, tokens, credenciales ni datos privados.

## Criterios de aprobación

Debes poder explicar con tus propias palabras:
- el recorrido cliente → solicitud → servidor → respuesta;
- la diferencia entre método, cabecera, estado y cuerpo;
- por qué un estado HTTP exitoso no garantiza calidad de datos;
- qué validaciones necesitaría un flujo como PharmaTracker antes de aceptar una respuesta.

Cuando confirmes que terminaste de estudiar y practicar, el asistente hará 2–3 preguntas de razonamiento. Si no dominas un criterio, repasarás ese punto antes de avanzar.