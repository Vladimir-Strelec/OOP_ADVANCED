def multiply(n):
    def decorator(ref_func):
        def wrapper(num):
            result = ref_func(num) * n
            return result
        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))