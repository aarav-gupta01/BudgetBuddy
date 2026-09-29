# Export transactions to a CSV file

**Difficulty:** M

## Description

Players want to open their transactions in a spreadsheet. Add an export that
writes the current transactions to a CSV file with columns
`id,description,amount,category`.

## Acceptance criteria

- [ ] A new function writes the transactions to a given CSV path.
- [ ] The header row matches `id,description,amount,category`.
- [ ] Every transaction becomes exactly one row, in order.
- [ ] A new menu option in `main.py` runs the export and confirms the file was written.
- [ ] A test covers exporting a small list and reading the CSV back.

## Notes

The standard-library `csv` module handles the writing. Touches
`features/core.py` and `main.py`.
