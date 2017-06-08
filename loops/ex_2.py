"""
make a program that takes number_game from lesson 2
and every time the user gusses the right number
you win and the game stops
"""

from random import randint
random_number = randint(0, 11)
print(random_number)

def number_game():
    answer = input("Guess a number ")
    int_answer = int(answer)

    if random_number == int_answer:
        print("You win!")
    elif random_number > int_answer:
        print("Your number is too low.")
    elif random_number < int_answer:
        print("Your number is too high.")

    print("The number was %d" % random_number)



