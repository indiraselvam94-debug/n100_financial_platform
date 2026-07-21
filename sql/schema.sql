CREATE TABLE IF NOT EXISTS companies (
    company_id INTEGER PRIMARY KEY,
    company_name TEXT,
    ticker TEXT,
    broad_sector TEXT
);

CREATE TABLE IF NOT EXISTS financial_ratios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
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
    cfo_quality_label TEXT,
    capex_intensity_pct REAL,
    capex_intensity_label TEXT,
    fcf_conversion_pct REAL,
    fcf_conversion_label TEXT
);