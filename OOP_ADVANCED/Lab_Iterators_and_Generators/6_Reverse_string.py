def reverse_text(string):
    # result = (x for x in string[::-1])
    # return result
    for x in string[::-1]:
        yield x


for char in reverse_text("step"):
    print(char, end='')