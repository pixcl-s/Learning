
# Write a program that prints all elements from a given sequence
# of words that occur an odd number of times (case-insensitive) in it.
# ⦁	Words are given on a single line, space-separated.
# ⦁	Print the result elements in lowercase, in their order of appearance

elements = (z.lower() for z in input().split())

element = {}

for x in elements:
    if x not in element:
        element[x] = 0

    element[x] += 1

for y in element:
    if element[y] % 2 != 0:
        print(y, end=" ")

