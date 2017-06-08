print("Accessing just the elements")
for letter in ['a', 'b', 'c']:
    print(letter)

print("Accessing the elements and their position in the collection")
for (index, letter) in enumerate(['a', 'b', 'c']):
    print("[%d] %s" % (index, letter))

print("A string is also a collection...")
for (index, letter) in enumerate("banana"):
    print("iteration no. %d" % (index+1))
    print("[%d] %s" % (index, letter))

dict = {
    'first_key': 'first value'
}

dict['hi'] = 'hello'
dict['anyword'] = 23

print(dict)

"""
ABCDEFG
CDEFGHI

BAD -> DCF
"""