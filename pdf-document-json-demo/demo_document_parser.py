import csv
import json
import re
from pathlib import Path


RAW_FILE = Path("sample_document_raw.txt")
JSON_FILE = Path("sample_extracted.json")
CSV_FILE = Path("sample_extracted.csv")


def extract_field(pattern: str, text: str) -> str:
    match = re.search(pattern, text)
    return match.group(1).strip() if match else ""


def parse_invoice_text(text: str) -> dict:
    vendor = extract_field(r"Vendor:\s*(.+)", text)
    invoice_number = extract_field(r"Invoice Number:\s*(.+)", text)
    invoice_date = extract_field(r"Invoice Date:\s*(.+)", text)
    due_date = extract_field(r"Due Date:\s*(.+)", text)
    subtotal = float(extract_field(r"Subtotal:\s*([\d.]+)", text) or 0)
    tax = float(extract_field(r"Tax:\s*([\d.]+)", text) or 0)
    total = float(extract_field(r"Total:\s*([\d.]+)", text) or 0)
    payment_terms = extract_field(r"Payment Terms:\s*(.+)", text)
    notes = extract_field(r"Notes:\s*(.+)", text)

    bill_to_match = re.search(
        r"Bill To:\s*\n(.+)\n(.+)\n(.+)",
        text,
        flags=re.MULTILINE,
    )

    bill_to = {
        "name": bill_to_match.group(1).strip() if bill_to_match else "",
        "address": (
            f"{bill_to_match.group(2).strip()}, {bill_to_match.group(3).strip()}"
            if bill_to_match
            else ""
        ),
    }

    line_items = []
    item_pattern = re.compile(
        r"\d+\.\s*(.*?)\s*-\s*Quantity:\s*(\d+)\s*-\s*Unit Price:\s*([\d.]+)\s*USD\s*-\s*Line Total:\s*([\d.]+)\s*USD"
    )

    for item, quantity, unit_price, line_total in item_pattern.findall(text):
        line_items.append(
            {
                "item": item.strip(),
                "quantity": int(quantity),
                "unit_price": float(unit_price),
                "line_total": float(line_total),
            }
        )

    return {
        "document_type": "invoice",
        "vendor": {"name": vendor},
        "invoice": {
            "invoice_number": invoice_number,
            "invoice_date": invoice_date,
            "due_date": due_date,
            "payment_terms": payment_terms,
        },
        "bill_to": bill_to,
        "currency": "USD",
        "line_items": line_items,
        "totals": {
            "subtotal": subtotal,
            "tax": tax,
            "total": total,
        },
        "notes": notes,
    }


def write_json(data: dict, path: Path) -> None:
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def write_csv(data: dict, path: Path) -> None:
    fieldnames = [
        "document_type",
        "vendor_name",
        "invoice_number",
        "invoice_date",
        "due_date",
        "bill_to_name",
        "currency",
        "item",
        "quantity",
        "unit_price",
        "line_total",
        "subtotal",
        "tax",
        "total",
    ]

    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for item in data["line_items"]:
            writer.writerow(
                {
                    "document_type": data["document_type"],
                    "vendor_name": data["vendor"]["name"],
                    "invoice_number": data["invoice"]["invoice_number"],
                    "invoice_date": data["invoice"]["invoice_date"],
                    "due_date": data["invoice"]["due_date"],
                    "bill_to_name": data["bill_to"]["name"],
                    "currency": data["currency"],
                    "item": item["item"],
                    "quantity": item["quantity"],
                    "unit_price": item["unit_price"],
                    "line_total": item["line_total"],
                    "subtotal": data["totals"]["subtotal"],
                    "tax": data["totals"]["tax"],
                    "total": data["totals"]["total"],
                }
            )


def main() -> None:
    if not RAW_FILE.exists():
        raise FileNotFoundError(f"Missing input file: {RAW_FILE}")

    raw_text = RAW_FILE.read_text(encoding="utf-8")
    parsed = parse_invoice_text(raw_text)

    write_json(parsed, JSON_FILE)
    write_csv(parsed, CSV_FILE)

    print("Document extraction demo completed successfully.")
    print(f"JSON output: {JSON_FILE}")
    print(f"CSV output: {CSV_FILE}")


if __name__ == "__main__":
    main()
