#create BankAccount class
class BankAccount():
    def __init__(self, full_name, account_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = 0

    def deposit(self, amount):
        """
        description: Function that adds an amount to the customer's balance
        Parameter: Amount
        Returns: A message with new balance.
        """
        self.balance = self.balance + amount
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
    
    def print_statement(self):
        """
        description: Function that adds interest to customer's balance
        Parameter: Amount
        Returns: A message with account_name, account_number and balance.
        """
      
#Define 3 different bank account examples using the BankAccount() object.