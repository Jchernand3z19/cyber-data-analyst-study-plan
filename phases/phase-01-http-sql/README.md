# Fase 1 — Redes, HTTP, identidad, SQL y fundamentos de seguridad

> **Aviso de fase:** Día 1 incluye instalación (~1 h extra), el resto no. Si no se requiere instalar una herramienta en esta fase, utiliza ese tiempo para verificar versiones y abrir los archivos de práctica.


## Objetivo

Entender cómo viaja una solicitud entre cliente y servidor, cómo se representan los datos web y cómo consultar una base relacional de forma segura. El resultado es poder explicar riesgos y controles con evidencia, no atacar sistemas reales.

## Secuencia de estudio

| Días | Tema | Evidencia mínima |
|---|---|---|
| 1–2 | Cliente-servidor, HTTP, métodos, códigos y cabeceras | Diagrama de solicitud/respuesta anotado |
| 3–7 | DNS y recorrido web; identidad/autenticación/autorización; cookies; JSON/HTML; DevTools | Diagrama DNS→conexión→HTTP, ficha de identidad y evidencia saneada |
| 8–11 | Tablas, claves, SELECT, filtros, JOIN y agregaciones | Consultas sobre datos sintéticos y resultados esperados |
| 12–16 | Consultas parametrizadas, inyección SQL, validación, privilegios y auditoría | Matriz riesgo-control con ejemplos seguros |
| 17–18 | Integración y evaluación | Informe breve reproducible y respuestas de razonamiento |

## Redes e identidad antes de SQL

Antes de trabajar con consultas, distingue dominio, resolución DNS, dirección IP, puerto, protocolo, autenticación y autorización. No necesitas configurar routers, administrar servidores ni realizar escaneos. El objetivo es interpretar el flujo y no confundir HTTP 401 (no autenticado) con 403 (acceso denegado).

## Laboratorio ejecutable de SQL

Practica consultas SQL en una base SQLite en memoria con el [laboratorio SQL seguro](../../labs/phase-01-http-sql/README.md). No se conecta a sistemas externos.

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

El laboratorio SQL usa SQLite en memoria. La matriz de roles es un ejercicio de diseño conceptual: SQLite no demuestra la administración de usuarios y privilegios de un motor de base de datos empresarial.

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
