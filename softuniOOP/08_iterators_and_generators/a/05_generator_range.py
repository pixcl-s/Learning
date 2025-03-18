# Create a generator function called genrange that receives a start (int) and an end (int) upon initialization.
# It should generate all the numbers from the start to the end (inclusive).

def genrange(start: int, end: int):
    count = start
    while count <= end:
        yield count
        count += 1


# test
print(list(genrange(1, 10)))
# output
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
