# the game 7 boom


def computer_turn(number):
    if number % 7 == 0:
        print("boom")
    else:
        print(number)


def human_turn(number):
    answer = input("Next number: ")
    if number % 7 == 0 and answer == "boom":
        return True
    elif number % 7 != 0 and int(answer) == number:
        return True
    else:
        return False


turn = 0
for number in range(1,21):
    if turn == 0:
        turn = 1
        computer_turn(number)
    else:
        turn = 0
        if human_turn(number) == False:
            print("You lose!")
            break

