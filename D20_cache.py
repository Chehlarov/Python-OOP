def cache(fn):
    log = {}

    def wrapper(arg):
        if arg not in log:
            res = fn(arg)
            log[arg] = res
            return res
        return log[arg]

    wrapper.log = log
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(4)
print(fibonacci.log)
