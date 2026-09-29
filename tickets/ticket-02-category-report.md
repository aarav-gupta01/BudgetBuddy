# Finish the category totals report

**Difficulty:** S

## Description

`features/reports.py` has a `category_report(data)` function that is only a stub -
it always returns an empty dict. Finish it so it totals up how much was spent
or earned in each category. This is the report the menu's "Category breakdown"
option should eventually use.

## Acceptance criteria

- [ ] `category_report(data)` returns a dict of `{category: total_amount}`.
- [ ] Every transaction in the account is counted exactly once, in its category.
- [ ] An empty account returns an empty dict (no crash).
- [ ] A test in `tests/` checks the totals against a small sample account.

## Notes

Touches `features/reports.py` and a test file. The `count_by_category` function
in `core.py` is a good reference for the tally pattern.
