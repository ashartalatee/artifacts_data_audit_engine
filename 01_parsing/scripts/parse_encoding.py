from pathlib import Path

DATASET_PATH = Path("datasets/raw/raw_sales_export_latin1.csv")
OUTPUT_PATH = Path("01_parsing/outputs/detextion.txt")

def try_read(encoding_name):
    try:
        with open(DATASET_PATH, "r", encoding=encoding_name) as f:
            content = f.read()
        return True, content
    except UnicodeDecodeError as e:
        return False, str(e)

def main():
    encodings_to_test = ["utf-8", "latin-1"]

    with open(OUTPUT_PATH, "w", encoding="utf-8") as out:
        out.write("ENCODING DETECTION LOG \n\n")

        for enc in encodings_to_test:
            success, result = try_read(enc)
            out.write(f"Encoding tested: {enc}\n")
            out.write(f"Success: {success}\n")
            out.write(f"result:\n{result}\n")
            out.write("-" * 40 + "\n")

if __name__ == "__main__":
    main()