# Create a class called vowels, which should receive a string.
# Implement the __iter__ and __next__ methods, so the iterator returns only the vowels from the string.
from collections import deque


class vowels:
    def __init__(self, letters: str):
        self.letters = letters

        self.vowels = deque([x for x in self.letters if x.lower() in "aeiuyo"])

    def __iter__(self):
        return self

    def __next__(self):
        if not self.vowels:
            raise StopIteration
        return self.vowels.popleft()


# test
my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
# output
# A
# e
# i
# u
# y
# o
