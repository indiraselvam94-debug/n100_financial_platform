"""
Ratio Engine

Runs all financial ratio calculations and prepares
records for insertion into the financial_ratios table.
"""


from src.analytics.ratios import (
    net_profit_margin,
    operating_profit_margin,
    return_on_equity,
    return_on_capital_employed,
    return_on_assets,
    debt_to_equity,
    interest_coverage_ratio,
    asset_turnover,
)

from src.analytics.cashflow_kpis import (
    free_cash_flow,
    cfo_quality_score,
    capex_intensity,
    fcf_conversion_rate,
)


def calculate_financial_ratios(data):
    """
    Calculate all financial ratios for one company-year.

    Parameters:
        data (dict): Financial values for one company-year.

    Returns:
        dict: Calculated KPI values.
    """

    results = {}

    results["net_profit_margin_pct"] = net_profit_margin(
        data["net_profit"],
        data["sales"]
    )

    results["operating_profit_margin_pct"] = operating_profit_margin(
        data["operating_profit"],
        data["sales"]
    )

    results["return_on_equity_pct"] = return_on_equity(
        data["net_profit"],
        data["equity_capital"],
        data["reserves"]
    )

    results["return_on_capital_employed_pct"] = return_on_capital_employed(
        data["ebit"],
        data["equity_capital"],
        data["reserves"],
        data["borrowings"]
    )

    results["return_on_assets_pct"] = return_on_assets(
        data["net_profit"],
        data["total_assets"]
    )

    results["debt_to_equity"] = debt_to_equity(
        data["borrowings"],
        data["equity_capital"],
        data["reserves"]
    )

    results["interest_coverage"] = interest_coverage_ratio(
        data["operating_profit"],
        data["other_income"],
        data["interest"]
    )

    results["asset_turnover"] = asset_turnover(
        data["sales"],
        data["total_assets"]
    )

    fcf = free_cash_flow(
        data["operating_activity"],
        data["investing_activity"]
    )

    results["free_cash_flow_cr"] = fcf

    cfo_ratio, cfo_label = cfo_quality_score(
        data["operating_activity"],
        data["net_profit"]
    )

    results["cfo_quality_ratio"] = cfo_ratio
    results["cfo_quality_label"] = cfo_label

    capex_pct, capex_label = capex_intensity(
        data["investing_activity"],
        data["sales"]
    )

    results["capex_intensity_pct"] = capex_pct
    results["capex_intensity_label"] = capex_label

    fcf_pct, fcf_label = fcf_conversion_rate(
        fcf,
        data["operating_profit"]
    )

    results["fcf_conversion_pct"] = fcf_pct
    results["fcf_conversion_label"] = fcf_label

    return results