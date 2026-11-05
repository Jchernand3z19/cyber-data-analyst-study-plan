# Política de uso de datos sintéticos

**Versión:** 1.0  
**Aplicación:** todas las fases, laboratorios, evaluaciones, capturas, ejemplos y entregables.

## 1. Propósito y regla obligatoria
El programa analiza datos dentro del dominio de seguridad. Para ello, utiliza únicamente:
- Datos sintéticos generados para el ejercicio.
- Datos públicos cuya licencia y condiciones permitan el uso previsto.
- Datos de demostración expresamente autorizados y revisados para detectar información sensible.

**Nunca uses ni subas datos reales de producción**, aunque se hayan quitado nombres o reemplazado identificadores.

## 2. Por qué se prohíben los datos reales de producción
Los registros pueden contener PII directa o indirecta, identificadores de dispositivos, IP, usuarios, correos, tokens, rutas internas, detalles de infraestructura, horarios, patrones de comportamiento o información comercial. Quitar nombres no garantiza anonimización: la combinación de atributos puede permitir reidentificación.

Compartirlos en GitHub, capturas, issues, notebooks o servicios externos puede incumplir obligaciones contractuales, políticas internas, licencias o requisitos legales. Este repositorio no es un entorno autorizado para recibirlos.

## 3. Generación reproducible
Preferir generadores como Faker para Python y documentar dataset, generador, versión, semilla, fecha y transformaciones.

Instalación de ejemplo:

    python -m pip install Faker

Ejemplo:

    from faker import Faker
    import json
    import random

    fake = Faker("en_US")
    Faker.seed(2026)
    random.seed(2026)

    events = []
    for event_id in range(1, 21):
        events.append({
            "event_id": f"EVT-{event_id:04d}",
            "timestamp": fake.date_time().isoformat(),
            "srcip": f"192.0.2.{random.randint(1, 254)}",
            "srcuser": f"lab-user-{random.randint(1, 8)}",
            "event_type": random.choice(["ssh_login_failed", "ssh_login_success"]),
            "environment": "training"
        })

    with open("synthetic-events.json", "w", encoding="utf-8") as f:
        json.dump(events, f, indent=2)

Los rangos 192.0.2.0/24, 198.51.100.0/24 y 203.0.113.0/24 están reservados para documentación y son preferibles a IP públicas reales. Usa alias artificiales, no nombres ni correos que puedan coincidir con personas identificables. Para campos sensibles usa marcadores como PERSON-0001, user-lab-01 y dominios reservados como example.invalid.

Faker produce valores plausibles, no garantiza anonimato. No generes números oficiales, tarjetas, teléfonos ni correos con apariencia de datos reales utilizables.

## 4. Controles PII y secretos
Antes de guardar o publicar un dataset, captura o notebook:
1. Define propósito y campos mínimos necesarios.
2. Revisa nombres, correos, teléfonos, direcciones, identificadores oficiales, cuentas, IP, user-agent, geolocalización y campos libres.
3. Sustituye identidades por alias sintéticos; utiliza rangos IP de documentación y dominios reservados.
4. Busca tokens, contraseñas, claves API, cookies, cabeceras Authorization, claves privadas y cadenas de conexión.
5. Comprueba que la combinación de campos no describa a una persona real ni permita inferirla razonablemente.
6. Revisa capturas, logs, nombres de archivo y metadatos, no solo la tabla principal.
7. Registra fuente, generador, versión, semilla y transformaciones.

Si existe duda sobre si un campo identifica a alguien, trátalo como dato personal y no lo publiques.

## 5. Datos de seguridad
- No copies logs reales de endpoints, firewalls, VPN, correo, IAM, SIEM ni sistemas corporativos.
- No utilices hostnames, usuarios, dominios, IP, rutas o identificadores internos de una organización.
- Crea eventos ficticios con marcas de tiempo controladas, alias inventados y campos documentados.
- Distingue eventos simulados de alertas realmente generadas por el SIEM. Un JSON que contenga rule.id no demuestra que Wazuh haya disparado esa regla.
- No compartas secretos ni evidencia operativa real en capturas del dashboard.

## 6. Almacenamiento y exposición accidental
- Mantén datasets en carpetas de laboratorio y comparte solo lo necesario.
- No subas datos reales/sensibles a repositorios, issues, pull requests ni artefactos CI.
- No incluyas credenciales en código, notebooks, variables impresas ni historial Git.
- Si detectas PII o un secreto, detén la publicación, retira el archivo compartido, rota/invalida el secreto cuando corresponda y notifica al propietario de los datos. Borrar un commit no garantiza que desaparezcan copias o clones.
- No intentes limpiar datos de producción para introducirlos al curso: genera un dataset sintético nuevo.

## 7. Criterio de aceptación
Un entregable se acepta cuando su fuente y propósito están documentados, los valores son sintéticos/públicos/autorizados, no contiene PII ni secretos, es reproducible y sus limitaciones están descritas. Ante duda, no publicar y solicitar revisión.

Esta política es una regla educativa del repositorio; no constituye asesoría legal ni sustituye la política de seguridad, privacidad o clasificación de una organización.
