# Write a program that reads a matrix from the console and
# finds the 2x2 top-left submatrix with the biggest sum of its values.
# On the first line, you will get matrix sizes in the format "{rows}, {columns}".
# On the next rows, you will get elements for each column, separated with a comma and a space ", ".
# You should print the found submatrix and the sum of its elements, as shown in the examples.
# Hints
# · Be aware of IndexError
# · If you find more than one max square, print the top-left one
# input                         output
# 3, 6                          9 8
# 7, 1, 3, 3, 2, 1              7 9
# 1, 3, 9, 8, 5, 6              33
# 4, 6, 7, 9, 1, 0

row, col = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split(", ")] for _ in range(row)]

biggest_numbers = []
sumage = float("-inf")

for indexation in range(0, row-1):
    for indeksation in range(0, col-1):
        calculations = matrix[indexation][indeksation] + matrix[indexation][indeksation+1] +\
                       matrix[indexation+1][indeksation] + matrix[indexation+1][indeksation+1]
        if sumage < calculations:
            sumage = calculations
            biggest_numbers = [[matrix[indexation][indeksation], matrix[indexation][indeksation+1]],
                       [matrix[indexation+1][indeksation], matrix[indexation+1][indeksation+1]]]

for y in biggest_numbers:
    print(*y)

print(sumage)

# 100/100
