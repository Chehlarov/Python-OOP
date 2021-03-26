def even_numbers(fn):
    def wrapper(*args, **kwargs):
        res = fn(*args, **kwargs)
        return list(filter(lambda x: x % 2 == 0,res))

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
