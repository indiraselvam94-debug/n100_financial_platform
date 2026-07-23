import sqlite3
import pandas as pd
import random
from pathlib import Path

random.seed(42)

BASE_DIR = Path(__file__).resolve().parents[1]

DB_PATH = BASE_DIR / "database" / "n100.db"
OUTPUT = BASE_DIR / "data" / "reference" / "peer_groups.csv"

peer_groups = [
    "IT Services",
    "Banks",
    "FMCG",
    "Pharma",
    "Auto",
    "Energy",
    "Metals",
    "Telecom",
    "Infrastructure",
    "Capital Goods",
    "Consumer"
]

conn = sqlite3.connect(DB_PATH)

companies = pd.read_sql(
    "SELECT company_id, company_name FROM companies",
    conn
)

conn.close()

companies["peer_group_name"] = [
    random.choice(peer_groups)
    for _ in range(len(companies))
]

companies.to_csv(
    OUTPUT,
    index=False
)

print("✓ peer_groups.csv created")
print(companies.head())