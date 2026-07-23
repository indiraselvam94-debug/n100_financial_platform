import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

DB_PATH = BASE_DIR / "database" / "n100.db"
OUTPUT_DIR = BASE_DIR / "reports" / "radar_charts"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

conn = sqlite3.connect(DB_PATH)

df = pd.read_sql("SELECT * FROM screener_data", conn)
df["composite_quality_score"] = (
    df["return_on_equity_pct"] * 0.40 +
    df["return_on_capital_employed_pct"] * 0.30 +
    df["net_profit_margin_pct"] * 0.30
)
print(df.columns.tolist())
peer = pd.read_sql("SELECT * FROM peer_percentiles", conn)

conn.close()

metrics = [
    "return_on_equity_pct",
    "return_on_capital_employed_pct",
    "net_profit_margin_pct",
    "debt_to_equity",
    "free_cash_flow_cr",
    "pat_cagr_5yr",
    "revenue_cagr_5yr",
    "composite_quality_score"
]

angles = np.linspace(0, 2 * np.pi, len(metrics), endpoint=False).tolist()
angles += angles[:1]

latest = df.sort_values("year").groupby("company_id").tail(1)

for _, company in latest.iterrows():

    values = [company[m] for m in metrics]
    values += values[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    ax.plot(angles, values, linewidth=2)
    ax.fill(angles, values, alpha=0.25)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels([
        "ROE",
        "ROCE",
        "NPM",
        "D/E",
        "FCF",
        "PAT CAGR",
        "REV CAGR",
        "Score"
    ])

    ax.set_title(company["company_name"])

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / f"{company['company_name']}_radar.png"
    )

    plt.close()

print(f"✓ {len(latest)} radar charts created")
print("Location:", OUTPUT_DIR)