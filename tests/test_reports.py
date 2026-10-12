import unittest
from features import reports

class TestReports(unittest.TestCase):
    def test_empty_account(self):
        data = {"transactions": []}

        result = reports.category_report(data)

        self.assertEqual(result, {})

    def test_sample_transactions(self):
        data = {
            "transactions": [
                {'category': 'food', 'amount': -4},
                {'category': 'income', 'amount': 45},
                {'category': 'food', 'amount': -10}
            ]
        }

        result = reports.category_report(data)
        correct = {
            'food': -14, 'income': 45
        }

        self.assertEqual(result, correct)
