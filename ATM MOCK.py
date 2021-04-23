import random
import re
from datetime import datetime

now = datetime.now()
database = {}


def welcome():
    try:
        print("********** Welcome to Debby's World Bank ***********")
        print("1. Existing Customer\n 2. New Customer\n")

        User_input = int(input("\nSelect Option: \n\t >"))

        if User_input == 1:

            existing_customers()
        elif User_input == 2:

            register()

        else:
            print("You have selected invalid option")
            welcome()
    except ValueError:
        print('\nEnter an Integer!!\n\t>')
        welcome()


def register():
    print("****** Please Fill in Your Details Correctly!!! *******")
    first_name = input("\nWhat is your first name?\n\t>")
    last_name = input("\nWhat is your last name?\n\t>")
    pin = input("\nCreate a Strong Pin: \n\t>")
    confirm_pin = input('\nRe-Enter pin: \n\t>')
    if len(pin) < 8:
        print("Password must be 8 characters long.")
        register()
    elif re.search('[A-Z]', pin) is None:
        print("Password Must Contain @least 1 Uppercase Letter")
        register()

    elif re.search('[0-9]', pin) is None:
        print("Password Must Contain @least 1 Number")
        register()

    elif re.search('[!@#$%^&*<>]', pin) is None:
        print("Password Must Contain @least 1 Special Character ")
        register()

    else:
        if pin != confirm_pin:
            print("\nPasswords do not match, Try Again!\n\t>")
            register()

    email = input('Enter Your email address:  \n\t>')
    if re.search(r"([\w-]+)@([\w-]+)(\.[\w-]+)", email):
        print("Email is valid!")
    else:
        print('\nInvalid Email, Try Again!!\n\t>')
        register()

    accountNumber = generate_account_number()
    database[accountNumber] = [first_name, last_name, pin, email]
    database.update({"balance": 0.00})

    print("Your Account Has been created Successfully!")
    print("***********")
    print("Your Account Details:")
    print("Account Number:\t %d" % accountNumber)
    print("Full Name:\t " + first_name.title() + " " + last_name.title())
    print("Thank you for choosing us")
    print("_______________" * 4)
    print("\n")
    login()


def login():
    print("********* Login ***********")
    accountNumberFromUser = int(input("\nEnter your account number:  \n\t"))
    User_pin = input("\nEnter your pin:  \n\t>")
    for accountNumber, user_details in database.items():
        if accountNumber == accountNumberFromUser:

            if user_details[2] == User_pin:
                bank_operation(user_details)


def generate_account_number():
    return random.randrange(1111111111, 9999999999)


def bank_operation(user_details):
    print("***********" * 4)
    print("Log in Successful!")
    print("***********" * 4)
    print("Welcome, Please select an option")

    print("***********" * 4)

    print("*********" * 4)
    print('Banking Option:')
    print('1. Withdrawal')
    print('2. Deposit')
    print('3. Balance')
    print('4. Exit')
    print("*********" * 4)
    selected_option = int(input('Please select an Option: '))
    print("*********" * 4)

    if selected_option == 1:
        withdrawalOperation()
        bank_operation(user_details)

    elif selected_option == 2:
        depositOperation()
        bank_operation(user_details)
    elif selected_option == 3:
        balance()
        bank_operation(user_details)
    elif selected_option == 4:
        exist()
        bank_operation(user_details)

    else:

        print("Invalid option selected")
        bank_operation(user_details)


def balance():
    database.get("balance")
    print("Your balance is N %i \nDeposit Transaction Completed" % database["balance"])
    exist()


def withdrawalOperation():
    amount = int(input("Enter Amount: "))
    acc_balance = database.get("balance")
    if amount < acc_balance:
        bal = acc_balance - amount
        database["balance"] = bal
        print("Take Your Cash: ")
        print("Your balance is N %i \nWithdrawal Transaction Completed" % database["balance"])
    else:
        if amount > acc_balance:
            print('Insufficient funds!!!')
    exist()


def depositOperation():
    print("Deposit Operations")
    database.get("balance")
    bal = database.get("balance")
    amt = int(input("Enter amount: "))
    bal = amt + bal
    database["balance"] = bal
    print("Your balance is N %i \nDeposit Transaction Completed" % database["balance"])
    exist()


def existing_customers():
    name = input('\nEnter your Name:  \n\t>')
    allowed_users = ['Debby', 'Rhemy', 'Divine']
    allowed_password = ['Big', 'Bigger', 'Biggest']
    account_balance = [10000, 20000, 30000]
    if name in allowed_users:
        password = input('\nEnter password. \n\t>')
        user_Id = allowed_users.index(name)
        if password == allowed_password[user_Id]:
            print('Welcome %s' % name)
            print("Current date and time : ")
            print(now.strftime("%Y-%B-%d %H:%M:%S"))
            print('This are the available options')
            print('1. Withdrawal')
            print('2. Deposit')
            print('3. Complain')
            select_option = int(input('\nSelect an option: \n\t>'))
            if select_option == 1:
                withdraw = int(input('\nHow much will you like to withdraw? \n\t>'))
                if withdraw <= account_balance[user_Id]:
                    print('Transaction Successful! \n')
                    exist()
                else:
                    print('insufficient funds \n')
                    exist()
            elif select_option == 2:
                deposit = int(input('How much will you like to deposit? \n'))
                account_balance[user_Id] += deposit
                print('Current balance is %s' % account_balance[user_Id])
            elif select_option == 3:
                complain = input('What issue will you like to report? \n')
                print('Thank you for contacting us. \n')
                exist()
            else:
                print('Invalid option selected, Please Try again')
                existing_customers()
        else:
            print('Incorrect password, Try again')
            existing_customers()
    else:
        print('Name not found, Try again')
        existing_customers()


def exist():
    print("""Do you want to perform another transaction
    1. Yes \n 2. No \n""")
    log_out = int(input('\nSelect Option: 1 0r 2 \n\t>'))
    if log_out == 1:
        welcome()
    else:
        if log_out == 2:
            print('Thank you for banking with us, Please call again!!!')


welcome()
