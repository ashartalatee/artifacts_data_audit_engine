import csv
from pathlib import Path

DATASET_PATH = Path("datasets/raw/raw_sales_export.csv")
OUTPUT_PATH = Path("01_parsing/outputs/type_mismatch_report.txt")

EXPECTED_TYPES ={
    "order_id": int,
    "order_date": "date",
    "customer_id": str,
    "customer_age": int,
    "total_amount": float,
    "payment_status": str,
    "notes": str,
}

def is_int(value):
    try:
        int(value)
        return True
    except:
        return False

def is_float(value):
    try:
        float(value)
        return True
    except:
        return False

def main():
    with open(DATASET_PATH, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    mismatch_log = []

    for i, row in enumerate(rows, start=1):
        for col, expected in EXPECTED_TYPES.items():
            value = row.get(col)

            if expected == int and not is_int(value):
                mismatch_log.append(
                    f"Row {i} | Column '{col}' | Expected int | Got '{value}'"
                )
            
            elif expected == float and not is_float(value):
                mismatch_log.append(
                    f"Row {i} | Column '{col}' | Expected float | Got '{value}'"
                )

    with open(OUTPUT_PATH, "w", encoding="utf-8") as out:
        out.write("TYPE MISMATCH REPORT \n\n")
        out.write(f"Total rows checked: {len(rows)}\n")
        out.write(f"Total mismatches found: {len(mismatch_log)}\n\n")

        for m in mismatch_log:
            out.write(m + "\n")

if __name__ == "__main__":
    main()
