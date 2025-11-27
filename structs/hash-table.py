class HashTable:
    def __init__(self, size):
        self.size = 0
        self.table = [None] * size

    def _hash(self, key):
        hash_value = 0
        for index in range(len(key)):
            hash_value += index * ord(key[index])

        return abs(hash_value % len(self.table))

    def get(self, key):
        hash_value = self._hash(key)
        if self.table[hash_value] is None:
            return None

        for index in range(len(self.table[hash_value])):
            key_, value_ = self.table[hash_value][index]
            if key == key_:
                return value_

        return None

    def set(self, key, value):
        hash_value = self._hash(key)

        if self.table[hash_value] is None:
            self.table[hash_value] = []

        for index in range(len(self.table[hash_value])):
            key_ = self.table[hash_value][index][0]
            if key_ == key:
                self.table[hash_value][index] = [key, value]
                return

        self.table[hash_value].append([key, value])
        self.size += 1

    def to_object(self):
        result = {}
        for bucket in self.table:
            if bucket is not None:
                for key, value in bucket:
                    result[key] = value
        return result
