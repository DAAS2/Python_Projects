Py🐍ATM


Video Demo: https://www.youtube.com/watch?v=92kdkCjyQpY
📝 Description
Py🐍ATM is a robust terminal-based replica of a real-world Automatic Teller Machine. It features a secure banking environment with account creation, card management, encrypted authentication, and real-time email notifications for transactions.

The project is designed to handle multiple users, tracking their login history and balances within a local SQLite database while ensuring security through industry-standard encryption methods.

✨ Features
1. Secure Account Creation
Users can create a new banking profile by providing:

Personal Details: First Name, Last Name, Email, and Phone Number.

Validation: Uses Regular Expressions (Regex) to ensure valid Australian phone numbers and standard email formats.

Security: Passwords are masked during entry and stored using Base64 encryption.

Unique Account ID: The system automatically generates a unique account number for every user.

2. Card Management & Login
Add Card: Link a card to your profile by entering a Card Number (supports VISA, Mastercard, and AMEX via Luhn algorithm validation) and a 4-digit PIN.

DES Encryption: PINs are secured using DES encryption before being stored.

Login Tracking: Upon login, the system displays the status, date, and time of the last three login attempts (successful or failed) to alert users of unauthorized access.

3. Banking Operations
Once logged in, users have access to a full suite of ATM functions:

Withdraw: Remove funds from the account (with insufficient funds protection).

Deposit: Add funds to the current balance.

Electronic Funds Transfer (EFT): Transfer money securely to another user’s account using their name and unique account number.

Account Info: View a summary of profile details and current balance.

4. Automated Email Receipts
Every transaction (Withdraw, Deposit, or Transfer) triggers an automated email receipt sent to the user's registered email address. This receipt includes:

Transaction Type

Amount & Timestamp

Balance before and after the transaction

🛠️ Technical Stack
Language: Python 3

Database: SQLite (via cs50 library)

UI/UX: curses for interactive terminal menus and bullet for masked password inputs.

Encryption: base64 and DES.

Notifications: smtplib and ssl for secure email transmission.

Timezone: pytz (configured for Australia/Melbourne).

🚀 Getting Started
Prerequisites
Ensure you have the following Python libraries installed:

Bash

pip install cs50 pytz bullet
Installation
Clone the repository to your local machine.

Ensure atm.db is initialized with the required tables (accounts, cards, transactions, last_login).

Update the email_sender and email_password in receipt.py with your own credentials (use an App Password if using Gmail).

Usage
Run the main program:

Bash

python project.py
📂 File Structure
project.py: The main entry point containing the ATM class and core logic.

validate.py: Regex-based validation for cards, emails, and phone numbers.

interface.py: Logic for the interactive terminal menu system.

last_logins.py: Manages the history and status of user login attempts.

receipt.py: Handles SMTP logic for sending transaction emails.

atm.db: SQLite database storing user and transaction data.
