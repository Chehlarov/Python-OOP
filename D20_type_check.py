def type_check(typ):
    def decorator(fn):
        def wrapper(*args):
            is_correct_type = True
            for arg in args:
                if not isinstance(arg, typ):
                    is_correct_type = False
                    break
            if is_correct_type:
                return fn(*args)
            return "Bad Type"
        return wrapper
    return decorator


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))

