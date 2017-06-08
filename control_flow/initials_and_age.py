def initials_and_age():
    first_name = input('First name: ')
    last_name = input('Last name: ')
    year_of_birth = input('Year of birth: ')

    year_as_int = int(year_of_birth)

    age = get_age(year_as_int)
    initials = get_initials(first_name, last_name)

    print(get_sentence(initials, age))

def get_age(year):
    return 2017 - year

def get_initials(first_name, last_name):
    return first_name[0].upper() + last_name[0].upper()

def get_sentence(initials, age):
    return "Your initials are %s and you are %d years old" % (initials, age)


initials_and_age()