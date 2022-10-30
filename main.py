from BankAccount import BankAccount

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