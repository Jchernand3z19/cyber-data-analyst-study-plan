#!/usr/bin/env python3
"""Sync the 3 setup sessions and 90 detailed study sessions to Google Calendar.

This migration removes only the two legacy recurring series created by the
previous version of this script (identified by exact markers), then creates
idempotent, individually described events from curriculum/session-plan.md.
"""
from __future__ import annotations

import json
import os
import re
from datetime import date, datetime, time, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from google.oauth2 import service_account
from googleapiclient.discovery import build

TZ_NAME = "America/Tegucigalpa"
TZ = ZoneInfo(TZ_NAME)
SCOPES = ["https://www.googleapis.com/auth/calendar.events"]
TITLE = "Security Data Analyst — Ruta de aprendizaje"
REPOSITORY = "https://github.com/Jchernand3z19/cyber-data-analyst-study-plan"
LEGACY_TITLE = "Estudio Security Data Analyst"
LEGACY_MARKERS = ("[SDA-WEEKDAYS]", "[SDA-SATURDAY]")
SETUP = [
    {
        "marker": "[SDA-SETUP-01]",
        "title": "Preparación 1/3 — Inventario y organización",
        "objective": "Verificar las herramientas ya disponibles en el Mac, organizar el espacio de trabajo y comprobar acceso al repositorio.",
        "practice": "Revisar Python, editor, Git, navegador y SQLite sin instalar duplicados. Anotar versiones y faltantes.",
        "evidence": "Inventario de herramientas y lista concreta de pendientes.",
    },
    {
        "marker": "[SDA-SETUP-02]",
        "title": "Preparación 2/3 — Herramientas base",
        "objective": "Instalar únicamente las herramientas que falten y comprobar que funcionan.",
        "practice": "Ejecutar una prueba mínima de Python, Git y SQLite; guardar los comandos y resultados sin datos sensibles.",
        "evidence": "Verificación reproducible del entorno y registro de versiones.",
    },
    {
        "marker": "[SDA-SETUP-03]",
        "title": "Preparación 3/3 — Accesos y entorno de práctica",
        "objective": "Comprobar accesos de GitHub y Google Calendar, y preparar datos sintéticos.",
        "practice": "Revisar permisos y workflow sin mostrar secretos. Preparar carpeta de trabajo y un dataset ficticio.",
        "evidence": "Checklist de accesos y dataset sintético listo.",
    },
]
SESSION_ROW = re.compile(r"^\|\s*(\d{1,2})\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|$")


def next_study_day(start: date | None = None) -> date:
    """Return the next available Mon-Sat date, including today if still ahead."""
    current = start or datetime.now(TZ).date()
    now = datetime.now(TZ)
    if current.weekday() == 6:
        current += timedelta(days=1)
    elif current == now.date() and now.time() >= time(8, 0):
        current += timedelta(days=1)
        if current.weekday() == 6:
            current += timedelta(days=1)
    return current


def study_dates(first: date, count: int):
    current = first
    for _ in range(count):
        if current.weekday() == 6:
            current += timedelta(days=1)
        yield current
        current += timedelta(days=1)


def parse_sessions(path: Path) -> list[dict]:
    sessions: dict[int, dict] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = SESSION_ROW.match(line)
        if not match:
            continue
        number = int(match.group(1))
        if not 1 <= number <= 90:
            continue
        _, objective, resource, practice, evidence = match.groups()
        sessions[number] = {
            "marker": f"[SDA-SESSION-{number:02d}]",
            "title": f"Día {number:02d} — {objective}",
            "objective": objective,
            "resource": resource,
            "practice": practice,
            "evidence": evidence,
        }
    missing = sorted(set(range(1, 91)) - set(sessions))
    if missing:
        raise SystemExit(f"Curriculum must contain exactly 90 sessions; missing: {missing}")
    return [sessions[n] for n in range(1, 91)]


def event_description(item: dict, kind: str) -> str:
    parts = [
        f"Tipo: {kind}",
        f"Objetivo: {item['objective']}",
    ]
    if item.get("resource"):
        parts.append(f"Recurso: {item['resource']}")
    parts.extend([
        f"Práctica: {item['practice']}",
        f"Evidencia esperada: {item['evidence']}",
        "Estructura (90 min): 10 min recuperación activa; 20 min estudio; "
        "35 min práctica guiada; 15 min ejercicio individual; 10 min evidencia y dudas.",
        "Regla: no marcar como completado hasta realizar la práctica y aprobar la evaluación.",
        f"Plan detallado: {REPOSITORY}/blob/main/curriculum/session-plan.md",
        f"Repositorio: {REPOSITORY}",
        item["marker"],
    ])
    return "\n\n".join(parts)


def event_body(item: dict, day: date, kind: str) -> dict:
    start = datetime.combine(day, time(8, 0), TZ)
    end = start + timedelta(minutes=90)
    return {
        "summary": item["title"],
        "description": event_description(item, kind),
        "location": "Sesión personal de estudio",
        "start": {"dateTime": start.isoformat(), "timeZone": TZ_NAME},
        "end": {"dateTime": end.isoformat(), "timeZone": TZ_NAME},
        "reminders": {
            "useDefault": False,
            "overrides": [{"method": "popup", "minutes": 10}],
        },
    }


def list_events(service, calendar_id: str, *, title: str, single_events: bool):
    params = {
        "calendarId": calendar_id,
        "timeMin": datetime.now(TZ).isoformat(),
        "timeMax": (datetime.now(TZ) + timedelta(days=500)).isoformat(),
        "singleEvents": single_events,
        "q": title,
        "maxResults": 2500,
    }
    while True:
        response = service.events().list(**params).execute()
        yield from response.get("items", [])
        token = response.get("nextPageToken")
        if not token:
            break
        params["pageToken"] = token


def remove_legacy_series(service, calendar_id: str) -> int:
    removed = 0
    for event in list_events(service, calendar_id, title=LEGACY_TITLE, single_events=False):
        description = event.get("description", "")
        if any(marker in description for marker in LEGACY_MARKERS):
            service.events().delete(calendarId=calendar_id, eventId=event["id"]).execute()
            removed += 1
            print(f"Removed legacy recurring series: {event['id']}")
    return removed


def existing_markers(service, calendar_id: str) -> set[str]:
    markers = set()
    for event in list_events(service, calendar_id, title="", single_events=True):
        description = event.get("description", "")
        match = re.search(r"\[SDA-(?:SETUP-\d{2}|SESSION-\d{2})\]", description)
        if match:
            markers.add(match.group(0))
    return markers


def main() -> None:
    raw_credentials = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON", "")
    calendar_id = os.environ.get("GOOGLE_CALENDAR_ID", "").strip()
    if not raw_credentials or not calendar_id:
        raise SystemExit("Missing GOOGLE_SERVICE_ACCOUNT_JSON or GOOGLE_CALENDAR_ID secret.")
    try:
        credentials_info = json.loads(raw_credentials)
    except json.JSONDecodeError as exc:
        raise SystemExit("GOOGLE_SERVICE_ACCOUNT_JSON is not valid JSON.") from exc

    credentials = service_account.Credentials.from_service_account_info(
        credentials_info, scopes=SCOPES
    )
    service = build("calendar", "v3", credentials=credentials, cache_discovery=False)

    # Remove only the old program-owned recurring series. No unrelated events are touched.
    removed = remove_legacy_series(service, calendar_id)
    already = existing_markers(service, calendar_id)

    curriculum_path = Path(__file__).resolve().parents[2] / "curriculum" / "session-plan.md"
    sessions = parse_sessions(curriculum_path)
    items = [(item, "preparation") for item in SETUP]
    items.extend((item, "learning session") for item in sessions)
    dates = list(study_dates(next_study_day(), len(items)))

    created = 0
    skipped = 0
    for (item, kind), day in zip(items, dates):
        if item["marker"] in already:
            skipped += 1
            continue
        service.events().insert(
            calendarId=calendar_id,
            body=event_body(item, day, kind),
        ).execute()
        created += 1
        print(f"Created {item['marker']} for {day.isoformat()}")

    print(
        f"Calendar sync complete: removed_legacy_series={removed}, "
        f"created={created}, already_present={skipped}, "
        f"schedule=Mon-Sat 08:00-09:30, timezone={TZ_NAME}."
    )


if __name__ == "__main__":
    main()
