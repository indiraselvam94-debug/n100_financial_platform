import sqlite3
import yaml
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

DB_PATH = BASE_DIR / "database" / "n100.db"
CONFIG_PATH = BASE_DIR / "config" / "screener_config.yaml"


def load_config():
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)


def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM screener_data", conn)
    conn.close()
    return df


def quality_compounder(df, cfg):

    result = df[
    (df["return_on_equity_pct"] >= cfg["roe_min"]) &
    (df["debt_to_equity"] <= cfg["debt_to_equity_max"]) &
    (df["free_cash_flow_cr"] >= cfg["free_cash_flow_min"]) &
    (df["revenue_cagr_5yr"] >= cfg["revenue_cagr_min"])
].copy()

    result["composite_quality_score"] = (
        result["return_on_equity_pct"] * 0.40 +
        result["return_on_capital_employed_pct"] * 0.30 +
        result["net_profit_margin_pct"] * 0.30
    )

    result = result.sort_values(
        "composite_quality_score",
        ascending=False
    )

    return result


def value_pick(df, cfg):
    
    result = df[
        (df["pe_ratio"] <= cfg["pe_max"]) &
        (df["pb_ratio"] <= cfg["pb_max"]) &
        (df["debt_to_equity"] <= cfg["debt_to_equity_max"]) &
        (df["dividend_yield"] >= cfg["dividend_yield_min"])
    ].copy()

    result["composite_quality_score"] = (
        result["return_on_equity_pct"] * 0.40 +
        result["return_on_capital_employed_pct"] * 0.30 +
        result["net_profit_margin_pct"] * 0.30
    )

    result = result.sort_values(
        "composite_quality_score",
        ascending=False
    )

    return result

def growth_accelerator(df, cfg):
    
    result = df[
        (df["pat_cagr_5yr"] >= cfg["pat_cagr_min"]) &
        (df["revenue_cagr_5yr"] >= cfg["revenue_cagr_min"]) &
        (df["debt_to_equity"] <= cfg["debt_to_equity_max"])
    ].copy()

    result["composite_quality_score"] = (
        result["return_on_equity_pct"] * 0.40 +
        result["return_on_capital_employed_pct"] * 0.30 +
        result["net_profit_margin_pct"] * 0.30
    )

    result = result.sort_values(
        "composite_quality_score",
        ascending=False
    )

    return result

def dividend_champion(df, cfg):
    
    result = df[
        (df["dividend_yield"] >= cfg["dividend_yield_min"]) &
        (df["dividend_payout"] <= cfg["dividend_payout_max"]) &
        (df["free_cash_flow_cr"] >= cfg["free_cash_flow_min"])
    ].copy()

    result["composite_quality_score"] = (
        result["return_on_equity_pct"] * 0.40 +
        result["return_on_capital_employed_pct"] * 0.30 +
        result["net_profit_margin_pct"] * 0.30
    )

    result = result.sort_values(
        "composite_quality_score",
        ascending=False
    )

    return result

def debt_free_blue_chip(df, cfg):
    
    result = df[
        (df["debt_to_equity"] <= cfg["debt_to_equity_max"]) &
        (df["return_on_equity_pct"] >= cfg["roe_min"]) &
        (df["sales"] >= cfg["sales_min"])
    ].copy()

    result["composite_quality_score"] = (
        result["return_on_equity_pct"] * 0.40 +
        result["return_on_capital_employed_pct"] * 0.30 +
        result["net_profit_margin_pct"] * 0.30
    )

    result = result.sort_values(
        "composite_quality_score",
        ascending=False
    )

    return result

def turnaround_watch(df, cfg):
    
    result = df[
        (df["revenue_cagr_5yr"] >= cfg["revenue_cagr_min"]) &
        (df["free_cash_flow_cr"] >= cfg["free_cash_flow_min"])
    ].copy()

    result["composite_quality_score"] = (
        result["return_on_equity_pct"] * 0.40 +
        result["return_on_capital_employed_pct"] * 0.30 +
        result["net_profit_margin_pct"] * 0.30
    )

    result = result.sort_values(
        "composite_quality_score",
        ascending=False
    )

    return result

if __name__ == "__main__":
    
    config = load_config()

    df = load_data()

    screened = turnaround_watch(
    df,
    config["turnaround_watch"]
)

    print("Companies Found:", len(screened))

    print(
        screened[
            [
                "company_name",
                "return_on_equity_pct",
                "debt_to_equity",
                "free_cash_flow_cr",
                "revenue_cagr_5yr",
                "composite_quality_score",
            ]
        ].head(10)
    )