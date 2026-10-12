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
