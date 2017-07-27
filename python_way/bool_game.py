"""
bool is a game were one player gives a 5 letter str and the other player needs to guess it.
if he guessed a right letter its a hit if it is in the right place its a bool
"""
import random
import string

word = "".join(random.choice(string.ascii_lowercase)for i in range(5))
word = "aabac"
print(word)

turn_count = 0
print("I have a 5 letter word, try to guess what it is.\n"
      "if you guess a right letter you get a hit.\n"
      "if you guess the right letter in its right place you get a bool")
while True:
    while True:
        guess = input("Guess word: ")
        if len(guess) == 5 and \
            guess.lower() and \
            guess.isalpha():
            break
        turn_count += 1
        print("Guess again, your guess must be a 5 letter lower case word.")
    turn_count += 1

    if guess == word:
        print("You won in %d guesses!" % turn_count)
        break

    bool_count = 0
    hit_count = 0
    index = 0

    for letter in guess:
        if letter == word[index]:
            bool_count += 1
        elif letter in word:
            hit_count += 1
        index += 1

    print("bool = %d\nhit = %d" % (bool_count, hit_count))

"""
WORD_LENGTH = 5

def game():
    game_over = False
    turn_count = 0

    word = get_random_word(?)

    display_rules() # print("I have a 5 letter word...")

    while not game_over:
        guess = read_word(?)

        if guess == word:
            print("You won in %d guesses!" % turn_count)
            game_over = True

        bool_count, hit_count = calc_matches(?)
        
        print("bool = %d\nhit = %d" % (bool_count, hit_count))
        
game()
"""