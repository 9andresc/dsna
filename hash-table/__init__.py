class HashTable(object):
    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def hash(self, key):
        return key % self.size

    def rehash(self, hash_value):
        return (hash_value + 1) % self.size

    def get(self, key):
        hash_value = self.hash(key)
        value = None

        while self.keys[hash_value] != None:
            if self.keys[hash_value] == key:
                value = self.values[hash_value]
                break
            else:
                hash_value = self.rehash(hash_value)
                if self.keys[hash_value] == key:
                    break

        return value

    def put(self, key, value):
        hash_value = self.hash(key)

        if self.keys[hash_value] == None:
            self.keys[hash_value] = key
            self.values[hash_value] = value
        else:
            if self.keys[hash_value] == key:
                self.values[hash_value] = value
            else:
                hash_value = self.rehash(hash_value)
                while self.keys[hash_value] != None and self.keys[hash_value] != key:
                    hash_value = self.rehash(hash_value)

                if self.keys[hash_value] == None:
                    self.keys[hash_value] = key
                    self.values[hash_value] = value
                else:
                    self.values[hash_value] = value
