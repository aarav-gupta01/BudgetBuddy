"""Reporting helpers for BudgetBuddy.

Heads up: this module is half-built on purpose. `account_summary` works, but
`category_report` is still a stub with a clear seam to finish (see the tickets).
"""


def account_summary(data):
    return data["name"] + ": " + str(len(data["transactions"])) + " transactions"


def category_report(data):
    # TODO(ticket): tally each transaction into a {category: total amount} dict and return it.
    # For now this returns an empty report so the menu never crashes.
    report = {}
    return report
