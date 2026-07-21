# N100 Financial Platform

## Sprint 2 – Financial Ratio Engine

This project is part of the Bluestock Fintech Internship.

### Features
- Generate sample financial data for 92 companies
- Create SQLite database
- Load financial datasets into database
- Calculate financial ratios
- Generate cash flow KPIs
- Generate capital allocation report
- Export results to CSV
- Unit tested with pytest

## Technologies Used
- Python
- Pandas
- SQLite
- SQLAlchemy
- Pytest

## Project Structure

```
n100_financial_platform/
│
├── data/
├── database/
├── output/
├── scripts/
├── sql/
├── src/
├── tests/
├── requirements.txt
└── README.md
```

## How to Run

Generate sample data:

```bash
python scripts/generate_sample_data.py
```

Create database:

```bash
python scripts/create_database.py
```

Load data:

```bash
python scripts/load_database.py
```

Run Financial Ratio Engine:

```bash
python scripts/run_ratio_engine.py
```

Run tests:

```bash
pytest -v
```

## Results

- 92 Companies
- 920 Financial Records
- 920 Financial Ratio Records
- 56/56 Unit Tests Passed

## Author

Indira P