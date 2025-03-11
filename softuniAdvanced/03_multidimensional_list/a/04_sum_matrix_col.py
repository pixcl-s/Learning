# Write a program that reads a matrix from the console and prints the sum for each column on separate lines.
# On the first line, you will get matrix sizes in the format "{rows}, {columns}".
# On the next rows, you will get elements for each column separated with a single space.
# input                     output
# 3, 6                      12
# 7 1 3 3 2 1               10
# 1 3 9 8 5 6               19
# 4 6 7 9 1 0               ...

row, column = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(row):
    matrix.append([int(x) for x in input().split()])

for index in range(column):
    sumage = 0
    for lul in range(row):
        sumage += matrix[lul][index]
    print(sumage)

# 100/100
