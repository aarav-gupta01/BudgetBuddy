"""Core BudgetBuddy logic: transactions, balance, and small helpers."""

import csv


def get_transactions(data):
    return data["transactions"]


def add_transaction(data, description, amount, category="general"):
    new_id = max((t["id"] for t in data["transactions"]), default=0) + 1
    tx = {"id": new_id, "description": description, "amount": amount, "category": category}
    data["transactions"].append(tx)
    return tx


def balance(data):
    return round(data["starting_balance"] + sum(t["amount"] for t in data["transactions"]), 2)


def list_transactions(transactions, show=print):
    for t in transactions:
        show(str(t["id"]) + ". " + t["description"] + " (" + str(t["amount"]) + ")")


def transactions_by_category(transactions, category):
    return [t for t in transactions if t["category"] == category]


"""
count_by_category takes in the list of dictionaries, transactions, 
and counts how many of each category is present. It returns a dictionary 
of the category as the key and the number of times it is there as the value.
"""
def count_by_category(transactions):
    counts = {}
    for t in transactions:
        name = t["category"]
        counts[name] = counts.get(name, 0) + 1
    return counts


def last_transaction(transactions):
    if not transactions:
        return None
    return transactions[-1]


def total_spent(transactions):
    return round(sum(-t["amount"] for t in transactions if t["amount"] < 0), 2)


def average_transaction(transactions):
    if not transactions:
        return 0
    return round(sum(t["amount"] for t in transactions) / len(transactions), 2)


def export_to_csv(transactions, path):
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "description", "amount", "category"])
        for t in transactions:
            writer.writerow([t["id"], t["description"], t["amount"], t["category"]])
