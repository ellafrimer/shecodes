my_file = open("input.txt", "w")
my_file.write("cat\n"
              "dog\n"
              "life\n"
              "mouse\n"
              "banana\n"
              "file\n"
              "python\n"
              "sun\n"
              "moon\n"
              "milk\n")
my_file.close()

revers_file = open("revers.txt", "w")
with open("input.txt", "r") as reading_file:
    for line in reading_file.readlines():
        revers_file.write(line[::-1])
revers_file.close()

new_content = []
with open("revers.txt", "r") as read_revers:
    new_content.append(read_revers.read())

with open("input.txt", "r") as read_input:
    new_content.append(read_input.read())

new_content = "\n".join(new_content)

with open("both.txt", "w") as both:
    both.write(new_content)
