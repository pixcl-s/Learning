# Write a program that receives a matrix of numbers and
# prints a new one only with the even numbers. Use nested comprehension for that problem.
# On the first line, you will receive the rows of the matrix.
# On the next rows, you will get elements for each column separated with a comma and a space ", ".
# input                     output
# 2                         [[2], [4, 6]]
# 1, 2, 3
# 4, 5, 6

matrix = [[int(x) for x in input().split(", ") if int(x) % 2 == 0]for _ in range(int(input()))]

print(matrix)

# 100/100
