import csv
from pathlib import Path

DATASET_PATH = Path("datasets/raw/raw_sales_export_missing_col.csv")
OUTPUT_PATH = Path("01_parsing/outputs/missing_column_warning.txt")

EXPECTED_COLUMNS = [
    "order_id",
    "order_date",
    "customer_id",
    "customer_age",
    "total_amount",
    "notes"
]

def main():
    with open(DATASET_PATH, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)

    missing_columns = [col for col in EXPECTED_COLUMNS if col not in header]

    with open(OUTPUT_PATH, "w", encoding="utf-8") as out:
        out.write("MISSING COLUMN WARNING LOG \n\n")
        out.write(f"Dataset: {DATASET_PATH.name}\n")
        out.write(f"Header found: {header}\n")
        out.write(f"Expected columns: {EXPECTED_COLUMNS}\n\n")

        if missing_columns:
            out.write("WARNING: Missing expected columns detected\n")
            for col in missing_columns:
                out.write(f"- {col}\n")
        else:
            out.write("NO missing columns detected\n")

if __name__ == "__main__":
    main()
