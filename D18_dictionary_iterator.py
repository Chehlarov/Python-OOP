class dictionary_iter:
    def __init__(self, dict):
        self.dict = dict
        self.keys = tuple(self.dict.keys())
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.i < len(self.keys):
            result = (self.keys[self.i], self.dict[self.keys[self.i]])
            self.i += 1
            return result
        else:
            raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
