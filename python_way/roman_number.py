"""
a function that takes a roman number and returns its int
"""


def roman_to_int(x):
    """jhg

    >>> roman_to_int("XV")
    15
    >>> roman_to_int("III")
    3
    >>> roman_to_int("IV")
    4
    >>> roman_to_int("CM")
    900
    """
    letter_value = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
    result = 0
    for (i, s) in enumerate(x):
        if (i + 1) < len(x):
            next_letter = x[i + 1]
            if letter_value[s] < letter_value[next_letter]:
                result -= letter_value[s]
            else:
                result += letter_value[s]
        else:
            result += letter_value[s]
    return result
