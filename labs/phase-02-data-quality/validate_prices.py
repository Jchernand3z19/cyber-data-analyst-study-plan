#!/usr/bin/env python3
"""Validate a synthetic price-observation CSV using only Python's standard library."""

from __future__ import annotations

import csv
import json
import math
from collections import Counter
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "sample_prices.csv"
OUTPUT_DIR = BASE_DIR / "output"
REQUIRED = ("product_id", "store_id", "observed_at", "price", "currency")
ALLOWED_CURRENCIES = {"HNL", "USD"}


def validate_row(row: dict[str, str]) -> list[str]:
    errors: list[str] = []
    for field in REQUIRED:
        if not (row.get(field) or "").strip():
            errors.append(f"missing_{field}")

    timestamp = (row.get("observed_at") or "").strip()
    if timestamp:
        try:
            parsed = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
            if parsed.strftime("%Y-%m-%dT%H:%M:%SZ") != timestamp:
                errors.append("invalid_observed_at")
        except ValueError:
            errors.append("invalid_observed_at")

    raw_price = (row.get("price") or "").strip()
    if raw_price:
        try:
            numeric_price = float(raw_price)
            if not math.isfinite(numeric_price):
                errors.append("price_must_be_finite")
            elif numeric_price <= 0:
                errors.append("price_must_be_positive")
        except ValueError:
            errors.append("price_not_numeric")

    currency = (row.get("currency") or "").strip().upper()
    if currency and currency not in ALLOWED_CURRENCIES:
        errors.append("currency_not_allowed")

    return errors


def main() -> None:
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

    OUTPUT_DIR.mkdir(exist_ok=True)
    valid: list[dict[str, str]] = []
    rejected: list[dict[str, str]] = []
    seen_keys: set[tuple[str, str, str]] = set()
    rejection_counts: Counter[str] = Counter()

    with INPUT_FILE.open(newline="", encoding="utf-8") as source:
        reader = csv.DictReader(source)
        missing_columns = set(REQUIRED) - set(reader.fieldnames or [])
        if missing_columns:
            raise ValueError(f"Missing columns: {', '.join(sorted(missing_columns))}")

        for line_number, row in enumerate(reader, start=2):
            errors = validate_row(row)
            key = (
                (row.get("product_id") or "").strip(),
                (row.get("store_id") or "").strip(),
                (row.get("observed_at") or "").strip(),
            )
            if not errors and key in seen_keys:
                errors.append("duplicate_business_key")
            if errors:
                reason = ";".join(errors)
                rejected.append({**row, "source_line": str(line_number), "rejection_reason": reason})
                rejection_counts.update(errors)
            else:
                seen_keys.add(key)
                valid.append({**row, "source_line": str(line_number)})

    def write_csv(path: Path, rows: list[dict[str, str]], extra_fields: tuple[str, ...]) -> None:
        fieldnames = list(REQUIRED) + list(extra_fields)
        with path.open("w", newline="", encoding="utf-8") as target:
            writer = csv.DictWriter(target, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    write_csv(OUTPUT_DIR / "valid_rows.csv", valid, ("source_line",))
    write_csv(OUTPUT_DIR / "rejected_rows.csv", rejected, ("source_line", "rejection_reason"))

    total = len(valid) + len(rejected)
    report = {
        "input_file": INPUT_FILE.name,
        "rows_total": total,
        "rows_valid": len(valid),
        "rows_rejected": len(rejected),
        "acceptance_rate": round(len(valid) / total, 4) if total else 0,
        "rejection_reasons": dict(sorted(rejection_counts.items())),
        "business_key": ["product_id", "store_id", "observed_at"],
        "allowed_currencies": sorted(ALLOWED_CURRENCIES),
        "note": "Synthetic teaching data; rules are illustrative, not production policy.",
    }
    (OUTPUT_DIR / "quality_report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
