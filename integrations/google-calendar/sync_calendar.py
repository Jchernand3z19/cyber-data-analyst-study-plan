#!/usr/bin/env python3
"""Create the recurring Security Data Analyst study sessions in Google Calendar."""
from __future__ import annotations

import json
import os
from datetime import datetime, time, timedelta
from zoneinfo import ZoneInfo

from google.oauth2 import service_account
from googleapiclient.discovery import build

TZ_NAME = "America/Tegucigalpa"
TZ = ZoneInfo(TZ_NAME)
SCOPES = ["https://www.googleapis.com/auth/calendar"]
TITLE = "Estudio Security Data Analyst"
MARKER_WEEKDAYS = "[SDA-WEEKDAYS]"
MARKER_SATURDAY = "[SDA-SATURDAY]"
REPOSITORY = "https://github.com/Jchernand3z19/cyber-data-analyst-study-plan"
DESCRIPTION = """Sesión de estudio de 60 minutos para el plan Security Data Analyst.
Retoma el tema pendiente más antiguo del tracker de GitHub. Si no terminas, deja el tema pendiente; no saltes contenido.
Distribución sugerida: 10 min repaso, 20 min estudio, 20 min práctica y 10 min evidencia.
Repositorio: {repository}
{marker}"""


def next_start(weekday: int) -> datetime:
    """Return the next local occurrence at 19:00; weekday is Monday=0."""
    now = datetime.now(TZ)
    candidate = datetime.combine(now.date(), time(19, 0), TZ)
    days_ahead = (weekday - now.weekday()) % 7
    if days_ahead == 0 and candidate <= now:
        days_ahead = 7
    return candidate + timedelta(days=days_ahead)


def event_body(start: datetime, marker: str, rrule: str) -> dict:
    end = start + timedelta(hours=1)
    return {
        "summary": TITLE,
        "description": DESCRIPTION.format(repository=REPOSITORY, marker=marker),
        "location": "Sesión personal de estudio",
        "start": {"dateTime": start.isoformat(), "timeZone": TZ_NAME},
        "end": {"dateTime": end.isoformat(), "timeZone": TZ_NAME},
        "recurrence": [rrule],
        "reminders": {
            "useDefault": False,
            "overrides": [{"method": "popup", "minutes": 10}],
        },
    }


def series_exists(service, calendar_id: str, marker: str) -> bool:
    now = datetime.now(TZ)
    params = {
        "calendarId": calendar_id,
        "timeMin": now.isoformat(),
        "timeMax": (now + timedelta(days=400)).isoformat(),
        "singleEvents": True,
        "q": TITLE,
        "maxResults": 2500,
    }
    while True:
        result = service.events().list(**params).execute()
        for event in result.get("items", []):
            if marker in event.get("description", "") and event.get("recurringEventId"):
                return True
        token = result.get("nextPageToken")
        if not token:
            return False
        params["pageToken"] = token


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

    series = [
        (MARKER_WEEKDAYS, next_start(0), "RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR"),
        (MARKER_SATURDAY, next_start(5), "RRULE:FREQ=WEEKLY;BYDAY=SA"),
    ]
    for marker, start, rrule in series:
        if series_exists(service, calendar_id, marker):
            print(f"Already exists: {marker}")
            continue
        created = service.events().insert(
            calendarId=calendar_id,
            body=event_body(start, marker, rrule),
        ).execute()
        print(f"Created {marker}: {created.get('htmlLink', '(link unavailable)')}")

    print(f"Calendar sync completed. Timezone={TZ_NAME}; schedule=Mon-Sat 19:00-20:00.")


if __name__ == "__main__":
    main()
