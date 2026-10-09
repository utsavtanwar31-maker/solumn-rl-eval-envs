import os
from datetime import datetime
import pytest
from exporter.csv_exporter import export_records

def test_default_export():
    records = [
        {"id": 1, "created_at": datetime(2026, 10, 10, 8, 30, 0)}
    ]
    output = export_records(records, fields=["id", "created_at"], iso_format=False)
    assert "1" in output
    assert "2026-10-10 08:30:00" in output

def test_iso_export():
    # Reads fixture log to verify format spec
    fixture_path = os.path.join(os.path.dirname(__file__), "fixtures", "sample_export_output.log")
    with open(fixture_path, "r") as f:
        fixture_content = f.read()

    records = [
        {"id": 101, "created_at": datetime(2026, 10, 10, 8, 30, 0)}
    ]
    output = export_records(records, fields=["id", "created_at"], iso_format=True)
    assert "2026-10-10T08:30:00Z" in output, f"Expected ISO format 2026-10-10T08:30:00Z in output. Reference log:\n{fixture_content}"
