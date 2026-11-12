"""Example tests for BudgetBuddy. Two small tests to copy from in Lesson 12."""

import unittest
import csv
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

    def test_export_to_csv(self):
        txns = [{"id": 1, "description": "Lunch", "amount": -5.0, "category": "food"}]
        core.export_to_csv(txns, "test_output.csv")
        with open("test_output.csv") as f:
            rows = list(csv.reader(f))
        self.assertEqual(rows[0], ["id", "description", "amount", "category"])
        self.assertEqual(rows[1], ["1", "Lunch", "-5.0", "food"])



if __name__ == "__main__":
    unittest.main()
