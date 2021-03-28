def even_parameters(fn):
    def wrapper(*args, **kwargs):
        to_calculate = True
        for arg in args:
            if (not isinstance(arg, int)) or arg % 2 != 0:
                to_calculate = False
                break
        # for arg in kwargs.items():
        #     if arg[1] % 2 != 0:
        #         to_calculate = False
        #         break
        if to_calculate:
            res = fn(*args, **kwargs)
            return res
        else:
            return "Please use only even numbers!"

    return wrapper


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, "4", 6, 8))
# print(multiply())
