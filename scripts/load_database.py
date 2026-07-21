import os
import sqlite3
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_PATH = os.path.join(BASE_DIR, "database", "n100.db")
RAW_DIR = os.path.join(BASE_DIR, "data", "raw")

conn = sqlite3.connect(DB_PATH)

files = {
    "companies": "companies.csv",
    "profit_loss": "profit_loss.csv",
    "balance_sheet": "balance_sheet.csv",
    "cash_flow": "cash_flow.csv"
}

for table, file in files.items():

    path = os.path.join(RAW_DIR, file)

    df = pd.read_csv(path)

    df.to_sql(table, conn, if_exists="replace", index=False)

    print(f"✓ Loaded {table} ({len(df)} rows)")

conn.commit()
conn.close()

print("\nAll datasets loaded successfully.")