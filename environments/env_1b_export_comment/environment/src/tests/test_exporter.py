from datetime import datetime
from exporter.csv_exporter import export_records

def test_default_export():
    records = [{"id": 1, "created_at": datetime(2026, 10, 10, 8, 30, 0)}]
    output = export_records(records, fields=["id", "created_at"], iso_format=False)
    assert "1" in output
    assert "2026-10-10 08:30:00" in output

def test_iso_export():
    records = [{"id": 101, "created_at": datetime(2026, 10, 10, 8, 30, 0)}]
    output = export_records(records, fields=["id", "created_at"], iso_format=True)
    assert "2026-10-10T08:30:00Z" in output
