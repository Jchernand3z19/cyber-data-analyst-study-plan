#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

PYTHON_BIN="${PYTHON_BIN:-python3}"
command -v "$PYTHON_BIN" >/dev/null 2>&1 || {
  echo "ERROR: Python 3 was not found. Set PYTHON_BIN to its executable."
  exit 1
}

echo "[1/3] SQL / SQLite"
"$PYTHON_BIN" labs/phase-01-http-sql/sql_basics.py

echo "[2/3] Data quality"
"$PYTHON_BIN" labs/phase-02-data-quality/validate_prices.py
"$PYTHON_BIN" - <<'PY'
import json
from pathlib import Path
p = Path("labs/phase-02-data-quality/output/quality_report.json")
report = json.loads(p.read_text(encoding="utf-8"))
expected = {"rows_total": 7, "rows_valid": 2, "rows_rejected": 5}
for key, value in expected.items():
    if report.get(key) != value:
        raise SystemExit(f"FAIL: {key} expected {value}, got {report.get(key)}")
print("PASS: data-quality counts match the synthetic fixture.")
PY

echo "[3/3] Log analysis"
"$PYTHON_BIN" labs/phase-04-log-analysis/analyze_auth_logs.py
"$PYTHON_BIN" - <<'PY'
import json
from pathlib import Path
p = Path("labs/phase-04-log-analysis/output/analysis_report.json")
report = json.loads(p.read_text(encoding="utf-8"))
expected = {"valid_events": 7, "rejected_events": 2, "alerts_generated": 1}
for key, value in expected.items():
    if report.get(key) != value:
        raise SystemExit(f"FAIL: {key} expected {value}, got {report.get(key)}")
print("PASS: log-analysis counts match the synthetic fixture.")
PY

echo "All local script checks passed. Power BI and Splunk require separate interactive validation."
