# Flujo diario de estudio

A las **08:00 AM**, abre el evento del día en Google Calendar y revisa el objetivo, los recursos y la evidencia esperada. Completa el bloque de 90 minutos siguiendo los cinco pasos: **10 min recuperación activa → 20 min estudio → 35 min práctica guiada → 15 min ejercicio individual → 10 min evidencia y dudas**.

Al terminar la práctica y guardar la evidencia, antepone **✅** al título del evento (por ejemplo: `✅ Día 01 — Explicar cliente, servidor y ciclo HTTP`). El workflow consulta los eventos del día a las **23:55 hora de Honduras** y marca la sesión correspondiente como `[x]` en `tracker.md`; no modifica el currículo ni marca sesiones sin el marcador del evento.

```mermaid
graph TD
    A["🔁 10m · Repaso"] --> B["📘 20m · Estudio"]
    B --> C["🧪 35m · Práctica"]
    C --> D["📝 15m · Ejercicio"]
    D --> E["📁 10m · Evidencia"]
    E --> F["✅ Calendario"]
    F --> G["🤖 Sync GitHub"]
    classDef learning fill:#142d4e,stroke:#38bdf8,color:#f8fafc,stroke-width:2px;
    classDef evidence fill:#123b35,stroke:#34d399,color:#ecfdf5,stroke-width:2px;
    classDef automation fill:#3b2b16,stroke:#f59e0b,color:#fffbeb,stroke-width:2px;
    class A,B,C,D learning;
    class E evidence;
    class F,G automation;
```
