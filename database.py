import sqlite3


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

    def add_exec(self, transaction):
        try:
            self.cursor.execute(
                f'''INSERT INTO {self.table_name} (type, category, description, amount, date) VALUES (?,?,?,?,?)''', transaction)
            self.connect.commit()
        except ValueError as e:
            raise e("Unable to add transaction to database.")

    def update_exec(self, transaction):
        # implement functionality
        pass

    def delete_exec(self, id):
        try:
            self.cursor.execute(
                f'DELETE FROM {self.table_name} WHERE id = ?', (id,))
            self.connect.commit()
        except sqlite3.Error as e:
            print(f"Error deleting transaction: {e}")

    def get_transactions(self):
        self.cursor.execute(f'SELECT * FROM {self.table_name}')
        return self.cursor.fetchall()

    def find_transaction(self, id):
        self.cursor.execute(
            f'SELECT * FROM {self.table_name} WHERE id = ?', (id,))
        if self.cursor.fetchone() is None:
            raise ValueError(f"Transaction #{id} does not exist.")

    # for testing
    def clear(self):
        self.cursor.execute(f'DELETE FROM {self.table_name}')
        self.connect.commit()
