# Write a program to flatten several lists of numbers received in the following format:
# String with numbers or empty strings separated by "|"
# Values are separated by spaces (" ", one or several)
# Order the output list from the last to the first matrix sub-lists and their values from left to right as shown below
# input                      output
# 1 2 3 |4 5 6 | 7  88       7 88 4 5 6 1 2 3

numbers = input().split("|")
matrix = []

for x in numbers:
    matrix.append(x.split())

print(" ".join(str(x) for y in matrix[::-1] for x in y))

# 100/100
