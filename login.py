import sqlite3
import bcrypt
from datetime import datetime
from email_validator import validate_email, EmailNotValidError
import re

class LoginAuthentication:

    def __init__(self, path: str) -> None:
        self.path = path
        self.table_name = "login"
        self.connect = sqlite3.connect(self.path)
        self.cursor = self.connect.cursor()
        self.create_table()

    def display_menu(self) -> None:
        print("Welcome to Budget Tracker!\n")
        print('\t1.) Login\n\t2.) Create an account\n\t3.) Forgot password\n')

    def create_table(self) -> None:
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.table_name} (
                            id INTEGER PRIMARY KEY,
                            email TEXT,
                            password BLOB,
                            date TEXT)
                            ''')
        self.connect.commit()

    def create_account(self, email: str, password: str) -> None:
        now = datetime.now().isoformat()
        hashed = self.hash_password(password)
        self.cursor.execute(f'''INSERT INTO {self.table_name} 
                            (email, password, date) VALUES (?, ?, ?)''',
                            (email, hashed, now))
        self.connect.commit()

    def login(self, email: str, password: str) -> None:
        #FIXME: implement login functionality
        self.cursor.execute(f'''SELECT email, password FROM {self.table_name} WHERE email = ?''', (email,))
        acc = self.cursor.fetchone()

        stored_email, stored_pw = acc

        print(stored_email, stored_pw)

    def create_acc_email(self) -> str:
        try:
            email = input("Enter your email >> ")
            valid = validate_email(email)
            return valid.email
        except EmailNotValidError as e:
            print(f"Error: {e}")

    def create_acc_password(self) -> str:
        while True:

            password = input("Enter password >> ")
            if not self.valid_password(password):
                print("Invalid password: must be 6-20 chars, include uppercase, lowercase, digit, special char.")
                continue

            confirm = input("Confirm password >> ")
            if (confirm != password):
                print("Error: Passwords must match.")
                continue

            return password

    def email_prompt(self) -> None:
        email = input("Enter your email >> ")
        return email    

    def password_prompt(self) -> str:
        password = input("Enter your password >> ")
        return password
        
    def valid_password(self, password: str) -> bool:
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        pattern = re.compile(reg)
        pw_match = re.search(pattern, password)
        return bool(pw_match)
        
    def hash_password(self, password: str) -> bytes:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password=password.encode('utf-8'), salt=salt)
        return hashed

    def forgot_password(self) -> None:
        #FIXME functionality
        self.update_account()
        ...

    def update_account(self) -> None:
        #FIXME functionality
        ...

    def close(self) -> None:
        self.cursor.close()
        self.connect.close()
