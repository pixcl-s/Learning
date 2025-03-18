# Create a class called reverse_iter which should receive an iterable upon initialization.
# Implement the __iter__ and __next__ methods, so the iterator returns the items of the iterable in reversed order.

class reverse_iter:
    def __init__(self, digits: list):
        self.digits = digits

        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count -= 1
        if abs(self.count) > len(self.digits):
            raise StopIteration
        return self.digits[self.count]


# test
reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
# output
# 4
# 3
# 2
# 1
