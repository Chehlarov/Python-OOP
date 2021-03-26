VOWELS = {'A', 'E', 'I', 'O', 'U'}


def vowel_filter(fn):
    def wrapper(*args, **kwargs):
        results = fn(*args, **kwargs)
        return [c for c in results if c.upper() in VOWELS]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
