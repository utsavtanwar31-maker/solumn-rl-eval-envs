# Data Exporter Formatting Task

Update the CSV export formatting logic in `exporter/csv_exporter.py` so that when `iso_format=True` is passed to `export_records()`, all datetime fields in the output records are formatted as ISO 8601 UTC strings (`YYYY-MM-DDTHH:MM:SSZ`).

Ensure all existing unit tests pass cleanly by running `pytest`.
