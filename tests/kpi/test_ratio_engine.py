import unittest

from src.analytics.ratio_engine import calculate_financial_ratios


class TestRatioEngine(unittest.TestCase):

    def test_calculate_financial_ratios(self):
        sample_data = {
            "net_profit": 100,
            "sales": 1000,
            "operating_profit": 150,
            "equity_capital": 200,
            "reserves": 300,
            "ebit": 180,
            "borrowings": 100,
            "total_assets": 800,
            "other_income": 20,
            "interest": 10,
            "operating_activity": 250,
            "investing_activity": -100,
        }

        results = calculate_financial_ratios(sample_data)

        self.assertIn("net_profit_margin_pct", results)
        self.assertIn("return_on_equity_pct", results)
        self.assertIn("debt_to_equity", results)
        self.assertIn("free_cash_flow_cr", results)
        self.assertIn("fcf_conversion_pct", results)


if __name__ == "__main__":
    unittest.main()