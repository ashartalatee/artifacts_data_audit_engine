import json
import pandas as pd
from pathlib import Path
from datetime import datetime

SCHEMA_FILE = Path("expected_schema.json")
LOG_FILE = Path("schema_mismatch.log")

TYPE_MAP = {
    "int": "int64",
    "float": "float64",
    "string": "object"
}

def log_issue(message):
    timestamp = datetime.utcnow().isoformat()
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} | {message}\n")

def validate_schema(df):
    with open(SCHEMA_FILE) as f:
        schema = json.load(f)

    expected_cols = schema["columns"]
    strict = schema.get("strict", False)

    # Missing columns
    for col in expected_cols:
        if col not in df.columns:
            log_issue(f"MISSING COLUMN: {col}")
            raise ValueError(f"Missing column: {col}")

    # Extra columns
    if strict:
        for col in df.columns:
            if col not in expected_cols:
                log_issue(f"UNEXPECTED COLUMN: {col}")
                raise ValueError(f"Unexpected column: {col}")

    # Type & nullability
    for col, rules in expected_cols.items():
        expected_type = TYPE_MAP[rules["type"]]
        nullable = rules["nullable"]

        actual_type = str(df[col].dtype)

        if expected_type not in actual_type:
            log_issue(
                f"TYPE MISMATCH: {col} expected {expected_type}, got {actual_type}"
            )
            raise TypeError(f"Type mismatch on {col}")

        if not nullable and df[col].isnull().any():
            log_issue(f"NULL VIOLATION: {col}")
            raise ValueError(f"Null violation on {col}")

    return True
