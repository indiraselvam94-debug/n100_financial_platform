import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

DB_PATH = BASE_DIR / "database" / "n100.db"
PEER_FILE = BASE_DIR / "data" / "reference" / "peer_groups.csv"

METRICS = [
    "return_on_equity_pct",
    "return_on_capital_employed_pct",
    "net_profit_margin_pct",
    "debt_to_equity",
    "free_cash_flow_cr",
    "pat_cagr_5yr",
    "revenue_cagr_5yr",
    "eps_cagr_5yr",
    "interest_coverage",
    "asset_turnover"
]


def load_data():
    conn = sqlite3.connect(DB_PATH)

    ratios = pd.read_sql(
        "SELECT * FROM screener_data",
        conn
    )

    conn.close()

    peers = pd.read_csv(PEER_FILE)

    df = ratios.merge(peers, on=["company_id", "company_name"])

    return df


def calculate_percentiles(df):

    rows = []

    for peer_group in df["peer_group_name"].unique():

        peer_df = df[df["peer_group_name"] == peer_group]

        for metric in METRICS:

            ascending = metric == "debt_to_equity"

            ranks = peer_df[metric].rank(
                pct=True,
                ascending=ascending
            )

            if metric == "debt_to_equity":
                ranks = 1 - ranks

            temp = peer_df[
                ["company_id",
                 "peer_group_name",
                 "year"]
            ].copy()

            temp["metric"] = metric
            temp["value"] = peer_df[metric]
            temp["percentile_rank"] = ranks

            rows.append(temp)

    return pd.concat(rows, ignore_index=True)


def save_database(df):

    conn = sqlite3.connect(DB_PATH)

    df.to_sql(
        "peer_percentiles",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()


if __name__ == "__main__":

    df = load_data()

    result = calculate_percentiles(df)

    save_database(result)

    print("✓ Peer percentile table populated")
    print(result.head())