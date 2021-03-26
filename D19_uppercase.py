def uppercase(fn):
    def wrapper():
        result = fn()
        return result.upper()

    return wrapper


@uppercase  # say_hi = uppercase(say_hi)
def say_hi():
    return 'Hi!'


print(say_hi())
# say_hi = uppercase(say_hi) # decoration
# print(uppercase(say_hi)())
