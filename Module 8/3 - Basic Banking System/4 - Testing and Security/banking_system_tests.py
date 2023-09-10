import unittest
from unittest.mock import patch
from banking_system import DataStorage, Account, Transaction

class TestBankingSystem(unittest.TestCase):
    def setUp(self):
        # Use an in-memory database for testing
        self.storage = DataStorage(":memory:")
        self.account_module = Account(self.storage)
        self.transaction_module = Transaction(self.storage)

    def test_create_account(self):
        response = self.account_module.create_account("John", 1000, "pass123")
        self.assertEqual(response, "Account created successfully!")
    
    def test_check_balance(self):
        self.account_module.create_account("John", 1000, "pass123")
        balance = self.account_module.check_balance(1, "pass123")
        self.assertEqual(balance, 1000)
    
    def test_deposit(self):
        self.account_module.create_account("John", 1000, "pass123")
        response = self.transaction_module.deposit(1, 500)
        self.assertEqual(response, "Deposited $500 to account 1")
        new_balance = self.account_module.check_balance(1, "pass123")
        self.assertEqual(new_balance, 1500)
    
    def test_withdraw(self):
        self.account_module.create_account("John", 1000, "pass123")
        response = self.transaction_module.withdraw(1, 500)
        self.assertEqual(response, "Withdrew $500 from account 1")
        new_balance = self.account_module.check_balance(1, "pass123")
        self.assertEqual(new_balance, 500)
    
    def test_insufficient_funds(self):
        self.account_module.create_account("John", 1000, "pass123")
        response = self.transaction_module.withdraw(1, 1500)
        self.assertEqual(response, "Insufficient funds")

    def test_close_account(self):
        self.account_module.create_account("John", 1000, "pass123")
        response = self.account_module.close_account(1, "pass123")
        self.assertEqual(response, "Account closed successfully!")
    
    def test_view_transactions(self):
        self.account_module.create_account("John", 1000, "pass123")
        self.transaction_module.deposit(1, 500)
        self.transaction_module.withdraw(1, 200)
        response = self.transaction_module.view_transactions(1)
        self.assertTrue("deposit: $500" in response)
        self.assertTrue("withdraw: $200" in response)

    def tearDown(self):
        self.storage.close()

if __name__ == "__main__":
    unittest.main()
