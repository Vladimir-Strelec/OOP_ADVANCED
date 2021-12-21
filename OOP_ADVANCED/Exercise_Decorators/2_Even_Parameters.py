def even_parameters(name_function):
    def wrapper(*args):
        for arg in args:
            try:
                if arg % 2 != 0:
                    return f'Please use only even numbers!'
            except:
                return f'Please use only even numbers!'
        result = name_function(*args)
        return result

    return wrapper


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))