# Create a class called dictionary_iter. Upon initialization, it should receive a dictionary object.
# Implement the iterator to return each key-value pair of the dictionary as a tuple of two elements (the key and the value).

from typing import Dict


class dictionary_iter:
    def __init__(self, stuff: Dict):
        self.list_of_the_stuff = list(stuff.items())

        self.index_for_the_stuff = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index_for_the_stuff += 1
        if self.index_for_the_stuff == len(self.list_of_the_stuff):
            raise StopIteration
        return self.list_of_the_stuff[self.index_for_the_stuff]


# test
result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
# output
# (1, '1')
# (2, '2')
print()
# test
result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
# output
# ("name", "Peter")
# ("age", 24)
