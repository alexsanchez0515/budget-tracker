from tracker import BudgetTracker
from login import LoginAuthentication

path = "C:\\Users\\alexs\\Documents\\Python Portfolio\\Budget Tracker\\tracker.db"

def main() -> None:
    # initializing the tracker file
    my_tracker = BudgetTracker("Alex")
    account = LoginAuthentication(path=path)
    account.display_menu()
    logged_in = False

    try:
        choice = input("Pick an option from the list above (1, 2, 3) >> ")
        match choice:
            case '1':
                email = account.email_prompt()
                password = account.password_prompt()
                account.login(email=email, password=password)
                logged_in = True
            case '2':
                email = account.create_acc_email()
                password = account.create_acc_password()
                account.create_account(email=email, password=password)
                print("Account created!")
            case '3':
                account.forgot_password()
                ...
    except ValueError as e:
        print("Invalid choice.")


    '''
    while logged_in:
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
                print("Logging out.")
                logged_in = False
                
            case _:
                print("Invalid option. Please pick from the options above.")
'''

if __name__ == "__main__":
    main()
