import os
from email.message import EmailMessage
import ssl
import smtplib
from datetime import datetime, timedelta
import pytz
from cs50 import SQL

db = SQL("sqlite:///atm.db")

time_now = datetime.now(pytz.timezone('Australia/Melbourne'))

# REMEBER TO CHANGE EMAIL RECEIVER TO THE EMAIL FROM ATM DATABASE

def send_receipt(Type, amount, current_balance, new_balance, card_number):
    accounts = db.execute("SELECT * FROM accounts WHERE id=(SELECT account_id FROM cards WHERE card_number = ?)", card_number)

    email_sender = "daasrmalik@gmail.com"
    email_password = 'mwxovnevaqaewnot'
    email_receiver = accounts[0]["email"]

    subject = 'TRANSACTION'
    body = f"""{time_now.strftime("%d/%m/%Y %H:%M:%S")}
Account Number: {accounts[0]["account_number"]}\n
Card Number: {card_number}\n\n
Transaction type: {Type}\n
Amount: ${amount}\n
Balance: ${current_balance}\n
New Balance: ${new_balance}\n\n\n
Py🐍ATM Australia"""
    em = EmailMessage()
    em["FROM"] = email_sender
    em["TO"] = email_receiver
    em["SUBJECT"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


