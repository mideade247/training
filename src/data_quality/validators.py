import csv
import json
from pathlib import Path


def validate_csv(file_path, required_columns=None):
    required_columns = required_columns or []
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    with path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames:
            raise ValueError("CSV file has no header")

        missing_columns = [
            column
            for column in required_columns
            if column not in reader.fieldnames
        ]

        if missing_columns:
            raise ValueError(
                f"Missing required columns: {missing_columns}"
            )

        rows = list(reader)

        return {
            "valid": True,
            "row_count": len(rows),
            "columns": reader.fieldnames,
        }


def validate_json(file_path):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return {
        "valid": True,
        "record_count": len(data) if isinstance(data, list) else 1,
    }
