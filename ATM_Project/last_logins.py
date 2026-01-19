from datetime import datetime, timedelta
import pytz
from cs50 import SQL
from time import sleep

db = SQL("sqlite:///atm.db")

def add_first_login(first_name, last_name):
    id = db.execute("SELECT * FROM accounts WHERE first_name = ? AND last_name = ?", first_name, last_name)
    time_now = datetime.now(pytz.timezone('Australia/Melbourne'))
    text = "\033[1;32;40m SUCCESSFUL"
    insert = db.execute("INSERT INTO last_login (login_3, status3, account_id) VALUES(?,?,?)", time_now.strftime("%d/%m/%Y %H:%M:%S"), text, id[0]["id"])

def last_login(status, id):

    time_before = db.execute("SELECT * from last_login where account_id=?", id)

    date, time = time_before[0]["login_3"].split(" ")

    hour, minute, second = time.split(":")
    day, month, year = date.split("/")

    time_now = datetime.now(pytz.timezone('Australia/Melbourne'))

    if time_now.day > int(day) or time_now.month > int(month) or time_now.year > int(year) or time_now.hour > int(hour) or time_now.minute > int(minute) or time_now.second > int(second):
        db.execute("UPDATE last_login SET login_1 = ? WHERE account_id = ?", time_before[0]["login_2"], id)
        db.execute("UPDATE last_login SET status_1 = ? WHERE account_id = ?", time_before[0]["status_2"], id)
        db.execute("UPDATE last_login SET login_2 = ? WHERE account_id = ?", time_before[0]["login_3"], id)
        db.execute("UPDATE last_login SET status_2 = ? WHERE account_id = ?", time_before[0]["status3"], id)
        db.execute("UPDATE last_login SET login_3 = ? WHERE account_id = ?", time_now.strftime("%d/%m/%Y %H:%M:%S"), id)
        db.execute("UPDATE last_login SET status3 = ? WHERE account_id = ?", status , id)

def display_logins(card, pin):
    logins = db.execute("SELECT * FROM last_login WHERE account_id=(SELECT account_id from cards WHERE card_number = ? and pin = ?)", card, pin)
    print(f"\033[0;37;40m Latest Login: {logins[0]['login_3']} STATUS: {logins[0]['status3']}")
    print(f"\033[0;37;40m 2nd latest Login: {logins[0]['login_2']} STATUS: {logins[0]['status_2']}")
    print(f"\033[0;37;40m Oldest Login: {logins[0]['login_1']} STATUS: {logins[0]['status_1']}")
    sleep(3)
    print("\033[0;37;40m \033[0m 0;30;47m", end="")
