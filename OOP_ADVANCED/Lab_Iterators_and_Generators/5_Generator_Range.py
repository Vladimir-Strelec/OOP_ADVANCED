def genrange(start, end):
    number_of_list = (x for x in range(start, end+1))
    return number_of_list


print(list(genrange(1, 10)))