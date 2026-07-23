import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

DB_PATH = BASE_DIR / "database" / "n100.db"
OUTPUT = BASE_DIR / "output" / "peer_comparison.xlsx"

conn = sqlite3.connect(DB_PATH)

peer = pd.read_sql(
    "SELECT * FROM peer_percentiles",
    conn
)

companies = pd.read_sql(
    "SELECT company_id, company_name FROM companies",
    conn
)

conn.close()

peer = peer.merge(companies, on="company_id")

writer = pd.ExcelWriter(
    OUTPUT,
    engine="openpyxl"
)

for group in sorted(peer["peer_group_name"].unique()):

    df = peer[
        peer["peer_group_name"] == group
    ]

    df.to_excel(
        writer,
        sheet_name=group[:31],
        index=False
    )

writer.close()

print("✓ peer_comparison.xlsx created")
print("Sheets:", peer["peer_group_name"].nunique())