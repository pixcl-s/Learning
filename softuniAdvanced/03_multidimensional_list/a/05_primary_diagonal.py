# Write a program that finds the sum of all numbers in a matrix's primary diagonal (runs from top left to bottom right).
# On the first line, you will receive an integer N – the size of a square matrix.
# The next N lines hold the values for each column - N numbers, separated by a single space.
# input                 output
# 3                     4
# 11 2 4
# 4 5 6
# 10 8 -12

matrix = [[int(x) for x in input().split()]for _ in range(int(input()))]
sumage = 0

for x in range(len(matrix)):
    sumage += matrix[x][x]

print(sumage)

# 100/100
