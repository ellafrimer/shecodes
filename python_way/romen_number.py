"""
a function that takes a romen number and returns its int
"""

def romen_to_int(x):
    result = 0
    number_list = []
    for l in x:
        if l == "I":
            number_list.append(1)
        elif l == "V":
            number_list.append(5)
        elif l == "X":
            number_list.append(10)
        elif l == "L":
            number_list.append(50)
        elif l == "C":
            number_list.append(100)
        elif l == "D":
            number_list.append(500)
        elif l == "M":
            number_list.append(1000)
    for n in number_list:
        if n < number_list[n + 1]:
            number_list[n + 1] = number_list[n + 1] - n
            number_list.remove(n)
        result += n
    return result


print(romen_to_int("X"))

