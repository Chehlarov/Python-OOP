class HashTable:
    def __init__(self, capacity=4):
        self.array = [None] * capacity
        self.capacity = capacity
        self.length = 0

    def get(self, target_key, default=None):
        idx = self.hash(target_key)
        if self.array[idx] is None:
            return default

        key_values = self.array[idx]
        for key, value in reversed(key_values):
            if key == target_key:
                return value
        return default
        # return self.array[idx]

    def set(self, key, value):
        index = self.hash(key)
        if self.array[index] is None:
            self.array[index] = []
        self.array[index].append((key, value))
        self.length += 1
        if self.length / self.capacity > 0.5:
            self.increase_size()

    def increase_size(self):
        new_table = HashTable(capacity=2 * self.capacity)
        for chain in self.array:
            if chain is None:
                continue
            for key, value in chain:
                new_table.set(key, value)
        self.array = new_table.array
        self.capacity = new_table.capacity

    def hash(self, key) -> int:
        return hash(key) % self.capacity

    def __setitem__(self, key, value):
        self.set(key, value)

    def __getitem__(self, target_key):
        return self.get(target_key)

    def __len__(self):
        return self.capacity


# table = HashTable(5)
# table.set('Jim', 'value_for_Jim')
# table.set('Mike', 'value_for_Mike')
# print(table.get('Jim', 'def'))
# print(table.get('Mike', 'def'))
table = HashTable()

table["name"] = "Peter"
table["age"] = 25

print(table)
print(table.get("name"))
print(table["age"])
print(len(table))
