# Set a budget per category

**Difficulty:** M

## Description

Players want to cap how much they plan to spend in a category (like "food" or
"fun") and get a heads-up when they've gone over.

## Acceptance criteria

- [ ] A new function stores a `{category: limit}` budget map (in the data file
      is fine, e.g. `data["budgets"]`).
- [ ] A helper checks whether total spend in a category has passed its budget.
- [ ] A bad/missing category (no budget set) is reported clearly, not a raw crash.
- [ ] A new menu option in `main.py` sets a budget and shows over-budget categories.
- [ ] A test covers a category under budget and one over budget.

## Notes

Touches `features/core.py`, `main.py`, and `data/budgetbuddy.json`. The
`transactions_by_category` function is a good building block.
