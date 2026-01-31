import json
from datetime import datetime
from pathlib import Path

from reproducibility.fingerprint import file_sha256

BASE_DIR = Path("01_parsing/reproducibility")

LATEST_FILE = BASE_DIR / "run_metadata.json"
HISTORY_DIR = BASE_DIR / "run_history"

def save_run_metadata(input_file, output_file):
    HISTORY_DIR.mkdir(exist_ok=True)

    run_time = datetime.utcnow().isoformat()

    data = {
        "run_timestamp_utc": run_time,
        "input_sha256": file_sha256(input_file),
        "output_sha256": file_sha256(output_file),
        "engine_version": "v0.1"
    }

    # Save latest snapshot
    with open(LATEST_FILE, "w") as f:
        json.dump(data, f, indent=2)

    # Save historical record
    history_file = HISTORY_DIR / f"run_{run_time}.json"

    with open(history_file, "w") as f:
        json.dump(data, f, indent=2)
