import unittest

from src.analytics.cagr import (
    calculate_cagr,
    revenue_cagr,
    pat_cagr,
    eps_cagr
)


class TestCAGR(unittest.TestCase):

    def test_normal_cagr(self):
        value, flag = calculate_cagr(100, 200, 5)
        self.assertIsNone(flag)
        self.assertAlmostEqual(value, 14.87, places=2)

    def test_decline_to_loss(self):
        value, flag = calculate_cagr(100, -50, 5)
        self.assertIsNone(value)
        self.assertEqual(flag, "DECLINE_TO_LOSS")

    def test_turnaround(self):
        value, flag = calculate_cagr(-100, 200, 5)
        self.assertIsNone(value)
        self.assertEqual(flag, "TURNAROUND")

    def test_both_negative(self):
        value, flag = calculate_cagr(-100, -50, 5)
        self.assertIsNone(value)
        self.assertEqual(flag, "BOTH_NEGATIVE")

    def test_zero_base(self):
        value, flag = calculate_cagr(0, 100, 5)
        self.assertIsNone(value)
        self.assertEqual(flag, "ZERO_BASE")

    def test_insufficient_years(self):
        value, flag = calculate_cagr(100, 200, 0)
        self.assertIsNone(value)
        self.assertEqual(flag, "INSUFFICIENT")

    def test_revenue_cagr(self):
        value, flag = revenue_cagr(100, 200, 5)
        self.assertIsNone(flag)
        self.assertAlmostEqual(value, 14.87, places=2)

    def test_pat_cagr(self):
        value, flag = pat_cagr(100, 200, 5)
        self.assertIsNone(flag)
        self.assertAlmostEqual(value, 14.87, places=2)

    def test_eps_cagr(self):
        value, flag = eps_cagr(10, 20, 5)
        self.assertIsNone(flag)
        self.assertAlmostEqual(value, 14.87, places=2)


if __name__ == "__main__":
    unittest.main()