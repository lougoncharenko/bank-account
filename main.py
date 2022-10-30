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


# Stretch Challenge: Create an Application
def run_bank_application():
    print('Welcome to your bank account')
    account_name = input('Enter your full name: ')
    valid_option = False
    while(valid_option == False):
        account_number = input('Enter your 8-digit account number: ')
        if (len(account_number) == 8):
            break
        else: 
            print('Not a valid 8 digit number, try again.')
    account_number = int(account_number)
    account_balance = int(input('Enter a balance to initiate account with: '))
    new_account = BankAccount(account_name, account_number, account_balance)

    program_exit = False
    while(program_exit == False):
        option = input('Choose the following options.\n Enter 1 to print statement\n Enter 2 to deposit money.\n Enter 3 to withdraw. \n Enter 4 to exit the applicaton.')
        if (option == '1'):
            new_account.print_statement()
        elif (option == '2'): 
            deposit = int(input('Enter an amount to deposit: '))
            new_account.deposit(deposit)
        elif (option == '3'):
            withdrawl_amount= int(input('Enter an amount to withdraw: '))
            new_account.withdraw(withdrawl_amount)
        elif (option == '4'):
            break
        else: 
            print('Not a valid option. Choose 1, 2, 3, or 4. ')

run_bank_application()
