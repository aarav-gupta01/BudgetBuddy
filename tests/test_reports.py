"""Reference tests for the average_balance feature (Lesson 12 answer key)."""

import unittest

from features import reports


class TestAverageBalance(unittest.TestCase):
    def test_empty_history_is_zero(self):
        self.assertEqual(reports.average_balance({"history": []}), 0.0)

    def test_single_balance(self):
        self.assertEqual(reports.average_balance({"history": [60]}), 60.0)

    def test_several_balances_are_averaged(self):
        self.assertEqual(reports.average_balance({"history": [50.0, 45.0, 60.0]}), 51.7)


if __name__ == "__main__":
    unittest.main()
