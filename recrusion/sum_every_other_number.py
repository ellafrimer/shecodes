def sum_every_other_number(n):
    """Return the sum of every other natural number
    up to n, inclusive.

    >>> sum_every_other_number(8)
    20
    >>> sum_every_other_number(9)
    25
    """
    if n <= 0:
        return 0
    else:
        return n + sum_every_other_number(n - 2)
