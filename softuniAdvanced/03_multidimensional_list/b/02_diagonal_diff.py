# Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).
# On the first line, you will receive an integer N - the size of a square matrix.
# The following N lines hold the values for each column - N numbers separated by a single space.
# Print the absolute difference between the primary and the secondary diagonal sums.
# input             output
# 3                 15
# 11 2 4
# 4 5 6
# 10 8 -12

matrix = [[int(x) for x in input().split()]for _ in range(int(input()))]

sumage_main = 0
sumage_opposite = 0

for x in range(len(matrix)):
    sumage_main += matrix[x][x]
    sumage_opposite += matrix[x][len(matrix)-1-x]

print(abs(sumage_main - sumage_opposite))

# 100/100
