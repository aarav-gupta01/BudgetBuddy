"""Reporting helpers for BudgetBuddy.
"""


def account_summary(data):
    return data["account_name"] + ": " + str(len(data["transactions"])) + " transactions"


def category_report(data):
    report = {}
    for t in data["transactions"]:
        flow = t['amount']
        report[t['category']] = report.get(t['category'], 0) + flow
    return report


def average_balance(data):
    """Average of the past balances in data['history'].

    Returns a float rounded to one decimal place. An empty history returns 0.0.
    """
    history = data["history"]
    if not history:
        return 0.0
    return round(sum(history) / len(history), 1)
