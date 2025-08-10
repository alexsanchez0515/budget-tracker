import sqlite3
import bcrypt
from datetime import datetime


class LoginAuthentication:

    def __init__(self, path: str):
        self.path = path
        self.table_name = "login"
        self.connect = sqlite3.connect(self.path)
        self.cursor = self.connect.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.table_name} (
                            id INTEGER PRIMARY KEY,
                            email TEXT,
                            password BLOB,
                            date TEXT)
                            ''')
        self.connect.commit()

    def create_account(self, email: str, password: str):
        now = datetime.now().isoformat()
        hashed = self.hash_password(password)
        self.cursor.execute(f'''INSERT INTO {self.table_name} 
                            (email, password, date) VALUES (?, ?, ?)''',
                            (email, hashed, now))
        self.connect.commit()

    def login(self, email: str, password: str):
        #FIXME: implement login functionality
        pass

    def hash_password(self, password: str):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password=password, salt=salt)
        return hashed

    def close(self):
        self.cursor.close()
        self.connect.close()
