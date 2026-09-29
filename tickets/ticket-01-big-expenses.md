# Add a big-expenses warning

**Difficulty:** S

## Description

Right now every transaction looks the same in the list. Players want a quick
way to spot the big hits to their balance. Add a helper that, given the
transactions and a dollar threshold, returns just the expenses at or above
that threshold so a warning view can use them.

## Acceptance criteria

- [ ] A new function `big_expenses(transactions, threshold)` lives in `features/core.py`.
- [ ] `threshold` is a positive number (e.g. `10` means "$10 or more spent").
- [ ] It returns the list of transactions whose spend is at least `threshold`
      (income and small expenses are excluded).
- [ ] If nothing qualifies, it returns an empty list (no crash).
- [ ] A test in `tests/` covers a mixed case and the "nothing qualifies" case.

## Notes

Touches `features/core.py` and a test file. No changes to the data file needed.
