"""
counting how many times a word is printed in alice.txt for all words
"""


def word_count(file):
    """counts all the times a word appears in a text
    and prints it out i alphabetical order"""
    word_dict = {}
    word_list = []
    with open(file, "r") as read_file:
        for line in read_file.readlines():
            lower = line.lower()
            word_list += lower.split()

    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    for item, number in sorted(word_dict.items()):
        print(item, ":", number)


# word_count("alice.txt")

def print_top(file):
    """prints out the top 20 most appeared words"""
    word_dict = {}
    word_list = []

    with open(file, "r") as read_file:
        for line in read_file.readlines():
            lower = line.lower()
            word_list += lower.split()

    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    number_list = [(v, k) for k, v in word_dict.items()]
    sorted_list = sorted(number_list, reverse=True)
    for i in range(20):
        print(sorted_list[i])

    print(sorted(number_list, reverse=True))


print_top("alice.txt")