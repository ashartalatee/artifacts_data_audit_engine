import csv
from pathlib import Path

DATASET_PATH = Path("datasets/raw/force_broken_delimiter.csv")
OUTPUT_PATH = Path("01_parsing/outputs/parsing.txt")

def main():
    with open(DATASET_PATH, mode="r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)  # DELIBERATELY WRONG DELIMITER

        rows = []
        error_count = 0

        for i, row in enumerate(reader):
            try:
                rows.append(row)
            except Exception as e:
                error_count += 1
                rows.append(f"ERROR at row {i}: {e}")

    with open(OUTPUT_PATH, "w", encoding="utf-8") as out:
        out.write("=== PARSING ERROR LOG ===\n")
        out.write(f"Rows attempted: {len(rows)}\n")
        out.write(f"Errors captured: {error_count}\n\n")

        for r in rows:
            out.write(str(r) + "\n")

if __name__ == "__main__":
    main()
