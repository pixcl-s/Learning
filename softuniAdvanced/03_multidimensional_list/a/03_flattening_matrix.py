# Write a program that receives a matrix and prints its flattened version (a list with all the values).
# For example, the flattened list of the matrix: [[1, 2], [3, 4]] will be [1, 2, 3, 4].
# On the first line, you will receive the number of a matrix's rows.
# On the next rows, you will get the elements for each column separated with a comma and a space ", ".
# # input                 output
# 2                       [1, 2, 3, 4, 5, 6]
# 1, 2, 3
# 4, 5, 6

neo = []

for _ in range(int(input())):
    neo.append([int(x) for x in input().split(", ")])

flat_neo = [num for outer in neo for num in outer]

print(flat_neo)

# 100/100
