# Add a monthly summary report

**Difficulty:** M

## Description

Right now reports only summarize the whole account at once. Add a report that
groups transactions by month and shows how much came in and went out each
month, so a player can see spending trends over time.

## Acceptance criteria

- [ ] A new function in `features/reports.py` groups transactions by month.
- [ ] Each month reports total income and total spending separately.
- [ ] A month with no transactions is simply absent (no crash, no empty entry).
- [ ] A new menu option in `main.py` prints the monthly summary.
- [ ] A test covers a small set of transactions across two different months.

## Notes

Touches `features/reports.py` and `main.py`. Transactions will need a `date`
field added when they're created for this to be meaningful - note that in the
PR description.
