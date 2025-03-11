# Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square
# with a maximum sum of its elements. There will be no case with two or more 3x3 squares with equal maximal sum.
# Input
# · On the first line, you will receive the rows and columns in the format "{rows} {columns}"
# · On the following lines, you will receive each row with its columns
# Output
# · On the first line, print the maximum sum of the elements in the 3x3 square in the format "Sum = {sum}"
# · On the following 3 lines, print each element of the found submatrix, separated by a single space
# input                 output
# 4 5                   Sum = 75
# 1 5 5 2 4             1 4 14
# 2 1 4 14 3            7 11 2
# 3 7 11 2 8            8 12 16
# 4 8 12 16 4

row, col = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(row)]

biggest_numbers = []
sumage = float("-inf")
ind = [

]
for indexation in range(0, row-2):
    for indeksation in range(0, col-2):
        current_sumage = 0
        for r in range(indexation, indexation+3):
            for c in range(indeksation, indeksation+3):
                current_sumage += matrix[r][c]
        if current_sumage > sumage:
            sumage = current_sumage
            ind = [indexation, indeksation]

print(f"Sum = {sumage}")
for r in range(ind[0], ind[0]+3):
    for c in range(ind[1], ind[1]+3):
        print(matrix[r][c], end=" ")
    print()

# 100/100


# calculations = matrix[indexation][indeksation] + matrix[indexation][indeksation+1] + matrix[indexation][indeksation+2] +
#                matrix[indexation+1][indeksation] + matrix[indexation+1][indeksation+1] + matrix[indexation+1][indeksation+2]
#                + matrix[indexation+2][indeksation] + matrix[indexation+2][indeksation+1] + matrix[indexation+2][indeksation+2]
# if sumage < calculations:
#     sumage = calculations
#     biggest_numbers = [[matrix[indexation][indeksation], matrix[indexation][indeksation+1], matrix[indexation][indeksation+2]],
#                        [matrix[indexation+1][indeksation], matrix[indexation+1][indeksation+1], matrix[indexation+1][indeksation+2]],
#                        [matrix[indexation+2][indeksation], matrix[indexation+2][indeksation+1], matrix[indexation+2][indeksation+2]]]

# 100/100
