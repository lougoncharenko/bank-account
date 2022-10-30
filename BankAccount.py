#create BankAccount class
from random import randint

def generate_account_number(n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        account_number = randint(range_start, range_end)
        return account_number

random_account_number = generate_account_number(8)

class BankAccount():
    def __init__(self, full_name, account_number = random_account_number, balance = 0):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """
        description: Function that adds an amount to the customer's balance
        Parameter: Amount
        Returns: A message with new balance.
        """
        self.balance = self.balance + amount
        print(f'Amount deposited: ${amount} new balance: ${self.balance} \n')
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
            print(f'Amount withdrawn: ${amount} new balance: ${self.balance} \n')
            return self.balance

    def get_balance(self):
        """
        description: Function that displays customer's account balance.
        Parameter: none
        Returns: Current balance.
        """
        print(f'Your current balance is: ${self.balance}')

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
      





