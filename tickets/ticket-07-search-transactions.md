# Search and filter transactions by description

**Difficulty:** S

## Description

With a long transaction history, players want to find a specific purchase
without scrolling through everything. Add a search that matches on the
transaction description.

## Acceptance criteria

- [ ] A new function `search_transactions(transactions, keyword)` lives in
      `features/core.py`.
- [ ] The match is case-insensitive and matches anywhere in the description.
- [ ] No matches returns an empty list (no crash).
- [ ] A new menu option in `main.py` prompts for a keyword and prints matches.
- [ ] A test covers a matching keyword and a keyword with no matches.

## Notes

Touches `features/core.py` and `main.py`. `list_transactions` is a good
reference for how matches should print.
