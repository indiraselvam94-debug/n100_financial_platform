import sqlite3
import random
import pandas as pd

random.seed(42)

conn = sqlite3.connect("database/n100.db")

companies = pd.read_sql("SELECT * FROM companies", conn)
profit_loss = pd.read_sql("SELECT * FROM profit_loss", conn)
balance_sheet = pd.read_sql("SELECT * FROM balance_sheet", conn)
cash_flow = pd.read_sql("SELECT * FROM cash_flow", conn)
ratios = pd.read_sql("SELECT * FROM financial_ratios", conn)

df = (
    ratios
    .merge(companies, on="company_id")
    .merge(profit_loss, on=["company_id", "year"])
    .merge(balance_sheet, on=["company_id", "year"])
    .merge(cash_flow, on=["company_id", "year"])
)

# Generate additional fields needed for Sprint 3
df["revenue_cagr_5yr"] = [random.uniform(5, 25) for _ in range(len(df))]
df["pat_cagr_5yr"] = [random.uniform(5, 30) for _ in range(len(df))]
df["eps_cagr_5yr"] = [random.uniform(5, 30) for _ in range(len(df))]
df["pe_ratio"] = [random.uniform(8, 40) for _ in range(len(df))]
df["pb_ratio"] = [random.uniform(0.5, 8) for _ in range(len(df))]
df["dividend_yield"] = [random.uniform(0, 5) for _ in range(len(df))]
df["dividend_payout"] = [random.uniform(10, 90) for _ in range(len(df))]
df["market_cap"] = [random.uniform(5000, 500000) for _ in range(len(df))]

df.to_sql("screener_data", conn, if_exists="replace", index=False)

print("✓ screener_data table created")
print("Rows:", len(df))
print(df.head())

conn.close()