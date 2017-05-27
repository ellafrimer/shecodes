def first_is_last(list):
    total = 0
    for s in list:
        if len(s) >= 2 and s[0] == s[-1]:
            total = total + 1
    print(total)

ex = ["aba", "xyz", "aa", "x", "bbb"]
first_is_last(ex)

ex_2 = ["x", "xy", "xyx", "xx", ""]
first_is_last(ex_2)
