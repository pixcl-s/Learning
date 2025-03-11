# Write a program that reads a matrix from the console and prints:
# · The sum of all numbers in the matrix
# · The matrix itself
# On the first line, you will receive the matrix sizes in the format "{rows}, {columns}".
# On the next rows, you will get elements for each column separated by a comma and a space ", ".
# input                                         output
# 3, 6                                          76
# 7, 1, 3, 3, 2, 1                              [[7, 1, 3, 3, 2, 1], [1, 3, 9, 8, 5, 6], [4, 6, 7, 9, 1, 0]]
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0

row, column = [int(x) for x in input().split(", ")]

matrix = []
sumage = 0

for _ in range(row):
    numbers = [int(x) for x in input().split(", ")]
    sumage += sum(numbers)
    matrix.append(numbers)

print(sumage)
print(matrix)

# 100/100
