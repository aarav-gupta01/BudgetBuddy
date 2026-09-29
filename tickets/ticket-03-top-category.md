# Find the top spending category

**Difficulty:** M

## Description

Players want to know where their money actually goes. Add a helper that,
given the transactions, returns the category with the largest total spend
(income doesn't count as spending).

## Acceptance criteria

- [ ] A new function `top_spending_category(transactions)` lives in `features/core.py`.
- [ ] It returns the name of the category with the highest total spend
      (sum of the negative amounts, as a positive number).
- [ ] If there are no expenses at all, it returns `None`.
- [ ] Ties can go to whichever category is found first.
- [ ] A test in `tests/` covers a mixed case and the "no expenses" case.

## Notes

Touches `features/core.py` and a test file. Think about building a totals dict
per category, then finding the max.
