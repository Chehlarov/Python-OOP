class store_results:
    # calls = []

    def __init__(self, fn):
        self.fn = fn
        # store_results.calls.append(fn.__name__)

    def __call__(self, *args, **kwargs):
        res = self.fn(*args, **kwargs)
        with open("results.txt", "a") as f:
            f.write(f"Function {self.fn.__name__} was add called. Result: {res}\n")
        return res


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)