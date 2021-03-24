class countdown_iterator:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        res = self.count
        if res >= 0:
            self.count -= 1
            return res
        else:
            raise StopIteration


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
