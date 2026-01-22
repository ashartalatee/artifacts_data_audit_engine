import csv
from pathlib import Path

DATASET_PATH = Path("datasets/raw/raw_sales_export.csv")
OUTPUT_PATH = Path("01_parsing/outputs/parsed_preview.txt")

def main():
    with open(DATASET_PATH, mode="r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)

        rows = list(reader)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as out:
        out.write("=== PARSED CSV PREVIEW ===\n")
        out.write(f"Total rows read (including header): {len(rows)}\n\n")

        for i, row in enumerate(rows[:10]):
            out.write(f"Row {i}: {row}\n")

if __name__ == "__main__":
    main()
