class Integer:
    def __init__(self, value: int):
        self.value: int = value

    @classmethod
    def from_float(cls, value: float):
        if type(value) == float:
            return cls(int(value))
        else:
            return "value is not a float"

    @classmethod
    def from_roman(cls, s: str):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return cls(int(int_val))

    @classmethod
    def from_string(cls, value: str):
        try:
            if not isinstance(value, str):
                raise ValueError('Not an instance of string')
            value_int = int(value)
            return cls(value_int)
        except ValueError:
            return "wrong type"

    def add(self, other):
        if not isinstance(other, Integer):
            return "number should be an Integer instance"
        return self.value + other.value


first_num = Integer(10)
second_num = Integer.from_roman("IV")

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
print(first_num.add(second_num))
