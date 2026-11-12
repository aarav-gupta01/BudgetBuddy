# BudgetBuddy

A small spending/allowance tracker you run in the terminal. Add transactions,
list them, and see your balance. This is your squad's starting product for
Elite 101 - you'll grow it one ticket at a time.

## What it does

Show your balance, list/add transactions, filter by category, see your last
transaction, category breakdown, spending summary, account summary, and
export your transactions to `transaction.csv` (menu option 9).

## Run it

```bash
python main.py
```

## Run the tests

```bash
python -m unittest
```

## How it's laid out

| File | What it does |
|---|---|
| `main.py` | The menu loop you interact with |
| `storage.py` | Loads and saves the JSON data file |
| `features/core.py` | The transactions, the balance, and small helpers |
| `features/reports.py` | Summary reports: account summary, category totals, average balance |
| `data/budgetbuddy.json` | The transaction history and starting balance |
| `tests/test_core.py` | Example tests to copy from |

## Team

<!-- Add yourself here on your Git lesson: - Your Name (role) -->
- Aarav Gupta (Building BudgetBuddy)
- (your squad will add themselves here)

## Where to start

Pick a ticket from the `tickets/` folder (or the Issues tab once your section
repo exists). Read `CONTRIBUTING.md` for the Definition of Done every pull
request has to meet.
