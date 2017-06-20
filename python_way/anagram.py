"""an anagram is a word that has the same letters
as another word only scrambled """


def is_anagram(x, y):

    if len(x) != len(y):
        return False
    y_list = list(y)
    for l in x:
        if l in y_list:
            del(y_list[y_list.index(l)])
        else:
            return False
    return True


def is_anagram_2(x, y):
    if len(x) != len(y):
        return False

    return sorted(x) == sorted(y)





