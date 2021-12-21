def read_next(*args):
    for i in args:
        for j in i:
            yield j


for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)

for item in read_next("string", (2,), {"d": 1, "I": 2, "c": 3, "t": 4}):
    print(item, end='')

