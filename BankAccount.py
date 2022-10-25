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
        #If the user tries to withdraw an amount that is greater than the current balance, print ”Insufficient funds.” and charge them with an overdraft fee of $10

    def get_balance(self):
        """
        description: Function that displays customer's account balance.
        Parameter: none
        Returns: Current balance.
        """

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