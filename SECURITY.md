# Seguridad del repositorio y del entorno de estudio

Este documento registra controles recomendados y límites de verificación. No certifica que la configuración de la cuenta de GitHub o Google sea segura.

## Datos y archivos

- Los datasets de los laboratorios deben ser sintéticos.
- No subir datos personales, datos de clientes, exportaciones laborales, contraseñas, tokens, claves API ni archivos JSON de cuentas de servicio.
- El archivo raíz `.gitignore` excluye archivos de entorno, claves comunes, bases de datos y carpetas locales `output/`. **Git ignore no protege archivos que ya fueron agregados al historial**.
- Antes de publicar cambios, revisar `git status`, los archivos staged y el diff completo.
- Los resultados generados por los laboratorios deben permanecer locales salvo que se revisen y se confirme que contienen únicamente datos ficticios.

## GitHub

Configuración recomendada para el propietario del repositorio:

1. Mantener el repositorio **Private** mientras se revisa su contenido e historial.
2. Habilitar Secret scanning y Push protection si están disponibles en el plan y para el repositorio.
3. Usar GitHub Actions con permisos mínimos. El workflow de Calendar declara `contents: read`.
4. Revisar periódicamente Actions, colaboradores, tokens de acceso y aplicaciones autorizadas.
5. No imprimir valores de secretos en logs. El enmascaramiento automático de GitHub es una defensa adicional, no una razón para imprimir secretos.
6. Si una credencial se publica, revocarla en el proveedor, generar otra y revisar el historial; borrar el archivo en un commit posterior no invalida la credencial expuesta.

## Google Calendar

- La integración usa una cuenta de servicio y el scope `https://www.googleapis.com/auth/calendar.events`.
- Comparte únicamente el calendario que necesita la automatización, con permiso para gestionar eventos; no compartas otros calendarios.
- Guarda el JSON de servicio exclusivamente en GitHub Actions Secrets como `GOOGLE_SERVICE_ACCOUNT_JSON`; el ID del calendario se guarda como `GOOGLE_CALENDAR_ID`.
- No copies el JSON ni el valor de los secretos en issues, commits, capturas o conversaciones.
- Si la clave pudo exponerse, revócala desde Google Cloud Console y crea una nueva.

## Qué está comprobado en el código y qué no

| Comprobación | Estado |
|---|---|
| Los laboratorios de ejemplo están diseñados con datos ficticios | Revisado estáticamente |
| El workflow declara `contents: read` | Revisado en el archivo |
| Las credenciales se leen desde variables de entorno de Actions | Revisado en el código |
| El scope de Calendar se redujo a `calendar.events` | Cambio aplicado en código |
| El repositorio está configurado como privado | Confirmado en GitHub: `visibility=private` (2026-11-03) |
| Secret scanning y Push protection están activos | No verificado |
| Los valores de los secretos están correctos y no expuestos | No se inspeccionan ni deben compartirse |
| No hay secretos en todo el historial Git | No certificado; requiere escaneo del historial |
| Permisos efectivos del calendario compartido | Pendiente de revisar en Google Calendar |

## Respuesta ante exposición

1. Revocar o rotar inmediatamente la credencial en el servicio que la emitió.
2. Revisar logs de uso y actividad disponible.
3. Retirar el secreto del repositorio y del historial siguiendo el procedimiento del proveedor; la rotación es prioritaria.
4. Revisar accesos y permisos concedidos.
5. Documentar fecha, alcance y acciones sin copiar el valor expuesto.

**Regla:** si no hay evidencia verificable, el control se registra como pendiente y no como seguro o implementado.
