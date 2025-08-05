from util import Utilities

utils = Utilities()


class BudgetTracker:

    def __init__(self, name: str):
        self.transactions = []
        self.options = ["date", "description", "amount", "category", "type"]
        self.balance = 0.0
        self.name = name
        self.MIN_ID = 1001  # subject to change later
        self.MAX_ID = 9999  # subject to change later
        self.next_id = self.MIN_ID
        self.return_key = '0'

    def get_balance(self):
        return self.balance

    def get_name(self):
        return self.name

    def update_balance(self, t_type: str, amount: float):
        if t_type == "income":
            self.balance = utils.add(self.balance, amount)
        elif t_type == "expense":
            self.balance = utils.sub(self.balance, amount)

    def view_transactions(self):

        if len(self.transactions) == 0:
            print("No transactions to view currently.")
            return

        for t in self.transactions:
            print(
                f"{t['type'].title()}: {t['description']} - ${t['amount']:.2f} on {t['date']} - ID: {t['id']}")

    def add_transaction(self, t_type: str, desc: str, category: str, amount: float, date: str = None):
        t_type = t_type.lower()

        if t_type not in ("expense", "income"):
            raise ValueError(
                "Invalid type. Please use 'income' or 'expense' for transaction type.")

        if date is None:
            date = utils.format_date(utils.get_date())
        else:
            pass

        transaction = {
            "type": t_type,
            "description": desc,
            "category": category,
            "amount": amount,
            "date": date,
            "id": self.next_id
        }

        self.transactions.append(transaction)
        self.update_balance(t_type, amount)
        self.next_id += 1
        print(f"{t_type.title()} was added: {desc} - ${amount:.2f}")

    def edit_transaction(self):
        user_input = input(
            "\nEnter the transaction ID you would like to edit, or type '0' to return to main menu: ")

        try:
            if user_input.lower() == self.return_key:
                print("Returning to main menu")
                return

            search_keyID = int(user_input)

            if search_keyID < self.MIN_ID or search_keyID > self.MAX_ID:
                raise ValueError(
                    f"ID must be in range of {self.MIN_ID} - {self.MAX_ID}")

            while True:
                selected_transaction = self.select_transaction(search_keyID)

                for c in self.options:
                    print(f"{c.title()}")
                choice = input(
                    "\nEnter an option to edit from the list above: ").lower()

                match choice:
                    case 'date':
                        self.edit_field(selected_transaction, "date")
                    case 'description':
                        self.edit_field(selected_transaction, "description")
                    case 'amount':
                        self.edit_field(selected_transaction, "amount")
                    case 'category':
                        self.edit_field(selected_transaction, "category")
                    case 'type':
                        self.edit_field(selected_transaction, "type")
                    case self.return_key:
                        print("Returning to main menu")
                        break
                    case _:
                        print("Invalid option. Choose an option from the list.")

        except ValueError as e:
            print(f"Error: {e}")

    def delete_transaction(self):
        user_input = input(
            "\nEnter the transaction ID you would like to delete, or type '0' to return to main menu: ")

        try:
            if user_input == self.return_key:
                # return user to main menu
                print("Returning to main menu...")
                return

            search_key = int(user_input)

            if search_key < self.MIN_ID or search_key > self.MAX_ID:
                raise ValueError(
                    f"ID must be in range of {self.MIN_ID} - {self.MAX_ID}")

            self.transactions = list(
                filter(lambda d: d.get('id') != search_key, self.transactions))

            print(f"\nTransaction ID #{search_key} has been deleted.")

        except ValueError as e:
            print(f"Error: {e}")

    def select_transaction(self, id):
        for t in self.transactions:
            if t['id'] == id:
                symbol = '+' if t['type'] == 'income' else '-'
                print(
                    f"\n\tSelected transaction\n{t['category'].title()} - {t['description']} - {t['type'].title()}: {symbol}${t['amount']:.2f} - {t['date']}\n")
                return t
            else:
                print("Invalid choice.")

    def edit_field(self, transaction, field):

        print(f"\nEditing field: {field.title()}")

        dollar_sign = "$" if field.lower() == 'amount' else ""
        print(f"Current {field} value: {dollar_sign}{transaction[field]}")

        while True:
            validator = self.get_validator(field)
            new_field = input(f"\nEnter new {field}: {dollar_sign}")

            try:
                update = validator(new_field)
                self.update_transaction(transaction, field, update)
                print(f"{field.title()} updated successfully!\n")
                break
            except ValueError as e:
                print(f"Error: {e}")
                continue

    def update_transaction(self, transaction: list, field, update):
        t_id = transaction['id']
        transaction[field] = update
        self.transactions = list(
            filter(lambda d: d.get('id') != t_id, self.transactions))
        self.transactions.append(transaction)

    def get_validator(self, field_name):
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

    def validate_amount(self, field):
        try:
            amount = float(field)
            if (amount <= 0):
                raise ValueError("Amount must be greater than zero.")
            return amount
        except ValueError:
            raise ValueError("Amount must be a valid number.")

    def validate_date(self, field):
        print("\nFIXME: validate date functionality.")

    def validate_category(self, field):
        field = field.strip().lower()
        if not field.isalpha():
            raise ValueError("Category must be text only.")
        if len(field) < 3:
            raise ValueError(
                "Category is too short. Must be longer than 3 characters.")
        if len(field) > 20:
            raise ValueError(
                "Category is too long. Must be shorter than 20 characters")
        return field.title()

    def validate_type(self, field):
        type_choice = ['income', 'expense']
        field = field.lower().strip()
        if (field not in type_choice):
            raise ValueError("Type must be either 'income' or 'expense'")
        return field.title()

    def validate_description(self, field):
        field = field.lower().strip()
        if len(field) < 3:
            raise ValueError(
                "Description is too short. Must be longer than 3 characters.")
        if len(field) > 100:
            raise ValueError(
                "Description is too long. Must be shorter than 100 characters")
        return field.title()

    def get_transaction_id(self, transaction):
        return transaction['id']

    def display_menu(self):
        print("\n\tBudget Tracker Menu\n")
        print("1.) Add Transaction")
        print("2.) Edit Transaction")
        print("3.) Delete Transaction")
        print("4.) View Transaction")
        print("5.) View Balance")
        print("6.) Exit Tracker\n")
