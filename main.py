from tracker import BudgetTracker
from util import Utilities


def main():
    # initializing the tracker file
    my_tracker = BudgetTracker("Alex")

    options = ["1", "2", "3", "4", "5", "6"]

    while True:
        my_tracker.display_menu()
        choice = input("Choose an option: ")

        match choice:
            case "1":
                # function to create transaction
                print(
                    "FIXME: function to create_transaction(), then call add_transaction()")
                pass
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
                # start of user program loop
                # my_tracker.add_transaction("income", "Test1", "Test1", 528.37)
                # my_tracker.add_transaction("expense", "Test2", "Test2", 180.81)
                # my_tracker.add_transaction("income", "Test3", "Test3", 344.45)

                # my_tracker.edit_transaction()
                # my_tracker.view_transactions()


if __name__ == "__main__":
    main()
