def letter_frequency(string):
    """ 
    make a loop that takes the "string" and for every letter
    finds the number of time it shows in "string".
    return the count of the letter.
    make a dictionary were the the letter is the key and number the value
    """
    frequency = {}

    for letter in string:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1

    return frequency


print(letter_frequency("abzzZA"))
print(letter_frequency("abzzZA"))
