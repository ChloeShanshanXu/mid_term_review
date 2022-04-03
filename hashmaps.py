## https://github.com/EricCharnesky/CIS2001-Winter2022/blob/main/HashMaps/main.py

class HashMap:
    class Item:
        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self == other)

        def __lt__(self, other):
            return self._key < other._key

    _STARTING_CAPACITY = 10
    _LOAD_FACTOR = 0.75

    def __init__(self):
        self._storage = [None] * self._STARTING_CAPACITY
        self._number_of_items = 0

    def _hash_function(self, key):
        return hash(key) % len(self._storage)

    def _is_empty(self):
        return self._number_of_items == 0

    def __len__(self):
        return self._number_of_items

    def __setitem__(self, key, value):
        index = self._hash_function(key)
        if self._storage[index] is None:
            self._storage[index] = []
            self._storage[index].append(self.Item(key, value))
            self._number_of_items += 1
        else:
            for item in self._storage[index]:
                if item._key == key:
                    old_value = item._value
                    item._value = value
                    return key, old_value
            self._storage[index].append(self.Item(key, value))
            self._number_of_items += 1
        if self._number_of_items >= len(self._storage)*self._LOAD_FACTOR:
            self._resize()

    def __getitem__(self, key):
        index = self._hash_function(key)
        if self._storage[index] is None:
            raise KeyError
        for item in self._storage[index]:
            if key == item._key:
               return item._value
        raise KeyError

    def __delitem__(self, key):
        index = self._hash_function(key)
        if self._storage[index] is None:
            raise KeyError
        for item in self._storage[index]:
            if key == item._key:
                value = item._value
                self._storage.remove(item)
                return value

    def _resize(self):
        old_storage = self._storage
        self._storage = [None]*len(self._storage)*2
        for bucket in old_storage:
            if bucket is not None:
                for item in bucket:
                    self[item._key] = item._value  ### used __set_item__  !!

    def __iter__(self):
        for bucket in self._storage:
            if bucket is not None:
                for item in bucket:
                    yield item._key



class Coffee:

    def __init__(self, size, creams = 0, sugars = 0):
        self._size = size
        self._creams = creams
        self._sugars = sugars

    def __str__(self):
        return f'{self._size} coffee with {self._creams} creams and {self._sugars} sugars'

    def __eq__(self, other):
        return self._size == other._size and self._creams == other._creams and self._sugars == other._sugars

    def __hash__(self):
        return hash(self._size)


crappy_dictionary = HashMap()

small_black_coffee = Coffee("small")
large_double_double = Coffee("large", 2, 2)
large_double_double_again = Coffee("large", 2, 2)

crappy_dictionary[small_black_coffee] = 1.99
crappy_dictionary[large_double_double] = 2.99
crappy_dictionary[large_double_double_again] = 3.99

for coffee in crappy_dictionary:
    print(coffee, ":", crappy_dictionary[coffee])

print(crappy_dictionary._storage)