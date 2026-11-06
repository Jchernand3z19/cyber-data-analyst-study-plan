#!/usr/bin/env python3
"""Import today's completed Google Calendar sessions into tracker.md."""
from __future__ import annotations

import json
import os
import re
from datetime import datetime, time, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from google.oauth2 import service_account
from googleapiclient.discovery import build

TZ_NAME = "America/Tegucigalpa"
TZ = ZoneInfo(TZ_NAME)
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
MARKER_RE = re.compile(r"\[SDA-SESSION-(\d{2})\]")
ROW_RE = re.compile(r"^(\|\s*Día\s+(\d{1,2})\s*\|.*)$")


def completed_sessions(service, calendar_id: str) -> set[int]:
    now = datetime.now(TZ)
    start = datetime.combine(now.date(), time.min, TZ)
    end = start + timedelta(days=1)
    params = {
        "calendarId": calendar_id,
        "timeMin": start.isoformat(),
        "timeMax": end.isoformat(),
        "singleEvents": True,
        "orderBy": "startTime",
        "maxResults": 2500,
    }
    completed: set[int] = set()
    while True:
        response = service.events().list(**params).execute()
        for event in response.get("items", []):
            if "✅" not in event.get("summary", ""):
                continue
            match = MARKER_RE.search(event.get("description", ""))
            if match:
                completed.add(int(match.group(1)))
        token = response.get("nextPageToken")
        if not token:
            break
        params["pageToken"] = token
    return completed


def update_tracker(path: Path, completed: set[int]) -> int:
    original = path.read_text(encoding="utf-8")
    updated_lines = []
    changed = 0
    for line in original.splitlines():
        match = ROW_RE.match(line)
        if match:
            day = int(match.group(2))
            if day in completed:
                cells = line.rstrip().rstrip("|").split("|")
                # The final cell is the new Estado column.
                if len(cells) >= 2:
                    status = cells[-1].strip()
                    if status != "[x]":
                        cells[-1] = " [x] "
                        line = "|".join(cells) + "|"
                        changed += 1
        updated_lines.append(line)
    if changed:
        path.write_text("\n".join(updated_lines) + "\n", encoding="utf-8")
    return changed


def main() -> None:
    raw = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON", "")
    calendar_id = os.environ.get("GOOGLE_CALENDAR_ID", "").strip()
    if not raw or not calendar_id:
        raise SystemExit("Missing GOOGLE_SERVICE_ACCOUNT_JSON or GOOGLE_CALENDAR_ID.")
    try:
        info = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise SystemExit("GOOGLE_SERVICE_ACCOUNT_JSON is not valid JSON.") from exc
    credentials = service_account.Credentials.from_service_account_info(info, scopes=SCOPES)
    service = build("calendar", "v3", credentials=credentials, cache_discovery=False)
    root = Path(__file__).resolve().parents[2]
    completed = completed_sessions(service, calendar_id)
    tracker = root / "tracker.md"
    changed = update_tracker(tracker, completed)
    print(f"Completed session markers found today: {sorted(completed)}")
    print(f"Tracker rows changed: {changed}")


if __name__ == "__main__":
    main()
