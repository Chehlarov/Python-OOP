def logged(fn):
    def wrapper(*args, **kwargs):
        res = fn(*args, **kwargs)
        output = f"you called {fn.__name__}{args}\n"
        output += f"it returned {res}"
        return output
    return wrapper


@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))

