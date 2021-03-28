def make_bold(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return "<b>" + result + "</b>"

    return wrapper


def make_italic(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return "<i>" + result + "</i>"

    return wrapper


def make_underline(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return "<u>" + result + "</u>"

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))
