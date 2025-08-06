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

    def add_transaction(self, transaction):
        self.cursor.execute(
            f'''INSERT INTO {self.table_name} (type, category, description, amount, date) VALUES (?,?,?,?,?)''', transaction)
        self.connect.commit()

    def get_transactions(self):
        self.cursor.execute(f'SELECT * FROM {self.table_name}')
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connect.close()

    def update_transaction(self, transaction):
        # implement functionality
        pass

    def delete_transaction(self, transaction):
        # implement functionality
        pass

    # for testing
    def clear(self):
        self.cursor.execute(f'DELETE FROM {self.table_name}')
        self.connect.commit()
