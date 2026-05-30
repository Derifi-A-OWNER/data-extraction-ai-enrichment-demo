# PDF / Document Data Extraction to Structured JSON Demo

This demo shows how unstructured document text can be converted into structured JSON and CSV outputs.

The example workflow:

1. Start with raw invoice or document text
2. Extract key fields such as vendor, invoice number, date, line items, subtotal, tax, and total
3. Normalize the extracted data
4. Export the result as JSON and CSV

## Example Use Cases

- Invoice extraction
- Quote or RFQ extraction
- Product sheet parsing
- Report-to-CSV conversion
- Document data normalization
- Structured JSON output for automation or database import

## Sample Files

This demo includes:

- `sample_document_raw.txt`
- `sample_extracted.json`
- `sample_extracted.csv`
- `demo_document_parser.py`

## Scope Boundaries

This demo focuses on structured extraction from provided document text.

For real client projects, OCR, scanned PDFs, complex tables, handwriting, or low-quality images may require separate review and scoping.
