import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_FOLDER = os.path.join(BASE_DIR, "database")
os.makedirs(DB_FOLDER, exist_ok=True)

DB_PATH = os.path.join(DB_FOLDER, "n100.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS companies(
company_id INTEGER PRIMARY KEY,
company_name TEXT,
ticker TEXT,
broad_sector TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS profit_loss(
company_id INTEGER,
year INTEGER,
sales REAL,
operating_profit REAL,
net_profit REAL,
other_income REAL,
interest REAL,
ebit REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS balance_sheet(
company_id INTEGER,
year INTEGER,
equity_capital REAL,
reserves REAL,
borrowings REAL,
total_assets REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS cash_flow(
company_id INTEGER,
year INTEGER,
operating_activity REAL,
investing_activity REAL,
financing_activity REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS financial_ratios(
company_id INTEGER,
year INTEGER,
net_profit_margin_pct REAL,
operating_profit_margin_pct REAL,
return_on_equity_pct REAL,
return_on_capital_employed_pct REAL,
return_on_assets_pct REAL,
debt_to_equity REAL,
interest_coverage REAL,
asset_turnover REAL,
free_cash_flow_cr REAL,
cfo_quality_ratio REAL,
capex_intensity_pct REAL,
fcf_conversion_pct REAL
)
""")

conn.commit()
conn.close()

print("Database created successfully.")