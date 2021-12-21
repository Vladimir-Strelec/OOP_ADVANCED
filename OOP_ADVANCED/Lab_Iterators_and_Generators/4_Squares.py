def squares(n):
    num = 1

    for x in range(1, n + 1):
        yield num ** 2
        num += 1

    # a = (x**2 for x in range(1, n + 1))
    # return a


print(list(squares(5)))