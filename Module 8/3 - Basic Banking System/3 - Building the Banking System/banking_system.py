import sqlite3
from datetime import datetime

# 3.3 Data Storage Module

class DataStorage:
    def __init__(self, db_name="banking_system.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    # Set up the initial database tables if they don't exist
    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                account_number INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                balance REAL NOT NULL,
                password TEXT NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id INTEGER PRIMARY KEY,
                account_number INTEGER,
                transaction_type TEXT NOT NULL,
                amount REAL,
                date TEXT NOT NULL
            )
        """)

        self.conn.commit()

    def close(self):
        self.conn.close()

# 3.1 Account Module

class Account:
    def __init__(self, storage):
        self.storage = storage

    def create_account(self, name, initial_deposit, password):
        # Data Validation and Security considerations would come here
        self.storage.cursor.execute("INSERT INTO accounts (name, balance, password) VALUES (?, ?, ?)",
                                    (name, initial_deposit, password))
        self.storage.conn.commit()
        return "Account created successfully!"

    def close_account(self, account_number, password):
        # Fetch account and check if password matches, then delete the account
        # We can add more checks like if balance is zero, etc.
        self.storage.cursor.execute("DELETE FROM accounts WHERE account_number = ? AND password = ?",
                                    (account_number, password))
        self.storage.conn.commit()
        return "Account closed successfully!"

    def check_balance(self, account_number, password):
        # Fetch account and check if password matches, then retrieve the balance
        self.storage.cursor.execute("SELECT balance FROM accounts WHERE account_number = ? AND password = ?",
                                    (account_number, password))
        balance = self.storage.cursor.fetchone()
        return balance[0] if balance else "Invalid account or password"

# 3.2 Transaction Module

class Transaction:
    def __init__(self, storage):
        self.storage = storage

    def deposit(self, account_number, amount):
        # Update account balance and record transaction
        self.storage.cursor.execute("UPDATE accounts SET balance = balance + ? WHERE account_number = ?",
                                    (amount, account_number))
        self.storage.cursor.execute("INSERT INTO transactions (account_number, transaction_type, amount, date) VALUES (?, ?, ?, ?)",
                                    (account_number, "deposit", amount, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        self.storage.conn.commit()
        return f"Deposited ${amount} to account {account_number}"

    def withdraw(self, account_number, amount):
        # Check if enough balance, then update account balance and record transaction
        # More validations would come here
        self.storage.cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
        balance = self.storage.cursor.fetchone()[0]
        if balance >= amount:
            self.storage.cursor.execute("UPDATE accounts SET balance = balance - ? WHERE account_number = ?",
                                        (amount, account_number))
            self.storage.cursor.execute("INSERT INTO transactions (account_number, transaction_type, amount, date) VALUES (?, ?, ?, ?)",
                                        (account_number, "withdraw", amount, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            self.storage.conn.commit()
            return f"Withdrew ${amount} from account {account_number}"
        else:
            return "Insufficient funds"

    def view_transactions(self, account_number):
        self.storage.cursor.execute("SELECT transaction_type, amount, date FROM transactions WHERE account_number = ?",
                                    (account_number,))
        transactions = self.storage.cursor.fetchall()
        if transactions:
            return "\n".join([f"{txn[0]}: ${txn[1]} on {txn[2]}" for txn in transactions])
        else:
            return "No transactions found"

# 3.4 User Interface (CLI) Module

def main():
    storage = DataStorage()
    account_module = Account(storage)
    transaction_module = Transaction(storage)

    while True:
        print("\n1. Create Account\n2. Close Account\n3. Check Balance\n4. Deposit\n5. Withdraw\n6. View Transactions\n7. Exit")
        choice = input("Enter your choice: ")

        # Handle different choices
        if choice == '1':
            name = input("Enter your name: ")
            deposit = float(input("Enter initial deposit: "))
            password = input("Enter a password for your account: ")
            print(account_module.create_account(name, deposit, password))
        elif choice == '2':
            acc_num = int(input("Enter your account number: "))
            password = input("Enter your account password: ")
            print(account_module.close_account(acc_num, password))
        elif choice == '3':
            acc_num = int(input("Enter your account number: "))
            password = input("Enter your account password: ")
            print(f"Balance: ${account_module.check_balance(acc_num, password)}")
        elif choice == '4':
            acc_num = int(input("Enter your account number: "))
            amount = float(input("Enter amount to deposit: "))
            print(transaction_module.deposit(acc_num, amount))
        elif choice == '5':
            acc_num = int(input("Enter your account number: "))
            amount = float(input("Enter amount to withdraw: "))
            print(transaction_module.withdraw(acc_num, amount))
        elif choice == '6':
            acc_num = int(input("Enter your account number: "))
            print(transaction_module.view_transactions(acc_num))
        elif choice == '7':
            break

    storage.close()

if __name__ == "__main__":
    main()
