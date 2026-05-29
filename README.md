# Data Extraction + AI Enrichment Demo

This repository demonstrates a simple data delivery workflow:

1. Extract structured data from a public source
2. Clean and normalize the data
3. Remove duplicates and formatting issues
4. Add optional AI enrichment such as category, tags, or summary
5. Export the final result as CSV and JSON

## Example Deliverables

A real client project may include:

* Python extraction script
* Clean CSV or JSON output
* Basic data cleaning
* Deduplication
* Optional AI categorization, tagging, or summarization
* Short README/run guide
* One bug-fix revision within the agreed scope

## Scope Boundaries

I work only with public and authorized data sources.

I do not provide:

* Captcha bypass
* Login-protected scraping
* Unauthorized private data extraction
* Spam lists
* Prohibited scraping
* Ongoing maintenance unless scoped separately

## Sample Files

This demo will include:

* `sample_raw.csv`
* `sample_clean.csv`
* `sample_enriched.csv`
* `sample_output.json`
## How to Run the Demo

This demo uses only Python standard library modules.

Run:

```bash
python demo_pipeline.py
Expected result:

Data Extraction + AI Enrichment Demo
Demo completed successfully.
Demo Workflow

The sample files show a simple delivery flow:

sample_raw.csv
→ sample_clean.csv
→ sample_enriched.csv
→ sample_output.json

This represents the typical client workflow:

Raw public source data
→ cleaned structured data
→ optional AI enrichment
→ CSV/JSON delivery
