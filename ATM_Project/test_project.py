from project import withdraw, deposit, transfer, add_card, account_number, something, something1

def test_function_1():
    assert account_number("Saad", "Malik", "daasrmalik@gmail.com", "0451726410") == True


def test_function_2():
    assert something("Saad") == "Saad"


def test_function_n():
    assert something1("jeff@gmail.com") == "jeff@gmail.com"