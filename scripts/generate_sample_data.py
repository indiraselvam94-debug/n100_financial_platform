"""
Generate Sample N100 Financial Data
-----------------------------------
Creates realistic financial datasets for 92 companies
from 2016 to 2025.

Outputs:
    data/raw/companies.csv
    data/raw/profit_loss.csv
    data/raw/balance_sheet.csv
    data/raw/cash_flow.csv
"""

import os
import random
import pandas as pd

random.seed(42)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DIR = os.path.join(BASE_DIR, "data", "raw")

os.makedirs(RAW_DIR, exist_ok=True)

YEARS = list(range(2016, 2026))

SECTORS = [
    "Financials",
    "Information Technology",
    "Healthcare",
    "Industrials",
    "Consumer Staples",
    "Consumer Discretionary",
    "Energy",
    "Utilities",
    "Materials",
    "Telecommunication",
]

companies = []

for i in range(1, 93):

    companies.append({

        "company_id": i,

        "company_name": f"Company {i}",

        "ticker": f"CMP{i:03}",

        "broad_sector": random.choice(SECTORS)

    })

companies_df = pd.DataFrame(companies)

# Save companies dataset
companies_df.to_csv(
    os.path.join(RAW_DIR, "companies.csv"),
    index=False
)

print("✓ companies.csv created")

# -----------------------------
# Generate Profit & Loss data
# -----------------------------

profit_loss = []

for company in companies:

    base_sales = random.randint(500, 5000)

    for year in YEARS:

        growth = random.uniform(0.90, 1.20)

        sales = round(base_sales * growth, 2)

        operating_profit = round(sales * random.uniform(0.10, 0.30), 2)

        net_profit = round(operating_profit * random.uniform(0.60, 0.90), 2)

        profit_loss.append({
            "company_id": company["company_id"],
            "year": year,
            "sales": sales,
            "operating_profit": operating_profit,
            "net_profit": net_profit,
            "other_income": round(random.uniform(5,100),2),
            "interest": round(random.uniform(2,50),2),
            "ebit": round(operating_profit + random.uniform(5,50),2)
        })

profit_loss_df = pd.DataFrame(profit_loss)

profit_loss_df.to_csv(
    os.path.join(RAW_DIR, "profit_loss.csv"),
    index=False
)

print("✓ profit_loss.csv created")


# -----------------------------
# Generate Balance Sheet data
# -----------------------------

balance_sheet = []

for company in companies:

    equity = random.randint(300, 3000)

    for year in YEARS:

        reserves = random.randint(200, 5000)
        borrowings = random.randint(0, 4000)
        investments = random.randint(50, 800)
        total_assets = equity + reserves + borrowings + random.randint(500, 5000)

        balance_sheet.append({
            "company_id": company["company_id"],
            "year": year,
            "equity_capital": equity,
            "reserves": reserves,
            "borrowings": borrowings,
            "investments": investments,
            "total_assets": total_assets
        })

balance_sheet_df = pd.DataFrame(balance_sheet)

balance_sheet_df.to_csv(
    os.path.join(RAW_DIR, "balance_sheet.csv"),
    index=False
)

print("✓ balance_sheet.csv created")


# -----------------------------
# Generate Cash Flow data
# -----------------------------

cash_flow = []

for company in companies:

    for year in YEARS:

        operating_activity = random.randint(100, 3000)
        investing_activity = -random.randint(50, 2000)
        financing_activity = random.randint(-1000, 1000)

        cash_flow.append({
            "company_id": company["company_id"],
            "year": year,
            "operating_activity": operating_activity,
            "investing_activity": investing_activity,
            "financing_activity": financing_activity
        })

cash_flow_df = pd.DataFrame(cash_flow)

cash_flow_df.to_csv(
    os.path.join(RAW_DIR, "cash_flow.csv"),
    index=False
)

print("✓ cash_flow.csv created")