import random


class Player:
    def __init__(self, name, secret_num=None):
        self.possible_opponent_nums = [i for i in range(9999) if self.is_valid_number(i)]
        self.name = name
        if secret_num is None:
            self.secret_num = random.choice(self.possible_opponent_nums)
        else:
            if self.is_valid_number(secret_num):
                self.secret_num = secret_num
            else:
                raise ValueError("Numbers must be 4 digits with no duplicated digits!")
        self.my_guesses = []

    @staticmethod
    def is_valid_number(num):
        digits = []
        while num > 0:
            dig = num % 10
            digits.append(dig)
            num = num // 10
        digits = set(digits)
        return len(digits) == 4

    def make_guess(self, value: int = None):
        if value is None:
            num = random.choice(self.possible_opponent_nums)
        elif not self.is_valid_number(value):
            raise ValueError("Numbers must be 4 digits with no duplicated digits!")
        else:
            num = value
        self.my_guesses.append(num)

    def receive_feedback(self, feedback: tuple):
        new_possible_nums = []
        for num in self.possible_opponent_nums:
            if self.check_b_and_c(num, self.my_guesses[-1]) == feedback:
                new_possible_nums.append(num)
        self.possible_opponent_nums = new_possible_nums
        return

    @classmethod
    def check_b_and_c(cls, num1, num2):
        if not (cls.is_valid_number(num1) and cls.is_valid_number(num2)):
            raise ValueError("Numbers must be 4 digits with no duplicated digits!")
        digits1 = []
        while num1 > 0:
            dig = num1 % 10
            digits1.append(dig)
            num1 = num1 // 10
        digits2 = []
        while num2 > 0:
            dig = num2 % 10
            digits2.append(dig)
            num2 = num2 // 10
        b, c = 0, 0
        for i in range(4):
            if digits1[i] == digits2[i]:
                b += 1
            elif digits1[i] in digits2:
                c += 1
        return b, c
