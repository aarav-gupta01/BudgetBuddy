"""Example tests for BudgetBuddy. Two small tests to copy from in Lesson 12."""

import unittest

from features import core


class TestCore(unittest.TestCase):
    def test_balance(self):
        data = {"starting_balance": 50.0, "transactions": [
            {"id": 1, "description": "Bus pass", "amount": -2.5, "category": "transport"},
            {"id": 2, "description": "Allowance", "amount": 20.0, "category": "income"},
        ]}
        self.assertEqual(core.balance(data), 67.5)

    def test_add_transaction_gives_a_new_id(self):
        data = {"transactions": [{"id": 1, "description": "t", "amount": 5.0, "category": "general"}]}
        tx = core.add_transaction(data, "New thing", -3.0)
        self.assertEqual(tx["id"], 2)
        self.assertEqual(len(data["transactions"]), 2)


if __name__ == "__main__":
    unittest.main()
