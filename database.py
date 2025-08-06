import sqlite3

ALLOWED_FIELDS = {"date", "description", "amount", "category", "type"}


class BudgetTrackerDB:

    def __init__(self, path):
        self.path = path
        self.table_name = "transactions"
        self.connect = sqlite3.connect(self.path)
        self.cursor = self.connect.cursor()
        self.create_tb()

    def create_tb(self):
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.table_name} (
                            id INTEGER PRIMARY KEY,
                            type TEXT,
                            category TEXT,
                            description TEXT,
                            amount REAL,
                            date TEXT)
                            ''')
        self.connect.commit()

    def close(self):
        self.cursor.close()
        self.connect.close()

    def add_transaction(self, transaction):
        try:
            self.cursor.execute(
                f'''INSERT INTO {self.table_name} (type, category, description, amount, date) VALUES (?,?,?,?,?)''', transaction)
            self.connect.commit()
        except ValueError as e:
            raise e("Unable to add transaction to database.")

    def update_transaction(self, id, new_data, field_to_update):
        if field_to_update not in ALLOWED_FIELDS:
            raise ValueError(f"Invalid field: {field_to_update.title()}")

        # implement functionality
        self.cursor.execute(
            f'''UPDATE {self.table_name} SET {field_to_update} = ? WHERE id = ?''', (new_data, id))

        self.connect.commit()
        print(f"Transaction #{id} updated successfully.")

    def delete_transaction(self, id):
        try:
            self.cursor.execute(
                f'DELETE FROM {self.table_name} WHERE id = ?', (id,))
            self.connect.commit()
        except sqlite3.Error as e:
            print(f"Error deleting transaction: {e}")

    def get_transaction_all(self):
        self.cursor.execute(f'SELECT * FROM {self.table_name}')
        return self.cursor.fetchall()

    def validate_transaction(self, id):
        self.cursor.execute(
            f'SELECT * FROM {self.table_name} WHERE id = ?', (id,))
        if self.cursor.fetchone() is None:
            raise ValueError(f"Transaction #{id} does not exist.")

    def get_transaction_one(self, id):
        self.cursor.execute(
            f'SELECT * FROM {self.table_name} WHERE id = ?', (id,))
        transaction = self.cursor.fetchone()
        if transaction is None:
            raise ValueError(f"Transaction #{id} does not exist.")
        return transaction
    # for testing

    def clear(self):
        self.cursor.execute(f'DELETE FROM {self.table_name}')
        self.connect.commit()
