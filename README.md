# Py🐍ATM

A robust, terminal-based replica of a real-world Automatic Teller Machine (ATM) built with Python.

#### 📺 [Video Demo](https://www.youtube.com/watch?v=92kdkCjyQpY)

---

## 📝 Description
**Py🐍ATM** provides a secure banking environment right in your terminal. It handles everything from account creation and card management to encrypted authentication and real-time email notifications. 

The project is designed to manage multiple users simultaneously, tracking their login history and balances within a local **SQLite** database while maintaining security through encryption.

---

## ✨ Features

### 1. Secure Account Creation
Users can create a new banking profile with built-in protections:
* **Personal Details:** Collects First Name, Last Name, Email, and Phone Number.
* **Validation:** Uses Regex to ensure valid **Australian phone numbers** and standard email formats.
* **Security:** Passwords are masked during entry and stored using **Base64 encryption**.
* **Unique Identity:** Automatically generates a unique account number for every user.

### 2. Card Management & Login
* **Add Card:** Link a card to your profile. Supports **VISA, Mastercard, and AMEX** (validated via the Luhn algorithm).
* **DES Encryption:** PINs are secured using **DES encryption** before storage.
* **Security Logs:** Upon login, the system displays the status and timestamp of the **last three login attempts** (Success/Failure) to alert users of unauthorized access.

### 3. Banking Operations
* **Withdraw:** Remove funds with real-time balance checks.
* **Deposit:** Instant balance updates.
* **EFT (Electronic Funds Transfer):** Transfer money securely to another user using their name and unique account number.
* **Account Info:** A dashboard displaying profile details and current balance.

### 4. Automated Email Receipts
Every transaction triggers an automated email via SMTP. Receipts include:
* Transaction Type & Timestamp.
* Amount processed.
* Balance before and after the transaction.

---

## 🛠️ Technical Stack
* **Language:** Python 3
* **Database:** SQLite (via `cs50` library)
* **UI/UX:** `curses` (Interactive menus) & `bullet` (Masked inputs)
* **Encryption:** `base64` & `DES`
* **Notifications:** `smtplib` & `ssl` (Secure Email)
* **Timezone:** `pytz` (Set to `Australia/Melbourne`)

---

## 🚀 Getting Started

### Prerequisites
You will need Python 3 installed. Install the required dependencies using pip:

```bash
pip install cs50 pytz bullet
InstallationClone the repository:Bashgit clone <your-repository-link>
cd PyATM
Database Setup:Ensure atm.db is initialized in the root directory with the necessary tables (accounts, cards, transactions, last_login).Email Configuration:Open receipt.py and update the email_sender and email_password with your credentials.Note: If using Gmail, you must use an App Password.UsageLaunch the ATM by running:Bashpython project.py
