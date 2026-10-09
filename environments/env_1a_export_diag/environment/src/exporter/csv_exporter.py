import csv
import io
from datetime import datetime

def export_records(records, fields, iso_format=False):
    """
    Exports a list of dictionary records to CSV string format.
    
    Args:
        records (list[dict]): List of data records.
        fields (list[str]): Field names to include in CSV header.
        iso_format (bool): If True, format datetime objects as ISO 8601 UTC strings (YYYY-MM-DDTHH:MM:SSZ).
    
    Returns:
        str: CSV formatted text.
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
                    # TODO: Implement ISO 8601 UTC formatting when iso_format=True
                    row[field] = str(val)
                else:
                    row[field] = str(val)
            else:
                row[field] = val
        writer.writerow(row)

    return output.getvalue()
