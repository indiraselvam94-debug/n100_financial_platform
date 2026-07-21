def free_cash_flow(operating_activity, investing_activity):
    """
    Calculate Free Cash Flow (FCF).

    Formula:
        FCF = Operating Activity + Investing Activity

    Returns:
        float : Free Cash Flow
    """

    return operating_activity + investing_activity

def cfo_quality_score(cfo, pat):
    """
    Calculate CFO Quality Score.

    Formula:
        CFO / PAT

    Returns:
        (ratio, label)
    """

    if pat == 0:
        return None, None

    ratio = cfo / pat

    if ratio > 1.0:
        label = "High Quality"
    elif ratio >= 0.5:
        label = "Moderate"
    else:
        label = "Accrual Risk"

    return round(ratio, 2), label


def capex_intensity(investing_activity, sales):
    """
    Calculate CapEx Intensity.

    Formula:
        abs(Investing Activity) / Sales * 100

    Returns:
        (percentage, label)
    """

    if sales == 0:
        return None, None

    percentage = (abs(investing_activity) / sales) * 100

    if percentage < 3:
        label = "Asset Light"
    elif percentage <= 8:
        label = "Moderate"
    else:
        label = "Capital Intensive"

    return round(percentage, 2), label


def fcf_conversion_rate(free_cash_flow, operating_profit):
    """
    Calculate FCF Conversion Rate.

    Formula:
        FCF / Operating Profit * 100

    Returns:
        (percentage, label)
    """

    if operating_profit == 0:
        return None, None

    percentage = (free_cash_flow / operating_profit) * 100

    if percentage >= 100:
        label = "Excellent"
    elif percentage >= 75:
        label = "Good"
    elif percentage >= 50:
        label = "Average"
    else:
        label = "Weak"

    return round(percentage, 2), label


def capital_allocation_pattern(cfo, cfi, cff):
    """
    Classify capital allocation pattern based on the signs of
    CFO (Operating), CFI (Investing), and CFF (Financing).

    Returns:
        str : Pattern label
    """

    signs = (
        "+" if cfo >= 0 else "-",
        "+" if cfi >= 0 else "-",
        "+" if cff >= 0 else "-"
    )

    patterns = {
        ("+", "-", "-"): "Reinvestor",
        ("+", "+", "-"): "Liquidating Assets",
        ("-", "+", "+"): "Distress Signal",
        ("-", "-", "+"): "Growth Funded by Debt",
        ("+", "+", "+"): "Cash Accumulator",
        ("-", "-", "-"): "Pre-Revenue",
        ("+", "-", "+"): "Mixed"
    }

    return patterns.get(signs, "Unknown")