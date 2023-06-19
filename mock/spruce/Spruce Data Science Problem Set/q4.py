# Spruce Data Science Problem Set
# Question 4


import unittest
import uuid

class TestSpruceQ4(unittest.TestCase):
    """
    Question 4 Unit Test for the 4 unit tests outlined in the readme
    """
    def test_initial_balance(self):
        account = BankAccount("John Doe",1000)
        self.assertEqual(account.get_balance(),1000)

    def test_set_balance(self):
        account = BankAccount("John Doe",1000)
        account.set_balance(2000)
        self.assertEqual(account.get_balance(),2000)

    def test_deposit(self):
        account = BankAccount("John Doe",1000)
        account.deposit(500)
        self.assertEqual(account.get_balance(),1500)

    def test_withdrawal(self):
        account = BankAccount("John Doe",1000)
        account.deposit(500)
        account.withdraw(200)
        self.assertEqual(account.get_balance(),1300)
    
    def test_withdrawal_insufficient_funds(self):
        account = BankAccount("John Doe",1000)
        account.set_balance(1300)
        
        self.assertEqual(account.withdraw(1500),'Insufficient Funds')
    

class BankAccount:
    def __init__(self, name, initial_balance = 0.0):
        """
        Initializes the bank account with the given `name` and initial_balance.
        """
        self.name = name
        self.balance = initial_balance
        self.account_number = uuid.uuid3(uuid.NAMESPACE_DNS,name)

    def get_balance(self):
        """
        Returns the current account balance.
        """
        return self.balance
    
    def deposit(self, amount):
        """
        Adds the given `amount` to the account balance.
        """
        self.balance += amount 

    def withdraw(self, amount):
        """
        Subtracts the given `amount` from the account balance.
        """
        if amount <= self.balance:
            self.balance -= amount
        else:
            return 'Insufficient Funds'

    def set_balance(self,balance):
        """
        Set the bank account with a given balance after initialization
        FOR INTERNAL BANK USE ONLY :) 
        """
        self.balance = balance


if __name__ == "__main__":
    unittest.main(argv=[''],verbosity=2,exit=False)
