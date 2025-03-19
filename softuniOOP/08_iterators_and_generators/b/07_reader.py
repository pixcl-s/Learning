# Create a generator function called read_next() which should receive a different number of arguments (all iterable).
# On each iteration, the function should return each element from each sequence.

def read_next(*stuff):
    # for x in stuff:
    #     yield from x
    for x in stuff:
        for y in x:
            yield y


# test
for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')
# output
# string2dict

print()

# test
for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
# output
# N
# e
# e
# d
# 2
# 3
# words
# .
