from reproducibility.run_metadata_manager import save_run_metadata

INPUT = "data/raw/sample_input.csv"
OUTPUT = "data/processed/parsed_output.csv"

def main():
    # parsing logic here
    
    save_run_metadata(INPUT, OUTPUT)

if __name__ == "__main__":
    main()
