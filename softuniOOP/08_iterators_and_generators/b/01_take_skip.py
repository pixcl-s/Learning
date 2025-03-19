# Create a class called take_skip. Upon initialization, it should receive a step (int) and a count (int).
# Implement the __iter__ and __next__ functions. The iterator should return the count numbers (starting from 0) with the given step.
# For more clarification, see the examples:

class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count

        self.digit = 0-step

    def __iter__(self):
        return self

    def __next__(self):
        self.digit += self.step
        if self.digit / self.step == self.count:
            raise StopIteration
        return self.digit


# test
numbers = take_skip(2, 6)
for number in numbers:
    print(number)
# output
# 0
# 2
# 4
# 6
# 8
# 10
# test
numbers = take_skip(10, 5)
for number in numbers:
    print(number)
# output
# 0
# 10
# 20
# 30
# 40
