"""BudgetBuddy - a small spending/allowance tracker.

Run it with:  python main.py
"""

import storage
from features import core, reports


def show_menu():
    print()
    print("=== BudgetBuddy ===")
    print("1) Show balance")
    print("2) List transactions")
    print("3) Add a transaction")
    print("4) Filter by category")
    print("5) Show the last transaction")
    print("6) Category breakdown")
    print("7) Spending summary")
    print("8) Account summary")
    print("0) Quit")


def main():
    data = storage.load_data()
    while True:
        show_menu()
        try:
            choice = input("Pick an option: ").strip()
        except EOFError:
            print()
            break
        if choice == "0":
            print("See you next session!")
            break
        elif choice == "1":
            print("Balance: $" + str(core.balance(data)))
        elif choice == "2":
            core.list_transactions(core.get_transactions(data))
        elif choice == "3":
            description = input("Description: ")
            amount = float(input("Amount: "))
            core.add_transaction(data, description, amount)
            storage.save_data(data)
            print("Transaction added.")
        elif choice == "4":
            category = input("Category: ").strip()
            matches = core.transactions_by_category(core.get_transactions(data), category)
            for t in matches:
                print("- " + t["description"])
        elif choice == "5":
            print(core.last_transaction(core.get_transactions(data))["description"])
        elif choice == "6":
            print(core.count_by_category(core.get_transactions(data)))
        elif choice == "7":
            txns = core.get_transactions(data)
            print("Spent $" + str(len(txns)) + " over " + str(core.total_spent(txns)) +
                  " transactions (avg $" + str(core.average_transaction(txns)) + ").")
        elif choice == "8":
            print(reports.account_summary(data))
        else:
            print("Please pick a number from the menu.")


if __name__ == "__main__":
    main()
