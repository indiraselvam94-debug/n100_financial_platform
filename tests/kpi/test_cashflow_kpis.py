import unittest

from src.analytics.cashflow_kpis import (
    free_cash_flow,
    cfo_quality_score,
    capex_intensity,
    fcf_conversion_rate,
    capital_allocation_pattern
)


class TestFreeCashFlow(unittest.TestCase):

    def test_positive_fcf(self):
        self.assertEqual(free_cash_flow(500, -200), 300)

    def test_negative_fcf(self):
        self.assertEqual(free_cash_flow(100, -300), -200)


class TestCFOQualityScore(unittest.TestCase):

    def test_high_quality(self):
        ratio, label = cfo_quality_score(120, 100)
        self.assertEqual(ratio, 1.2)
        self.assertEqual(label, "High Quality")

    def test_moderate(self):
        ratio, label = cfo_quality_score(75, 100)
        self.assertEqual(ratio, 0.75)
        self.assertEqual(label, "Moderate")

    def test_accrual_risk(self):
        ratio, label = cfo_quality_score(30, 100)
        self.assertEqual(ratio, 0.3)
        self.assertEqual(label, "Accrual Risk")

    def test_pat_zero(self):
        ratio, label = cfo_quality_score(100, 0)
        self.assertIsNone(ratio)
        self.assertIsNone(label)


class TestCapExIntensity(unittest.TestCase):

    def test_asset_light(self):
        percentage, label = capex_intensity(-20, 1000)
        self.assertEqual(percentage, 2.0)
        self.assertEqual(label, "Asset Light")

    def test_moderate(self):
        percentage, label = capex_intensity(-50, 1000)
        self.assertEqual(percentage, 5.0)
        self.assertEqual(label, "Moderate")

    def test_capital_intensive(self):
        percentage, label = capex_intensity(-120, 1000)
        self.assertEqual(percentage, 12.0)
        self.assertEqual(label, "Capital Intensive")

    def test_zero_sales(self):
        percentage, label = capex_intensity(-50, 0)
        self.assertIsNone(percentage)
        self.assertIsNone(label)


class TestFCFConversionRate(unittest.TestCase):

    def test_excellent(self):
        percentage, label = fcf_conversion_rate(120, 100)
        self.assertEqual(percentage, 120.0)
        self.assertEqual(label, "Excellent")

    def test_good(self):
        percentage, label = fcf_conversion_rate(80, 100)
        self.assertEqual(percentage, 80.0)
        self.assertEqual(label, "Good")

    def test_average(self):
        percentage, label = fcf_conversion_rate(60, 100)
        self.assertEqual(percentage, 60.0)
        self.assertEqual(label, "Average")

    def test_weak(self):
        percentage, label = fcf_conversion_rate(30, 100)
        self.assertEqual(percentage, 30.0)
        self.assertEqual(label, "Weak")

    def test_zero_operating_profit(self):
        percentage, label = fcf_conversion_rate(100, 0)
        self.assertIsNone(percentage)
        self.assertIsNone(label)


class TestCapitalAllocationPattern(unittest.TestCase):

    def test_reinvestor(self):
        self.assertEqual(
            capital_allocation_pattern(100, -50, -20),
            "Reinvestor"
        )

    def test_liquidating_assets(self):
        self.assertEqual(
            capital_allocation_pattern(100, 50, -20),
            "Liquidating Assets"
        )

    def test_distress_signal(self):
        self.assertEqual(
            capital_allocation_pattern(-100, 50, 20),
            "Distress Signal"
        )

    def test_growth_funded_by_debt(self):
        self.assertEqual(
            capital_allocation_pattern(-100, -50, 20),
            "Growth Funded by Debt"
        )

    def test_cash_accumulator(self):
        self.assertEqual(
            capital_allocation_pattern(100, 50, 20),
            "Cash Accumulator"
        )

    def test_pre_revenue(self):
        self.assertEqual(
            capital_allocation_pattern(-100, -50, -20),
            "Pre-Revenue"
        )

    def test_mixed(self):
        self.assertEqual(
            capital_allocation_pattern(100, -50, 20),
            "Mixed"
        )


if __name__ == "__main__":
    unittest.main()