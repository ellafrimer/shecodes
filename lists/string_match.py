def string_match(a, b):
    """
    do a loop that takes a letter and the one after it from string a
    and see if it matches that same position in string b
    if it does count it. return the count
    """

    total = 0
    index = 0

    for letter in a:
        if index + 1 < len(a):
            sub_str = letter + a[index + 1]
            if b[index:index + 2] == sub_str:
                total += 1
        index += 1

    return total


def string_match_alt(a, b):
    shorter = min(len(a), len(b))
    total = 0

    for index in range(shorter - 1):
        a_sub_str = a[index:index + 2]
        b_sub_str = b[index:index + 2]

        if b_sub_str == a_sub_str:
            total += 1

    return total

print(string_match_alt('xxcaazz', 'xxbaaz'))
print(string_match_alt('abc', 'abc'))
print(string_match_alt('abc', 'axc'))