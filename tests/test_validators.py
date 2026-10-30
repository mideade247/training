import json

import pytest

from src.data_quality.validators import (
    validate_csv,
    validate_json,
)


def test_valid_csv(tmp_path):
    file = tmp_path / "valid.csv"

    file.write_text(
        "name,age\nAlice,25\nBob,30\n",
        encoding="utf-8",
    )

    result = validate_csv(file, ["name", "age"])

    assert result["valid"] is True
    assert result["row_count"] == 2


def test_missing_csv_column(tmp_path):
    file = tmp_path / "invalid.csv"

    file.write_text(
        "name\nAlice\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Missing required columns"):
        validate_csv(file, ["name", "age"])


def test_missing_csv_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        validate_csv(tmp_path / "missing.csv")


def test_valid_json(tmp_path):
    file = tmp_path / "data.json"

    file.write_text(
        json.dumps([{"name": "Alice"}, {"name": "Bob"}]),
        encoding="utf-8",
    )

    result = validate_json(file)

    assert result["valid"] is True
    assert result["record_count"] == 2


def test_invalid_json(tmp_path):
    file = tmp_path / "invalid.json"

    file.write_text("{invalid json}", encoding="utf-8")

    with pytest.raises(json.JSONDecodeError):
        validate_json(file)


def test_missing_json_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        validate_json(tmp_path / "missing.json")


def test_empty_csv_rejects_missing_header(tmp_path):
    file = tmp_path / "empty.csv"
    file.write_text("", encoding="utf-8")

    with pytest.raises(ValueError, match="CSV file has no header"):
        validate_csv(file)


def test_header_only_csv_has_no_records(tmp_path):
    file = tmp_path / "headers.csv"
    file.write_text("item,quantity\n", encoding="utf-8")

    assert validate_csv(file, ["item"]) == {
        "valid": True,
        "row_count": 0,
        "columns": ["item", "quantity"],
    }


def test_csv_supports_bom_and_quoted_fields(tmp_path):
    file = tmp_path / "quoted.csv"
    file.write_text('item,quantity\n"sample, item",2\n', encoding="utf-8-sig")

    assert validate_csv(file, ["item", "quantity"]) == {
        "valid": True,
        "row_count": 1,
        "columns": ["item", "quantity"],
    }


@pytest.mark.parametrize(
    ("data", "expected_count"),
    [([], 0), ({"item": "sample"}, 1)],
)
def test_json_record_counts(tmp_path, data, expected_count):
    file = tmp_path / "records.json"
    file.write_text(json.dumps(data), encoding="utf-8")

    assert validate_json(file) == {
        "valid": True,
        "record_count": expected_count,
    }
