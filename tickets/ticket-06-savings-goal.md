# Track a savings goal with progress

**Difficulty:** M

## Description

Players want to set a savings goal (like "$100 for a new game") and see how
close their current balance gets them there.

## Acceptance criteria

- [ ] A new function stores a savings goal amount (e.g. `data["savings_goal"]`).
- [ ] A helper returns progress toward the goal as a percentage, capped at 100.
- [ ] A goal of `0` or an unset goal is handled without dividing by zero.
- [ ] A new menu option in `main.py` sets the goal and shows current progress.
- [ ] A test covers under-goal, at-goal, and over-goal balances.

## Notes

Touches `features/core.py`, `main.py`, and `data/budgetbuddy.json`. The
`balance` function is what progress is measured against.
