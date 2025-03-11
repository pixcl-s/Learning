# Find the number of all 2x2 squares containing identical chars in a matrix.
# On the first line, you will receive the matrix's dimensions in the format "{rows} {columns}".
# In the following rows, you will receive characters separated by a single space.
# Print the number of all square matrices you have found.
# input             output
# 3 4               2
# A B B D
# E B B B
# I J B B

row, col = [int(x) for x in input().split()]

neo = [input().split() for _ in range(row)]

how_many = 0

for indexation in range(0, row-1):
    for indeksation in range(0, col-1):
        first = neo[indexation][indeksation]
        second = neo[indexation][indeksation+1]
        thrid = neo[indexation+1][indeksation]
        fourth = neo[indexation+1][indeksation+1]
        if first == second and second == thrid and thrid == fourth:
            how_many += 1

print(how_many)

# 100/100
