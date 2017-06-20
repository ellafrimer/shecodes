def two_numbers(x, y):
    """taking tow numbers that will
    recursively multiply"""

    if y == 0:
        return 0
    return two_numbers(x, y - 1) + x


def times(base, exp):
    """a recursive that takes a base and ** with the exp"""
    if exp == 0:
        return 1
    return times(base, exp - 1) * base


def print_to_0(n):
    """a function using recursion to print from n to 0"""
    print(n)
    if n == 0:
        return 0

    return print_to_0(n - 1)


def print_to_n(n):
    """a function using recursion to print from 0 to n"""
    if n < 0:
        return 0
    print_to_n(n - 1)
    print(n)

def reverse_string(str):
    """a function using recursion that prints the
    string backwards"""
    if str == str[0]:
        return str
    return str[-1] + reverse_string(str[:-1])

def is_prime(n):
    if n == 1:
        return True
    elif n % (n - 1) == 

print(is_prime(3))
