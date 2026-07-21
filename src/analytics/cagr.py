def calculate_cagr(start_value, end_value, years):
    """
    Calculate Compound Annual Growth Rate (CAGR).

    Returns:
        (cagr_value, flag)
    """

    if years < 1:
        return None, "INSUFFICIENT"

    if start_value == 0:
        return None, "ZERO_BASE"

    # Positive -> Negative
    if start_value > 0 and end_value < 0:
        return None, "DECLINE_TO_LOSS"

    # Negative -> Positive
    if start_value < 0 and end_value > 0:
        return None, "TURNAROUND"

    # Negative -> Negative
    if start_value < 0 and end_value < 0:
        return None, "BOTH_NEGATIVE"

    cagr = (((end_value / start_value) ** (1 / years)) - 1) * 100

    return round(cagr, 2), None



def revenue_cagr(start_revenue, end_revenue, years):
    """
    Calculate Revenue CAGR.

    Returns:
        (cagr_value, flag)
    """

    return calculate_cagr(start_revenue, end_revenue, years)



def pat_cagr(start_pat, end_pat, years):
    """
    Calculate PAT CAGR.

    Returns:
        (cagr_value, flag)
    """

    return calculate_cagr(start_pat, end_pat, years)


def eps_cagr(start_eps, end_eps, years):
    """
    Calculate EPS CAGR.

    Returns:
        (cagr_value, flag)
    """

    return calculate_cagr(start_eps, end_eps, years)


