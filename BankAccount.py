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
John_account = BankAccount('John Thomas', 10000001, 0)
John_account.deposit(700)
John_account.print_statement()
John_account.deposit(800)
John_account.print_statement()
John_account.withdraw(100)
John_account.print_statement()