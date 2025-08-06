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
                my_tracker.add_transaction()
            case "2":
                my_tracker.edit_transaction()
            case "3":
                my_tracker.delete_transaction()
            case "4":
                print("\nViewing transactions:")
                my_tracker.view_transactions()
            case "5":
                print(f"Current balance: ${my_tracker.get_balance():.2f}")
            case "6":
                print("Exiting application.")
                break
            case _:
                print("Invalid option. Please pick from the options above.")


if __name__ == "__main__":
    main()
