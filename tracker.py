from util import Utilities

utils = Utilities()

MIN = 1000
MAX = 9999


class BudgetTracker:

    def __init__(self, name: str):
        self.transactions = []
        self.balance = 0.0
        self.name = name
        self.next_id = MIN + 1

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
        return

    def delete_transaction(self):
        user_input = input(
            "Enter the transaction ID you would like to delete: ")

        try:
            search_key = int(user_input)

            if search_key < MIN or search_key > MAX:
                raise ValueError(f"ID must be in range of {MIN} - {MAX}")

            self.transactions = list(
                filter(lambda d: d.get('id') != search_key, self.transactions))

            print(f"Transaction ID #{search_key} has been deleted.")

        except ValueError as e:
            print(f"Error: {e}")
