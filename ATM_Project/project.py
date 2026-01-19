from sys import exit
from validate import validate_card, validate_pin, validate_email, validate_phone_number
from bullet import Password
from cs50 import SQL
import base64
from interface import menu
from time import sleep
from des import DES
import os
from random import randint
from last_logins import last_login, display_logins, add_first_login
from receipt import send_receipt

db = SQL("sqlite:///atm.db")

accounts = {}

class ATM:
    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.pin = pin
        self.balance = 0

    def __str__(self):
        return f"{self.balance}"

    def withdraw(self, money):
        if money > self.balance:
            print("Not enough money in account")
            sleep(.7)
            return 1
        self.balance -= money

    def deposit(self, money):
        self.balance += money

    def change_pin(self, pin):
        return pin

    def receipt(self):
        pass

def main():
    os.system("clear")
    while True:
        if menu('Py🐍ATM', ['Create Account','Login'], 'blue') == 0:
            os.system('clear')
            add_card(*create_account())
            sleep(1.5)
            continue
        else:
            break

    os.system('clear')
    print("\n========Login In=========")

    # login user
    card, pin = login()
    os.system('clear')
    accounts["card"] = card
    accounts["pin"] = pin
    account = ATM(card, pin)
    balance = db.execute("SELECT balance FROM cards WHERE card_number = ? AND PIN = ?", card, pin)
    account.balance = balance[0]["balance"]
    print("\nLogging in")
    sleep(.7)
    os.system('clear')

    # display latest logins to user
    display_logins(card, pin)
    os.system('clear')

    while True:
        os.system('clear')
        atm_options = menu('Py🐍ATM options', ['Withdraw','Deposit', 'Electronic Funds Transfer', 'Account Info', 'Exit'], 'blue')

        # Withdraw money
        if atm_options == 0:
            withdraw(account)
            continue

        # Deposit money
        if atm_options == 1:
            deposit(account)
            continue

        # Transfer money into a different account
        if atm_options == 2:
            transfer(account)
            continue

        # Account Info
        if atm_options == 3:
            info(account)
            continue

        # exit ATM
        if atm_options == 4:
            exit("Thank you for using our Py🐍ATM! 🙋")


# withdraw money from account
def withdraw(account):
    print("\n========Withdraw=========")
    # check if valid amount
    try:
        withdraw = float(input("How much money would you like to withdraw? "))
    except ValueError:
        exit("INVALID AMOUNT")

    # if withdraw amount > balance
    if account.withdraw(withdraw) == 1:
        sleep(.7)
        print("Not enough money in your account")
    # if withdraw amount is < balance
    else:
        sleep(.7)
        print(f"You have succefully withdrawed ${withdraw} from your account")

        # insert transaction record for user and email receipt
        reciept = db.execute("INSERT INTO transactions (type, amount, current_balance, new_balance, card_number) VALUES(?, ?, ?, ?, ?)", "Withdraw", withdraw, account.balance+withdraw, account.balance, account.card_number)
        send_receipt("Withdraw", withdraw, account.balance+withdraw, account.balance, account.card_number)

        # withdraw money from account database
        withdraw = db.execute("UPDATE cards SET balance=balance-? WHERE card_number = ? and pin = ?", withdraw, account.card_number, account.pin)
        sleep(1.5)

        # display balance
        balance = db.execute("SELECT * FROM cards where card_number = ? and pin = ?", account.card_number, account.pin)
        print(f"Your balance is ${balance[0]['balance']}")
        sleep(2.5)

        return True

# deposit money into account
def deposit(account):
    print("\n========Deposit=========")
    # check if valid amount
    try:
        deposit = float(input("How much money would you like to deposit? "))
    except ValueError:
        exit("Invalid Amount")

    # deposit process
    account.deposit(deposit)
    sleep(.7)
    print(f"You have succefully deposited ${deposit} to your account")

    # insert transaction record for user and email receipt
    reciept = db.execute("INSERT INTO transactions (type, amount, current_balance, new_balance, card_number) VALUES(?, ?, ?, ?, ?)", "Deposit", deposit, account.balance-deposit, account.balance, account.card_number)
    send_receipt("Deposit", deposit, account.balance-deposit, account.balance, account.card_number)

    # deposit money into user account
    deposit = db.execute("UPDATE cards SET balance=balance+? WHERE card_number = ? and pin = ?", deposit, account.card_number, account.pin)
    sleep(1.5)

    # display balance
    balance = db.execute("SELECT * FROM cards where card_number = ? and pin = ?", account.card_number, account.pin)
    print(f"Your balance is ${balance[0]['balance']}")
    sleep(2.5)

    return True

# tranfer money into a different account
def transfer(account):
    print("\n========Electronic Funds Transfer=========")
    # get info for transfer
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    account_number = input("Account Number: ")

    # check if account exists with the information given
    check = db.execute("SELECT * FROM accounts WHERE first_name = ? AND last_name = ? AND account_number = ?", first_name, last_name, account_number)
    if not check:
        print("\n========ERROR=========")
        exit("Invalid Account number or Invalid name")
    else:
        pass

    # transfer amount
    try:
        transfer = float(input("How much money would you like to transfer? "))
    except ValueError:
        exit("INVALID AMOUNT")

    # if transfer money > balance
    if account.withdraw(transfer) == 1:
        sleep(.7)
        print("Not enough money in your account")

    # if transfer money < balance
    else:
        sleep(.7)
        # transfer money to other person
        db.execute("UPDATE cards SET balance=balance+? WHERE account_id=(SELECT id FROM accounts WHERE account_number=?)", transfer, account_number)

        # get info from other person to add transaction record and email receipt
        other = db.execute("SELECT * FROM cards where account_id=(SELECT id FROM accounts WHERE account_number=?)", account_number)
        db.execute("INSERT INTO transactions (type, amount, current_balance, new_balance, card_number) VALUES(?, ?, ?, ?, ?)", "Transfer", transfer, other[0]["balance"]-transfer, other[0]["balance"], other[0]["card_number"])
        send_receipt("Transfered to", transfer, other[0]["balance"]-transfer, other[0]["balance"], other[0]["card_number"])

        # insert transaction record for user and email receipt
        db.execute("INSERT INTO transactions (type, amount, current_balance, new_balance, card_number) VALUES(?, ?, ?, ?, ?)", "Transfer", transfer, account.balance+transfer, account.balance, account.card_number)
        send_receipt("Transfered from", transfer, account.balance+transfer, account.balance, account.card_number)

        # succesfully transfered money
        print(f"You have succesfully transfered ${transfer} from your account to {first_name} {last_name}")
        withdraw = db.execute("UPDATE cards SET balance=balance-? WHERE card_number = ? and pin = ?", transfer, account.card_number, account.pin)
        sleep(1.5)

        # display balance
        balance = db.execute("SELECT * FROM cards where card_number = ? and pin = ?", account.card_number, account.pin)
        print(f"Your balance is ${balance[0]['balance']}")
        sleep(2.5)

        return True


# display account info
def info(account):
    print("\n========Account Info=========")
    info = db.execute("SELECT * FROM accounts WHERE id=(SELECT account_id FROM cards WHERE card_number = ? AND pin = ?)", account.card_number, account.pin)
    print("First Name: ", info[0]["first_name"])
    print("Last Name: ", info[0]["last_name"])
    print("Email: ", info[0]["email"])
    print("Phone Number: ", info[0]["phone_number"])
    print("\nAccount Number: ", info[0]["account_number"])
    balance = db.execute("SELECT * FROM cards where card_number = ? and pin = ?", account.card_number, account.pin)
    print("\nBALANCE: $", balance[0]["balance"])
    sleep(5)

# create an account for user
def create_account():
    print("\n========Create Account=========")
    # get personal details for account
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    password = Password(prompt="Password: ", hidden="*")
    password = password.launch()
    confirm_password = Password(prompt="Password Confirmation: ", hidden="*")
    confirm_password = confirm_password.launch()

    # check if password is the same as confirmation password
    if confirm_password != password:
        exit("Passoword was wrong! ")

    # encrypt password
    password = base64.b64encode(password.encode("utf-8"))

    # validate email and phone number
    email = input("Email: ")
    validate_email(email)
    phone_number = input("Phone Number: ")
    validate_phone_number(phone_number)

    # check if account already exits by their first and last name
    check_account = db.execute("SELECT * FROM accounts WHERE first_name = ? AND last_name = ?", first_name, last_name)

    # if account does not exist
    if not check_account:
        result = db.execute("INSERT INTO accounts (first_name, last_name, password, email, phone_number) VALUES(?, ?, ?, ?, ?)", first_name, last_name, password, email, phone_number)
        add_first_login(first_name, last_name)
        account_number(first_name, last_name, email, phone_number)


    # if account exits
    if check_account:
        if first_name == check_account[0]["first_name"]:
            print("\n========ERROR=========")
            exit(f"Account already exits with the name of {first_name} {last_name}")

    return first_name, last_name

# create a unique account number
def account_number(first_name, last_name, email, p_num):
    phone_number = p_num[5] + p_num[6] + p_num[7] + p_num[8]
    email = email.split("@")
    account_number = phone_number + str(len(email[0])) + str(randint(100, 999))
    insert = db.execute("UPDATE accounts SET account_number=? WHERE first_name = ? and last_name = ?", account_number, first_name, last_name)
    return True


# add a card to the account
def add_card(first_name, last_name):
    os.system('clear')
    print("\n========Add Card=========")

    # ask for card_number and pin
    card_number = input("Card Number: ")
    pin = Password(prompt="PIN: ", hidden="*")
    pin = pin.launch()
    validate_pin(pin)
    pin = DES(pin)

    # Insert card number and pin into database with the same id as the user
    db.execute("INSERT INTO cards(card_number, pin, balance) VALUES(?, ?, 0)", card_number, pin)
    db.execute("UPDATE cards SET account_id=(SELECT id FROM accounts WHERE first_name = ? and last_name = ?) WHERE card_number = ? AND pin = ?", first_name, last_name, card_number, pin)
    sleep(.7)
    print("Card has been added to your account!")
    sleep(.5)

    return True

# login into account
def login():
    # get card number and check if valid
    card_number = input("Input Card Number: ")
    validate_card(card_number)

    # hide pin and check if valid pin
    pin = Password(prompt="PIN: ", hidden="*")
    pin = pin.launch()
    validate_pin(pin)
    pin = DES(pin)

    # check if card_number and pin exit on database
    check_account = db.execute("SELECT * from accounts where id = (SELECT account_id from cards where card_number = ? and pin = ?)", card_number, pin)
    id = db.execute("SELECT * from accounts where id = (SELECT account_id from cards where card_number = ?)", card_number)

    # if incorrect pin or card number
    if not check_account:
        # insert into last login database
        last_login("\033[1;31;40m UNSUCCESSFUL", id[0]["id"])
        exit("INVALID CARD NUMBER OR PIN")

    # insert into last login database
    last_login("\033[1;32;40m SUCCESSFUL", id[0]["id"])

    return card_number, pin

def something(name):
    return name

def something1(email):
    return email

if __name__ == "__main__":
    main()

