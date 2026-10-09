import csv
import io
import json
import os
from datetime import datetime

# Load exporter configuration
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config", "exporter_config.json")
try:
    with open(CONFIG_PATH, "r") as f:
        CONFIG = json.load(f)
except Exception:
    CONFIG = {}

def export_records(records, fields, iso_format=False):
    """
    Exports a list of dictionary records to CSV string format.
    """
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=fields)
    writer.writeheader()

    for record in records:
        row = {}
        for field in fields:
            val = record.get(field, "")
            if isinstance(val, datetime):
                if iso_format:
                    row[field] = str(val)
                else:
                    row[field] = str(val)
            else:
                row[field] = val
        writer.writerow(row)

    return output.getvalue()
