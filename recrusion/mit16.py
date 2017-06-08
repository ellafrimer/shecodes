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
    if n == 0:
        return 0
    print(n)
    return print_to_0(n - 1)


print_to_0(10)
