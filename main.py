from tracker import BudgetTracker
# will use login later in development
from login import LoginAuthentication

def main() -> None:
    # initializing the tracker file
    my_tracker = BudgetTracker("Alex")

    while True:
        my_tracker.display_menu()
        choice = input("Choose an option: ")

        match choice:
            case "1":
                my_tracker.prompt_to_add()
            case "2":
                my_tracker.prompt_to_update()
            case "3":
                my_tracker.prompt_to_delete()
            case "4":
                print("\nViewing transactions:")
                my_tracker.view_transaction_all()
            case "5":
                print(f"Current balance: ${my_tracker.get_balance():.2f}")
            case "6":
                print("Exiting application.")
                break
            case _:
                print("Invalid option. Please pick from the options above.")


if __name__ == "__main__":
    main()
