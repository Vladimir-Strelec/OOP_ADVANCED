from itertools import permutations


def possible_permutations(line_nums):

    for i in permutations(line_nums):
        yield list(i)


[print(n) for n in possible_permutations([1, 2, 3])]
