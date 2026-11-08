import unittest
from features.reports import average_balance

class TestCase(unittest.TestCase):
    def test_return_0(self):
        data = {"history": []}
        result = average_balance(data)
        self.assertEqual(result, 0.0)

    def test_average_balance(self):
        data = {"history": [10.0, 20.0, 30.0]}
        result = average_balance(data)
        self.assertEqual(result, 20.0)


