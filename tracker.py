from utilities import Utilities as util
from database import BudgetTrackerDB
from login import LoginAuthentication

path = "C:\\Users\\alexs\\Documents\\Python Portfolio\\Budget Tracker\\tracker.db"

class BudgetTracker:

    def __init__(self, name: str) -> None:
        self.db = BudgetTrackerDB(path=path)
        self.options: list = ["1. date", "2. description", "3. amount",
                        "4. category", "5. type", "0. return to main menu"]
        self.balance: float = 0
        self.name: str = name
        self.MIN_ID: int = 1001  # subject to change later
        self.MAX_ID: int = 9999  # subject to change later
        self.return_key: str = '0'
        self.db.clear()  # for testing purposes, to work with 1 transaction for now

    def get_balance(self) -> float:
        return self.balance

    def get_name(self) -> str:
        return self.name

    def init_balance(self) -> None:
        # function to initialize saved balances from previous use, will implement/update later
        if len(self.transactions) > 0:
            for t in self.transactions:
                if t['type'] == "income":
                    self.balance += float(t['amount'])
                if t['type'] == "expense":
                    self.balance -= float(t['amount'])

    def init_transactions(self) -> None:
        # function to initialize saved transactions from previous use, will implement/update later
        ...

    def update_balance(self, t_type: str, amount: float) -> None:
        if t_type == "income":
            self.balance += amount
        elif t_type == "expense":
            self.balance -= amount

    def view_transaction_all(self) -> None:
        for row in self.db.get_transaction_all():
            print(row)

    def view_transaction_one(self, id: int) -> None:
        transaction = self.db.get_transaction_one(id)
        if transaction:
            print("\nUpdated transaction:")
            print(
                f"ID: {transaction[0]} | Type: {transaction[1].title()} | Category: {transaction[2].title()} | Description: {transaction[3].title()} | Amount: ${transaction[4]:.2f} | Date: {transaction[5]}")

    def get_field_prompt(self, prompt: str) -> None:
        while True:
            try:

                user_type = input(prompt)

                if user_type == '0':
                    print("Returning to main menu")
                    return

                valid_field = self.validate_type(user_type)
                break
            except ValueError as e:
                print(f"Error: {e}. Please try again.")
        return valid_field

    def prompt_to_add(self) -> None:
        valid_type = self.get_field_prompt("Enter a transaction type, (Income or Expense), or type '0' to return to main menu: ")
        valid_category = self.get_field_prompt("Enter a category, (Work, Family, Bills, etc.), or type '0' to return to main menu: : ")
        valid_desc = self.get_field_prompt("Enter a description, or type '0' to return to main menu: ")
        valid_amount = self.get_field_prompt("Enter an amount, or type '0' to return to main menu: ")
        valid_date = self.get_field_prompt("Enter a date, (MM/DD/YYYY), or type '0' to return to main menu:  ")

        # type, category, description, amount, date
        transaction = (
            valid_type,
            valid_category,
            valid_desc,
            valid_amount,
            valid_date
        )

        self.db.add_transaction(transaction)
        self.update_balance(valid_type, valid_amount)
        # id = self.db.get_field_value(id, field=id)
        print("\nTransaction added:")
        print(
            f"Type: {valid_type.title()} | Category: {valid_category.title()} | Description: {valid_desc.title()} | Amount: ${valid_amount:.2f} | Date: {valid_date}")

    def prompt_to_update(self) -> None:
        self.view_transaction_all()

        user_input = input(
            "\nEnter the transaction ID you would like to edit, or type '0' to return to main menu: ")

        try:
            if user_input.lower() == self.return_key:
                print("Returning to main menu")
                return

            search_keyID = int(user_input)
            self.db.validate_transaction(search_keyID)

            while True:
                print("")
                for c in self.options:
                    print(f"{c.title()}")

                choice = input(
                    "\nEnter an option to edit from the list above, or type '0' to return to main menu: ").lower()

                match choice:
                    case 'date':
                        self.edit_field(search_keyID, "date")
                    case 'description':
                        self.edit_field(search_keyID, "description")
                    case 'amount':
                        self.edit_field(search_keyID, "amount")
                    case 'category':
                        self.edit_field(search_keyID, "category")
                    case 'type':
                        self.edit_field(search_keyID, "type")
                    case self.return_key:
                        print("Returning to main menu")
                        break
                    case _:
                        print("Invalid option. Choose an option from the list.")

        except ValueError as e:
            print(f"Error: {e}")

    def prompt_to_delete(self) -> None:
        self.view_transaction_all()
        user_input = input(
            "\nEnter the transaction ID you would like to delete, or type '0' to return to main menu: ")

        try:
            if user_input == self.return_key:
                print("Returning to main menu...")
                return

            search_id = int(user_input)
            self.db.find_transaction(search_id)

            confirm = input(
                f"Are you sure you want to delete transaction #{search_id}? (y/n): ")
            if confirm != 'y':
                print("Deletion cancelled.")
                return

            self.db.delete_transaction(search_id)
            print(f"\nTransaction ID #{search_id} has been deleted.")

        except ValueError as e:
            print(f"Error: {e}")

    def edit_field(self, id: int, field: str) -> None:

        print(f"\nEditing field: {field.title()}")

        dollar_sign = "$" if field.lower() == 'amount' else ""
        # print(f"Current {field} value: {dollar_sign}{transaction[field]}")

        while True:
            validator = self.get_validator(field)
            new_field = input(f"\nEnter new {field}: {dollar_sign}")
            # current_value = self.db.get_field_val(id, field)

            try:
                update = validator(new_field)
                confirm = input(
                    f"Are you sure you want to update \"(current_value)\" to {update}? (y/n): ").lower()
                if confirm != 'y':
                    print("Update cancelled.")
                    break

                self.db.update_transaction(id, update, field)
                self.view_transaction_one(id)
                break
            except ValueError as e:
                print(f"Error: {e}")
                continue

    def get_validator(self, field_name: str):
        match field_name:
            case 'date':
                return self.validate_date
            case 'amount':
                return self.validate_amount
            case 'category':
                return self.validate_category
            case 'type':
                return self.validate_type
            case 'description':
                return self.validate_description

    def validate_amount(self, field: float) -> float:
        try:
            amount = float(field)
            if (amount <= 0):
                raise ValueError("Amount must be greater than zero.")
            return amount
        except ValueError:
            raise ValueError("Amount must be a valid number.")

    def validate_date(self, field: str) -> str:
        try:
            valid_date = util.format_date(field)
            return valid_date
        except ValueError:
            raise ValueError(
                "Date must be in MM/DD/YYYY format, and date must be valid")

    def validate_category(self, field: str) -> str:
        field = field.strip().lower()
        if not field.isalpha():
            raise ValueError("Category must be text only.")
        if len(field) < 3:
            raise ValueError(
                "Category is too short. Must be longer than 3 characters.")
        if len(field) > 20:
            raise ValueError(
                "Category is too long. Must be shorter than 20 characters")
        return field

    def validate_type(self, field: str) -> str:
        type_choice = ['income', 'expense']
        field = field.lower().strip()
        if (field not in type_choice):
            raise ValueError("Type must be either 'income' or 'expense'")
        return field

    def validate_description(self, field: str) -> str:
        field = field.lower().strip()
        if len(field) < 3:
            raise ValueError(
                "Description is too short. Must be longer than 3 characters.")
        if len(field) > 100:
            raise ValueError(
                "Description is too long. Must be shorter than 100 characters")
        return field

    def get_transaction_id(self, transaction: list) -> int:
        return transaction['id']

    def display_menu(self):
        print("\n\tBudget Tracker Menu\n")
        print("1.) Add Transaction")
        print("2.) Edit Transaction")
        print("3.) Delete Transaction")
        print("4.) View Transaction")
        print("5.) View Balance")
        print("6.) Log out\n")
