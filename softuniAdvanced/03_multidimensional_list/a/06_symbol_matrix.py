# Write a program that reads a number - N, representing the rows and columns of a square matrix.
# On the next N lines, you will receive rows of the matrix. Each row consists of ASCII characters.
# After that, you will receive a symbol.
# Find the first occurrence of that symbol in the matrix and print its position in the format: "({row}, {col})".
# It would help if you started searching from the top left.
# If there is no such symbol, print the message "{symbol} does not occur in the matrix".
# input                     output
# 3                         (2, 1)
# ABC
# DEF
# X!@
# !

how_many = int(input())

matrix = [list(x) for _ in range(how_many) for x in input().split()]

looking_for = input()

for x in range(how_many):
    for y in range(how_many):
        if matrix[x][y] == looking_for:
            print((x, y))
            exit()

print(f"{looking_for} does not occur in the matrix")

# 100/100
