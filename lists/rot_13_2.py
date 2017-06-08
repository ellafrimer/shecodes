def encoder(abc, offset, text):
    text = text.lower()
    encoded_text = ""
    for i in text:
        if i in abc:
            index = abc.find(i)
            encoded_text += abc[index + offset]
        else:
            encoded_text += i
    return  encoded_text

abc = "abcdefghijklmnopqrstuvwxyz"
example = "v nz yrneavat clguba jvgu fur pbqrf npnqrzl!"
example_2 = "hello my name is iniego montoga"
print(encoder(abc, 13, example_2))
