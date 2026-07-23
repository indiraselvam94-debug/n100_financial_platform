import sqlite3
import pandas as pd
from pathlib import Path

from src.screener.engine import (
    load_config,
    load_data,
    quality_compounder,
    value_pick,
    growth_accelerator,
    dividend_champion,
    debt_free_blue_chip,
    turnaround_watch,
)

BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_FILE = BASE_DIR / "output" / "screener_output.xlsx"

config = load_config()
df = load_data()

screeners = {
    "Quality Compounder":
        quality_compounder(df, config["quality_compounder"]),

    "Value Pick":
        value_pick(df, config["value_pick"]),

    "Growth Accelerator":
        growth_accelerator(df, config["growth_accelerator"]),

    "Dividend Champion":
        dividend_champion(df, config["dividend_champion"]),

    "Debt Free Blue Chip":
        debt_free_blue_chip(df, config["debt_free_blue_chip"]),

    "Turnaround Watch":
        turnaround_watch(df, config["turnaround_watch"]),
}

with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:

    for sheet_name, data in screeners.items():

        data.to_excel(
            writer,
            sheet_name=sheet_name,
            index=False
        )

print("✓ Screener report created successfully")
print("Location:", OUTPUT_FILE)