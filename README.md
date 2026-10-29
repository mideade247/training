
# CSV and JSON Data Quality Checker

## Overview

A Python utility for validating CSV and JSON files and identifying common data quality issues before the data is used for reporting or analysis.

The project is designed for developers, analysts and small teams who need a repeatable way to inspect incoming data without manually checking every record.

## Business Problem

Data files frequently contain missing values, duplicate records, inconsistent schemas and invalid field formats. These issues can lead to incorrect reports and unnecessary manual cleaning.

This tool aims to make data validation repeatable, transparent and easier to troubleshoot.

## Planned Features

- Validate CSV and JSON file structures.
- Detect missing values and duplicate records.
- Check required columns and expected data types.
- Support configurable validation rules.
- Generate human-readable and machine-readable reports.
- Provide clear error messages and exit codes.
- Include automated tests and example datasets.

## Technology Stack

- Python
- Pandas
- Pydantic
- Pytest
- JSON and CSV

## Getting Started

Requirements: Python 3.11 or later.

Clone the repository and create a virtual environment:

    python -m venv .venv

Activate the environment and install dependencies:

    pip install -r requirements.txt

Run the available validation command:

    python -m src.cli --help

The command above will be available once the CLI is implemented.

## Testing

Run automated tests using:

    pytest

## Roadmap

See [ROADMAP.md](ROADMAP.md).

## Data and Privacy

Examples use synthetic data. Do not commit confidential files, credentials or real personal data.

## License

See the LICENSE file.
