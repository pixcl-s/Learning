# Create a generator function called fibonacci() that generates the Fibonacci numbers infinitely.
# The first two numbers in the sequence are always 0 and 1.
# Each following Fibonacci number is created by the sum of the current number with the previous one.

def fibonacci():
    first, second = 0, 1

    while True:
        combined = first + second
        yield first
        first, second = second, combined


# test
generator = fibonacci()
for i in range(10):
    print(next(generator))
# output
# 0
# 1
# 1
# 2
# 3

print()

# test
generator = fibonacci()
for i in range(1):
    print(next(generator))
# output
# 0