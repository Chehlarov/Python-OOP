def get_primes(input):
    for el in input:
        if el > 2:
            is_prime = True
            for i in range(2, el):
                if el % i == 0:
                    is_prime = False
                    break
            if is_prime:
                yield el
        elif el == 2:
            yield el


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))