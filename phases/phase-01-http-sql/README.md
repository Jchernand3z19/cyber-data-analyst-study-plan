# Fase 1 — HTTP, web, SQL y fundamentos de seguridad

## Objetivo

Entender cómo viaja una solicitud entre cliente y servidor, cómo se representan los datos web y cómo consultar una base relacional de forma segura. El resultado es poder explicar riesgos y controles con evidencia, no atacar sistemas reales.

## Secuencia de estudio

| Días | Tema | Evidencia mínima |
|---|---|---|
| 1–2 | Cliente-servidor, HTTP, métodos, códigos y cabeceras | Diagrama de solicitud/respuesta anotado |
| 3–7 | URLs, parámetros, cookies, sesiones, JSON/HTML, DevTools y repaso | Ficha de inspección de una respuesta pública o de ejemplo |
| 8–11 | Tablas, claves, SELECT, filtros, JOIN y agregaciones | Consultas sobre datos sintéticos y resultados esperados |
| 12–16 | Consultas parametrizadas, inyección SQL, validación, privilegios y auditoría | Matriz riesgo-control con ejemplos seguros |
| 17–18 | Integración y evaluación | Informe breve reproducible y respuestas de razonamiento |

## Laboratorio A — HTTP sin riesgo

Usa un navegador y una página pública que permita inspección normal, o trabaja con el ejemplo local de abajo. No escanees ni automatices peticiones contra sitios de terceros.

Ejemplo conceptual:
```http
GET /products?category=tablets HTTP/1.1
Host: example.test
Accept: application/json
```

Una respuesta posible:
```http
HTTP/1.1 200 OK
Content-Type: application/json
Cache-Control: no-store

{"items":[{"id":"P-100","name":"Sample tablet"}]}
```

Documenta:
1. Método, ruta, host y cabecera Accept.
2. Código de estado y significado.
3. Tipo de contenido del cuerpo.
4. Qué dato es metadato y qué dato es contenido.
5. Qué cambiaría si la respuesta fuera 401, 404 o 500.

Este bloque es material de práctica sintético; no representa una petición ejecutada.

## Laboratorio B — SQL con datos sintéticos

Tablas de ejemplo:
- `products(product_id, name, category_id, price)`
- `categories(category_id, category_name)`
- `offers(product_id, store_id, observed_at, price)`

Ejercicios:
1. Selecciona productos con precio mayor que 100.
2. Ordena ofertas de la más reciente a la más antigua.
3. Une productos con categorías por `category_id`.
4. Calcula el precio mínimo por producto y tienda.
5. Explica por qué concatenar texto de usuario dentro de una consulta puede alterar su significado.
6. Describe cómo una consulta parametrizada separa la instrucción SQL de los valores.

No ejecutes cargas maliciosas en sistemas reales. Para estudiar inyección, utiliza únicamente un laboratorio local diseñado para ello o analiza ejemplos escritos sin ejecutarlos.

## Controles que debes poder explicar

- Validar formato, longitud y rango de las entradas.
- Preferir consultas parametrizadas.
- Dar a cada cuenta solo los permisos necesarios.
- Evitar guardar contraseñas, tokens y datos personales en logs.
- Registrar eventos útiles sin capturar innecesariamente valores sensibles.
- Diferenciar evidencia observada, hipótesis y conclusión.

## Entregables de la fase

- Diagrama de una solicitud/respuesta HTTP.
- Archivo de consultas SQL sobre datos ficticios, con comentarios y resultados esperados.
- Tabla de riesgos, impacto, control preventivo y evidencia.
- Informe final de una página con hallazgos y limitaciones.

## Criterios de aprobación

La fase se aprueba cuando puedes, sin memorizar respuestas:
1. Explicar el recorrido cliente → servidor → respuesta.
2. Interpretar métodos, códigos, cabeceras y cuerpo.
3. Escribir y explicar SELECT, JOIN y agregaciones básicas.
4. Explicar el riesgo de SQL injection y la prevención mediante parametrización.
5. Identificar qué datos no deben exponerse en logs.
6. Reproducir los ejercicios y documentar resultados reales.

Si falta un criterio, repasa ese contenido antes de avanzar. Nunca marques una sesión aprobada solo por leer esta guía.
