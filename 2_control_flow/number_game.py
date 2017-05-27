from random import randint


def number_game():
    answer = input("Guess a number ")
    int_answer = int(answer)
    random_number = randint(0, 100)

    if random_number == int_answer:
        print("You win!")
    elif random_number > int_answer:
        print("Your number is too low.")
    elif random_number < int_answer:
        print("Your number is too high.")

    print("The number was %d" % random_number)

number_game()
