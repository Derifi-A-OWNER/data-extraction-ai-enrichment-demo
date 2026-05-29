import csv
import json
from pathlib import Path


RAW_FILE = Path("sample_raw.csv")
CLEAN_FILE = Path("sample_clean.csv")
ENRICHED_FILE = Path("sample_enriched.csv")
JSON_FILE = Path("sample_output.json")


def preview_csv(path: Path, max_rows: int = 3) -> None:
    print(f"\nPreview: {path.name}")
    print("-" * 60)

    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for index, row in enumerate(reader):
            if index >= max_rows:
                break
            print(row)


def preview_json(path: Path, max_items: int = 2) -> None:
    print(f"\nPreview: {path.name}")
    print("-" * 60)

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    for item in data[:max_items]:
        print(json.dumps(item, indent=2, ensure_ascii=False))


def main() -> None:
    print("Data Extraction + AI Enrichment Demo")
    print("=" * 60)

    for file_path in [RAW_FILE, CLEAN_FILE, ENRICHED_FILE, JSON_FILE]:
        if not file_path.exists():
            raise FileNotFoundError(f"Missing required file: {file_path}")

    preview_csv(RAW_FILE)
    preview_csv(CLEAN_FILE)
    preview_csv(ENRICHED_FILE)
    preview_json(JSON_FILE)

    print("\nDemo completed successfully.")


if __name__ == "__main__":
    main()
