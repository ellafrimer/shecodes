"""
a function that takes a number as a list of numbers from 1-9
an returns the next number: (5,2)-(5,3) (9,9)-(1,0,0)
"""


def plus_one(digits):
    string = ''.join(map(str, digits))
    new_number = int(string) + 1
    new_digits = list(map(int, str(new_number)))
    return new_digits
