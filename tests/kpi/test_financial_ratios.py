import unittest

from src.analytics.ratios import (
    net_profit_margin,
    return_on_equity,
    return_on_capital_employed,
    return_on_assets,
    check_opm_difference,
    debt_to_equity,
    high_leverage_flag,
    interest_coverage_ratio,
    icr_label,
    icr_warning_flag,
    net_debt,
    asset_turnover
)


class TestNetProfitMargin(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(net_profit_margin(200, 1000), 20.0)

    def test_zero_sales(self):
        self.assertIsNone(net_profit_margin(100, 0))


class TestReturnOnEquity(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(return_on_equity(200, 500, 500), 20.0)

    def test_negative_equity(self):
        self.assertIsNone(return_on_equity(200, -500, 400))


class TestReturnOnCapitalEmployed(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(
            return_on_capital_employed(300, 500, 500, 500),
            20.0
        )

    def test_zero_capital_employed(self):
        self.assertIsNone(
            return_on_capital_employed(300, 0, 0, 0)
        )


class TestReturnOnAssets(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(
            return_on_assets(200, 1000),
            20.0
        )

    def test_zero_assets(self):
        self.assertIsNone(
            return_on_assets(200, 0)
        )


class TestCheckOPMDifference(unittest.TestCase):

    def test_difference_greater_than_one(self):
        self.assertTrue(
            check_opm_difference(20.5, 19.0)
        )

    def test_difference_within_one(self):
        self.assertFalse(
            check_opm_difference(20.0, 19.5)
        )


class TestDebtToEquity(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(
            debt_to_equity(500, 250, 250),
            1.0
        )

    def test_debt_free_company(self):
        self.assertEqual(
            debt_to_equity(0, 500, 500),
            0
        )


class TestHighLeverageFlag(unittest.TestCase):

    def test_high_leverage_non_financial(self):
        self.assertTrue(
            high_leverage_flag(6.0, "Information Technology")
        )

    def test_financial_company(self):
        self.assertFalse(
            high_leverage_flag(10.0, "Financials")
        )


class TestInterestCoverageRatio(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(
            interest_coverage_ratio(500, 100, 100),
            6.0
        )

    def test_interest_zero(self):
        self.assertIsNone(
            interest_coverage_ratio(500, 100, 0)
        )


class TestICRLabel(unittest.TestCase):

    def test_debt_free_label(self):
        self.assertEqual(
            icr_label(None),
            "Debt Free"
        )

    def test_normal_label(self):
        self.assertEqual(
            icr_label(5.2),
            ""
        )


class TestICRWarningFlag(unittest.TestCase):

    def test_warning_required(self):
        self.assertTrue(
            icr_warning_flag(1.2)
        )

    def test_no_warning(self):
        self.assertFalse(
            icr_warning_flag(2.5)
        )


class TestNetDebt(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(
            net_debt(500, 200),
            300
        )

    def test_negative_net_debt(self):
        self.assertEqual(
            net_debt(100, 250),
            -150
        )


class TestAssetTurnover(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(
            asset_turnover(1000, 500),
            2.0
        )

    def test_zero_assets(self):
        self.assertIsNone(
            asset_turnover(1000, 0)
        )


if __name__ == "__main__":
    unittest.main()