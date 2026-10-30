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
