#!/usr/bin/env python3
"""Profile synthetic authentication logs and produce data-quality summaries."""

from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "sample_auth_events.csv"
OUTPUT_DIR = BASE_DIR / "output"


def parse_timestamp(value: str) -> datetime:
    parsed = datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    return parsed.replace(tzinfo=timezone.utc)


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    valid: list[dict[str, str]] = []
    rejected: list[dict[str, str]] = []
    seen: set[str] = set()

    with INPUT_FILE.open(newline="", encoding="utf-8") as source:
        reader = csv.DictReader(source)
        required = {"timestamp_utc", "event_type", "user_alias", "outcome", "request_id"}
        missing = required - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"Missing columns: {', '.join(sorted(missing))}")

        for line, row in enumerate(reader, start=2):
            request_id = (row.get("request_id") or "").strip()
            empty = [name for name in required if not (row.get(name) or "").strip()]
            if empty:
                rejected.append({"source_line": str(line), "request_id": request_id,
                                 "reason": "missing_required_fields:" + ",".join(sorted(empty))})
                continue
            if request_id in seen:
                rejected.append({"source_line": str(line), "request_id": request_id,
                                 "reason": "duplicate_request_id"})
                continue
            try:
                timestamp = parse_timestamp(row["timestamp_utc"].strip())
            except ValueError:
                rejected.append({"source_line": str(line), "request_id": request_id,
                                 "reason": "invalid_timestamp"})
                continue
            seen.add(request_id)
            valid.append({**row, "timestamp_utc": timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")})

    by_type = Counter(row["event_type"] for row in valid)
    by_outcome = Counter(row["outcome"] for row in valid)
    by_type_outcome = Counter((row["event_type"], row["outcome"]) for row in valid)
    summary = {
        "input_rows": len(valid) + len(rejected),
        "valid_events": len(valid),
        "rejected_events": len(rejected),
        "completeness_required_fields": {
            field: sum(1 for row in valid if row.get(field, "").strip()) for field in sorted(required)
        },
        "events_by_type": dict(sorted(by_type.items())),
        "events_by_outcome": dict(sorted(by_outcome.items())),
        "events_by_type_and_outcome": [
            {"event_type": key[0], "outcome": key[1], "count": count}
            for key, count in sorted(by_type_outcome.items())
        ],
        "rejected_rows": rejected,
        "time_basis": "UTC",
        "interpretation": "Descriptive profile of synthetic records; no detection rule or incident conclusion is produced."
    }

    with (OUTPUT_DIR / "valid_events.csv").open("w", newline="", encoding="utf-8") as target:
        fields = ["timestamp_utc", "event_type", "user_alias", "source_label", "outcome", "severity", "request_id"]
        writer = csv.DictWriter(target, fieldnames=fields)
        writer.writeheader()
        writer.writerows(valid)

    with (OUTPUT_DIR / "event_summary.csv").open("w", newline="", encoding="utf-8") as target:
        writer = csv.DictWriter(target, fieldnames=["event_type", "outcome", "count"])
        writer.writeheader()
        writer.writerows(summary["events_by_type_and_outcome"])

    (OUTPUT_DIR / "quality_report.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
