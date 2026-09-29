"""Reporting helpers for BudgetBuddy.

Heads up: this module is half-built on purpose. `account_summary` works, but
`category_report` is still a stub with a clear seam to finish (see the tickets).
"""


def account_summary(data):
    return data["account_name"] + ": " + str(len(data["transactions"])) + " transactions"


def category_report(data):
    # TODO(ticket): tally each transaction into a {category: total amount} dict and return it.
    # For now this returns an empty report so the menu never crashes.
    report = {}
    return report


def average_balance(data):
    """Average of the past balances in data['history'].

    Returns a float rounded to one decimal place. An empty history returns 0.0.
    This feature works but has no tests yet - that's your Lesson 12 job.
    """
    history = data["history"]
    if not history:
        return 0.0
    return round(sum(history) / len(history), 1)
