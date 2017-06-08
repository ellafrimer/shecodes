def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(int(n))

    if n == 1:
        return 1
    elif n % 2 == 0:
        n_next = n / 2
    elif n % 2 != 0:
        n_next = n * 3 + 1

    return 1 + hailstone(n_next)


def hailstone_list(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> hailstone_list(10)
    [10, 5, 16, 8, 4, 2, 1]
    """

    if n == 1:
        return [1]
    elif n % 2 == 0:
        n_next = n / 2
    elif n % 2 != 0:
        n_next = n * 3 + 1

    return [int(n)] + hailstone_list(n_next)