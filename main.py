from tracker import BudgetTracker
from util import Utilities

test_transaction_in = {
    "type": "Income",
    "description": "Transaction for Testing Purposes - In",
    "category": "Test In",
    "amount": 5000.00,
    "date": "08/04/2025",
    "id": Utilities.random_id(1001, 9999)
}
test_transaction_ex = {
    "type": "Expense",
    "description": "Transaction for Testing Purposes - Ex",
    "category": "Test Ex",
    "amount": 3456.78,
    "date": "08/04/2025",
    "id": Utilities.random_id(1001, 9999)
}


def main():
    # initializing the tracker file
    my_tracker = BudgetTracker("Alex")
    my_tracker.transactions.append(test_transaction_in)
    my_tracker.transactions.append(test_transaction_ex)
    my_tracker.update_balance(
        test_transaction_in['type'], test_transaction_in['amount'])
    my_tracker.update_balance(
        test_transaction_ex['type'], test_transaction_ex['amount'])

    options = ["1", "2", "3", "4", "5", "6"]

    while True:
        my_tracker.display_menu()
        choice = input("Choose an option: ")

        match choice:
            case "1":
                my_tracker.add_transaction()
            case "2":
                my_tracker.edit_transaction()
            case "3":
                my_tracker.delete_transaction()
            case "4":
                print("\nViewing transactions:")
                my_tracker.view_transactions()
            case "5":
                # create function in tracker.py to view balance (view_balance)
                print(f"Current balance: ${my_tracker.get_balance():.2f}")
            case "6":
                print("Exiting application.")
                break
            case _:
                print("Invalid input.")


if __name__ == "__main__":
    main()
