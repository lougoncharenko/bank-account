#create BankAccount class
from random import randint

class BankAccount():
    def __init__(self, full_name):
        self.full_name = full_name
        self. account_number = self.random_account_number(8)
        self.balance = 0

    def random_account_number(self, n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        self.account_number = randint(range_start, range_end)
        return self.account_number

    def deposit(self, amount):
        """
        description: Function that adds an amount to the customer's balance
        Parameter: Amount
        Returns: A message with new balance.
        """
        self.balance = self.balance + amount
        print(f'“Amount deposited: ${amount} new balance: ${self.balance}”')
        return self.balance
    
    def withdraw(self, amount):
        """
        description: Function that subtracts an amount from the customer's balance
        Parameter: Amount
        Returns: A message with amouitn withdrawn and new balance
        """
        self.balance = self.balance - amount
        if self.balance < 0:
            print('Insufficient funds.')
            self.balance = self.balance - 10
            return self.balance
        else:
            return self.balance

    def get_balance(self):
        """
        description: Function that displays customer's account balance.
        Parameter: none
        Returns: Current balance.
        """
        return self.balance

    def add_interest(self):
        """
        description: Function that adds interest to customer's balance
        Parameter: none
        Returns: current balance with interest
        """
        interest = self.balance * 0.00083
        self.balance = self.balance + interest
        return self.balance

    
    def print_statement(self):
        """
        description: Function that adds interest to customer's balance
        Parameter: Amount
        Returns: A message with account_name, account_number and balance.
        """
        print(f'{self.full_name}\n {self.account_number}\n {self.balance}')
      
#Define 3 different bank account examples using the BankAccount() object.
John_account = BankAccount('John Thomas')
John_account.deposit(700)
John_account.print_statement()
# John_account.deposit(800)
# John_account.print_statement()
# John_account.withdraw(100)
# John_account.print_statement()
