import sys
import re

def validate_card(cardNum):
    cardLen = len(str(cardNum))

    evenSum = 0
    oddSum = 0
    ttlSum = 0
    mulSum = 0

    if cardLen != 13 and cardLen != 15 and cardLen != 16:
        print("\n========ERROR=========")
        sys.exit("INVALID CARD NUMBER")

    for i in range(-2, (-cardLen-1), -2):

        tempMul = int(cardNum[i]) * 2

        if tempMul >= 10:
            evenSum = evenSum + tempMul - 9
        else:
            evenSum = evenSum + tempMul

    for i in range(-1, (-cardLen-1), -2):
        tempOdd = int(cardNum[i])
        oddSum = oddSum + tempOdd

    ttlSum = evenSum + oddSum

    if ttlSum % 2 == 0:
        if int(cardNum[0]) == 3 and int(cardNum[1]) == 4 or int(cardNum[1]) == 7:
            return True

        elif int(cardNum[0]) == 5 and int(cardNum[1]) == 1 or int(cardNum[1]) == 2 or int(cardNum[1]) == 3 or int(cardNum[1]) == 4 or int(cardNum[1]) == 5:
            return True

        elif int(cardNum[0]) == 4:
            return True

        else:
            print("\n========ERROR=========")
            sys.exit("INVALID CARD NUMBER")

def validate_pin(pin):
    # if pin is not a number
    if not int(pin):
        raise ValueError("Pin must be a number from 0-9")

    # if pin length is greater than 4
    if len(pin) > 4:
        raise Exception("Pin must be less than or equal to 4 numbers")

def validate_email(email):
    if matches := re.search(r"^[a-zA-Z0-9.!#$%&\'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", email, re.IGNORECASE):
        pass
    else:
        print("\n========ERROR=========")
        exit("Invalid Email")

def validate_phone_number(phone_number):
    if matches := re.search(r"^(?:\+?61|0)4 ?(?:(?:[01] ?[0-9]|2 ?[0-57-9]|3 ?[1-9]|4 ?[7-9]|5 ?[018]) ?[0-9]|3 ?0 ?[0-5])(?: ?[0-9]){5}$", phone_number, re.IGNORECASE):
        pass
    else:
        print("\n========ERROR=========")
        exit("Invalid Phone Number")


