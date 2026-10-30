# CSV & JSON Data Quality Checker

## Overview

CSV & JSON Data Quality Checker is a Python-based project designed to identify common data quality problems in structured datasets.

The project aims to help data analysts, developers, and small teams validate CSV and JSON files before using them for reporting, analysis, or downstream applications.

## Business Problem

Organisations frequently receive datasets containing:

- Missing or incomplete values
- Duplicate records
- Incorrect data types
- Inconsistent column names
- Unexpected schema changes
- Invalid field formats

These problems can produce inaccurate reports, disrupt data pipelines, and require time-consuming manual corrections.

This project aims to automate common data validation checks and provide clear, actionable reports.

## Current Project Status

The repository currently contains exploratory Python notebook work and initial project documentation.

The reusable validation engine, command-line interface, reporting functionality, and automated test suite are planned development tasks.

## Planned Features

### 1. File Validation
- Support CSV and JSON files.
- Detect malformed input files.
- Validate required columns.
- Check expected data types.

### 2. Data Quality Checks
- Identify missing values.
- Detect duplicate records.
- Validate field formats.
- Check configurable validation rules.

### 3. Reporting
- Generate validation summaries.
- Export results in JSON format.
- Generate human-readable HTML reports.
- Provide meaningful error messages.

### 4. Command-Line Interface
- Validate files directly from the terminal.
- Support configurable validation options.
- Return appropriate exit codes.

### 5. Automated Testing
- Unit tests for validation functions.
- Integration tests for file processing.
- Automated testing with GitHub Actions.

## Technology Stack

| Technology | Purpose |
|------------|---------|
| Python 3.11+ | Core application development |
| Pandas | Data processing and validation |
| Pydantic | Schema and input validation |
| Typer | Command-line interface |
| Pytest | Automated testing |
| JSON / CSV | Supported file formats |
| GitHub Actions | Continuous integration |

## Proposed Project Structure

```text
training/
├── src/
│   └── data_quality/
│       ├── __init__.py
│       ├── cli.py
│       ├── validators.py
│       ├── schemas.py
│       ├── rules.py
│       └── reports.py
├── tests/
│   ├── test_validators.py
│   ├── test_rules.py
│   └── test_cli.py
├── examples/
├── README.md
├── ROADMAP.md
├── LICENSE
└── pyproject.toml
```

## Getting Started

### Prerequisites

- Python 3.11 or later
- Git
- pip

### Clone the Repository

```bash
git clone https://github.com/mideade247/training.git
cd training
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it:

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### Install Dependencies

Once the application package and dependency configuration are implemented:

```bash
pip install -e .
```

## Planned Usage

The following command illustrates the intended CLI interface. It is not yet implemented.

```bash
data-quality validate examples/sample.csv
```

The tool will identify data quality issues and produce a validation report.

## Development Roadmap

| Phase | Task | Estimated Hours |
|-------|------|-----------------|
| 1 | Project restructuring and setup | 4 |
| 2 | CSV and JSON validation engine | 7 |
| 3 | Configurable validation rules | 7 |
| 4 | Command-line interface | 5 |
| 5 | Report generation | 5 |
| 6 | Automated tests and CI | 5 |
| 7 | Documentation | 2 |
| **Total** | | **35 hours** |

## Testing

Once the automated tests are implemented:

```bash
pytest
```

Testing will cover:

- Valid input files
- Missing columns
- Duplicate records
- Incorrect data types
- Malformed CSV and JSON files
- Invalid configurations

## Security and Privacy

- Use synthetic datasets for testing.
- Do not commit confidential information.
- Do not store passwords, API keys, or access tokens.
- Exclude sensitive files using `.gitignore`.

## Future Improvements

- Batch validation
- Custom validation rule templates
- Detailed HTML reports
- CI/CD integration
- Improved error reporting

## License

MIT

## Testing and Code Quality

The project uses Pytest for automated testing and Ruff
for Python linting.

### Running Tests

Install the development dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

Run the automated tests:

```bash
python -m pytest -v
```

### Linting

Run the Python lint checks:

```bash
ruff check src tests
```

### Continuous Integration

GitHub Actions runs automated tests and lint checks
when changes are pushed or pull requests are opened.

### Development Tasks

Future development is organised into bounded tasks
with defined objectives, scope and acceptance criteria.

Tests use synthetic data and local or mocked dependencies
where applicable.
