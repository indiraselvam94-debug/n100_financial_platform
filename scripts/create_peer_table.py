import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

DB_PATH = BASE_DIR / "database" / "n100.db"

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS peer_percentiles (

    company_id INTEGER,

    peer_group_name TEXT,

    metric TEXT,

    value REAL,

    percentile_rank REAL,

    year INTEGER

)
""")

conn.commit()
conn.close()

print("✓ peer_percentiles table created")