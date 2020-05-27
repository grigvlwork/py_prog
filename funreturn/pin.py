from math import sqrt


def simple(number):
    if number == 1:
        return False
    if number == 2:
        return True
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def palindrome(s):
    if s == s[::-1]:
        return True
    return False


def is2(number):
    n = 2
    while n < number:
        n *= 2
    if n == number:
        return True
    return False


def check_pin(pinCode):
    a = int(pinCode[:pinCode.find('-')])
    b = pinCode[pinCode.find('-') + 1:pinCode.rfind('-')]
    c = int(pinCode[pinCode.rfind('-') + 1:])
    if simple(a) and palindrome(b) and is2(c):
        return 'Корректен'
    return 'Некорректен'
