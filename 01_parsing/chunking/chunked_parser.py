import pandas as pd
from pathlib import Path

from control.stop_conditions import stop_if, StopEngine
from schema.schema_validator import validate_schema

BASE_DIR = Path(__file__).resolve().parents[2]

INPUT_FILE = BASE_DIR / "datasets" / "raw" / "raw_sales_export.csv"
OUTPUT_FILE = BASE_DIR / "01_parsing" / "outputs" / "parsed_partial.csv"

CHUNK_SIZE = 1000
MAX_ALLOWED_CHUNKS = 10_000  # hard safety limit


def parse_in_chunks():
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    header_written = OUTPUT_FILE.exists()
    processed_chunks = 0

    try:
        for i, chunk in enumerate(
            pd.read_csv(INPUT_FILE, chunksize=CHUNK_SIZE)
        ):
            print(f"[INFO] Processing chunk {i}")

            # --- STOP CONDITIONS ---
            stop_if(chunk.empty, "EMPTY_CHUNK", {"chunk": i})
            stop_if(i > MAX_ALLOWED_CHUNKS, "CHUNK_LIMIT_EXCEEDED", {"chunk": i})

            # --- SCHEMA CONTRACT ---
            validate_schema(chunk)

            # --- WRITE OUTPUT ---
            mode = "a" if header_written else "w"
            chunk.to_csv(
                OUTPUT_FILE,
                mode=mode,
                index=False,
                header=not header_written
            )

            header_written = True
            processed_chunks += 1

    except StopEngine as e:
        print(f"[FATAL] PIPELINE STOPPED: {e}")
        print(f"[INFO] Chunks processed safely: {processed_chunks}")

    except Exception as e:
        # Ini crash → bukan keputusan
        print("[CRASH] Unexpected failure")
        raise


if __name__ == "__main__":
    parse_in_chunks()
