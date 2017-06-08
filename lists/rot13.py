abc = "abcdefghijklmnopqrstuvwxyz"

def ceser_code(lenguage, n):
    code = {}
    index = 0
    for i in lenguage:
        if index + n < len(lenguage):
            code[i] = lenguage[index + n]
        else:
            code[i] = lenguage[n - (len(lenguage) - index)]
        index += 1

    return code
rot_13 = ceser_code(abc, 13)


def encode(string):
    """
    take a string and replace the letter 
    with the letters value in dictionary rot_13 
    """
    string = string.lower()
    encoded_str = ""
    for i in string:
        if i in rot_13:
            encoded_str += rot_13[i]
        else:
            encoded_str += i
    return encoded_str


print(encode("v nz yrneavat clguba jvgu fur pbqrf npnqrzl!"))

