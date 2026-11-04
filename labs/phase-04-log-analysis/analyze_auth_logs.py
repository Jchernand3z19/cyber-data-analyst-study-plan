#!/usr/bin/env python3
"""Analyze synthetic authentication events with a simple sliding-window rule."""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "sample_auth_events.csv"
OUTPUT_DIR = BASE_DIR / "output"
WINDOW = timedelta(minutes=10)
THRESHOLD = 5


def parse_timestamp(value: str) -> datetime:
    parsed = datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    return parsed.replace(tzinfo=timezone.utc)


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    events: list[dict[str, str | datetime]] = []
    rejected: list[dict[str, str]] = []
    seen_ids: set[str] = set()

    with INPUT_FILE.open(newline="", encoding="utf-8") as source:
        reader = csv.DictReader(source)
        required = {"timestamp_utc", "event_type", "user_alias", "outcome", "request_id"}
        missing = required - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"Missing columns: {', '.join(sorted(missing))}")

        for line_number, row in enumerate(reader, start=2):
            required_values = ("timestamp_utc", "event_type", "user_alias", "outcome", "request_id")
            empty_fields = [field for field in required_values if not (row.get(field) or "").strip()]
            if empty_fields:
                rejected.append({"source_line": str(line_number), "request_id": (row.get("request_id") or "").strip(),
                                 "reason": "missing_required_fields:" + ",".join(empty_fields)})
                continue
            request_id = (row.get("request_id") or "").strip()
            if request_id and request_id in seen_ids:
                rejected.append({"source_line": str(line_number), "request_id": request_id,
                                 "reason": "duplicate_request_id"})
                continue
            try:
                timestamp = parse_timestamp((row.get("timestamp_utc") or "").strip())
            except ValueError:
                rejected.append({"source_line": str(line_number), "request_id": request_id,
                                 "reason": "invalid_timestamp"})
                continue
            if request_id:
                seen_ids.add(request_id)
            events.append({**row, "parsed_timestamp": timestamp})

    by_alias: dict[str, list[dict[str, str | datetime]]] = defaultdict(list)
    for event in events:
        if event.get("event_type") == "authentication" and event.get("outcome") == "failure":
            by_alias[str(event.get("user_alias", ""))].append(event)

    alerts: list[dict[str, str]] = []
    for alias, failures in by_alias.items():
        failures.sort(key=lambda item: item["parsed_timestamp"])
        left = 0
        for right, event in enumerate(failures):
            current_time = event["parsed_timestamp"]
            while current_time - failures[left]["parsed_timestamp"] > WINDOW:
                left += 1
            count = right - left + 1
            if count >= THRESHOLD:
                alerts.append({
                    "user_alias": alias,
                    "window_start_utc": failures[left]["parsed_timestamp"].strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "window_end_utc": current_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "failure_count": str(count),
                    "rule": f">={THRESHOLD} failures within {int(WINDOW.total_seconds() / 60)} minutes",
                    "interpretation": "Review required; this alert alone does not confirm compromise.",
                })
                break

    with (OUTPUT_DIR / "alerts.csv").open("w", newline="", encoding="utf-8") as target:
        fields = ["user_alias", "window_start_utc", "window_end_utc", "failure_count", "rule", "interpretation"]
        writer = csv.DictWriter(target, fieldnames=fields)
        writer.writeheader()
        writer.writerows(alerts)

    report = {
        "valid_events": len(events),
        "rejected_events": len(rejected),
        "alerts_generated": len(alerts),
        "rejected_rows": rejected,
        "threshold": THRESHOLD,
        "window_minutes": int(WINDOW.total_seconds() / 60),
        "caution": "Synthetic teaching rule. An alert is not proof of an incident.",
    }
    (OUTPUT_DIR / "analysis_report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
