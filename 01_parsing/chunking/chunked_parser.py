import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

INPUT_FILE = BASE_DIR / "datasets" / "raw" / "raw_sales_export.csv"
OUTPUT_FILE = BASE_DIR / "01_parsing" / "outputs" / "parsed_partial.csv"

CHUNK_SIZE = 1000


def parse_in_chunks():
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    header_written = OUTPUT_FILE.exists()

    for i, chunk in enumerate(pd.read_csv(INPUT_FILE, chunksize=CHUNK_SIZE)):
        print(f"[INFO] Processing chunk {i}")

        if chunk.empty:
            raise ValueError("Empty chunk detected")

        mode = "a" if header_written else "w"

        chunk.to_csv(
            OUTPUT_FILE,
            mode=mode,
            index=False,
            header=not header_written
        )

        header_written = True


if __name__ == "__main__":
    parse_in_chunks()
