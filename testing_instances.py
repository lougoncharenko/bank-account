from BankAccount import BankAccount

# This section is where you run the code to test the instances of the bank class

################  JOHN EXAMPLE ################################
John_account = BankAccount('John Thomas')
John_account.deposit(700)
John_account.deposit(800)
John_account.withdraw(100)
John_account.print_statement()
John_account.withdraw(1500)
John_account.print_statement()


################  Mitchell EXAMPLE ################################
Mitchell_account = BankAccount('Mitchell Anderson', account_number = 13141592)
Mitchell_account.print_statement()
Mitchell_account.deposit(400000)
Mitchell_account.print_statement()
Mitchell_account.add_interest()
Mitchell_account.print_statement()
Mitchell_account.withdraw(150)
Mitchell_account.print_statement()


################  Cindy EXAMPLE ################################
Cindy_account = BankAccount('Cindy Fuller', balance = 500)
Cindy_account.get_balance()
Cindy_account.add_interest()
Cindy_account.print_statement()
Cindy_account.deposit(1000)

