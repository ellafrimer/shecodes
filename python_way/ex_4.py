"""a list that has the numbers 1-9
multiplied by 100 if they are even"""

# ex_4

new_list = [n * 100 for n in range(1,10) if n % 2 == 0]

# ex_5

list_5 = [n * 100 if n % 2 == 0 else n for n in range(1, 10)]

# 7 Boom list to 99

list_7_boom = ["Boom" if n % 7 == 0 else n for n in range(1,100)]

# ex 7

sum = lambda x, y: x + y

# ex 8

"""one line that gives tupels of joules and calories
joules / 4184 = calories"""

joules = [5000, 8000, 10000, 6000, 12000]
joules_calories = [{x : x / 4184 for x in joules}.items()]

# ex 9
"""one line of code that makes a list of tuples of all
36 combinations of (1,1) to (6,6)
"""
tuples_36 = [(x, y) for x in range(1, 7) for y in range(1, 7)]

#ex 10

languages = ["Html", "JavaScript", "Python", "Ruby"]
python = list(filter(lambda x: x == "Python", languages))

