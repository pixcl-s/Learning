# Create a generator function called squares that should receive a number n.
# It should generate the squares of all numbers from 1 to n (inclusive).

def squares(n):
    for x in range(1, n+1):
        yield x**2


# test
print(list(squares(5)))
# output
# [1, 4, 9, 16, 25]
