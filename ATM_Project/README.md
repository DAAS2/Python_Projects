 # Py🐍ATM
#### Video Demo:  <https://www.youtube.com/watch?v=92kdkCjyQpY>
#### Description:
This project is a replica of an ATM it works and functions like a normal atm would. My firt function is create_account() this functions allows the user to make an account and takes the following information first name, last name, password, confirmation password, email, and phone number it masks the password so that other people can't see your password when youn type it in this functions also validates the email and phone number using regular expressions, and also encrypts the password using base64, the phone number must be an Australian number. The function also checks to see if there is an account with the same first and last name. The program then inserts into a accounts table all the information. The function also creates a unique account number that is special for every user.

After that there is a add_card() function that adds a card to your account it asks for card_number and pin and validates the card_number, it can only accept VISA, MASTERCARD, AMEX. It also validates pin and encrypts the pin using DES encryption. After that you go to the home screen and login in you input your card number and pin then the program checks if there is a card number and pin that matches to the persons account and logs you in. The program then displays the last 3 logins it provides the date and time, and the status of the login. The ATM program has 5 main functions withdraw(), deposit(), EFT(Electronic funds transfer), Account Info.

The withdraw function withdraw money from your account then returns your balance after withdrawing if the amount is more than your balance it then displays an error message and exits. The withdraw function takes in account which is a class that contains the users card_number, pin, balance.

The deposit function deposits money into your account then returns your balance after depositing the money, it will display an error if you input the wrong amount. The deposit function also takes in acount which contains the users card_number, pin and balance.

The EFT(Electronic Funds Transfer) function allows you to transfer money into a different account it requires you to input the persons first name, last name, and the unique account number. It will then prompt your to list your amount to transfer.

After making different transactions the ATM has a function which will email you your receipt, this receipt contains your account number, card_number, amount you inputted in the transaction, balance before transaction and new balance. This will then email you all this information including the date and time of the transaction.

The program also has a account_info function which displays all your account info, first name, last name, email, phone number, account number and also your current balance.