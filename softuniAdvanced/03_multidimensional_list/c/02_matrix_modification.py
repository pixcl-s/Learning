# Write a program that reads a matrix from the console and changes its values.
# On the first line, you will get the matrix's rows - N.
# You will get elements for each column on the following N lines, separated with a single space.
# You will be receiving commands in the following format:
# · "Add {row} {col} {value}" – Increase the number at the given coordinates with the value.
# · "Subtract {row} {col} {value}" – Decrease the number at the given coordinates by the value.
# If the coordinate is invalid, you should print "Invalid coordinates".
# A coordinate is valid if both of the given indexes are in the range [0; len() – 1].
# When you receive "END", you should print the matrix and stop the program.
# input                 output
# 3                     6 2 3
# 1 2 3                 4 3 6
# 4 5 6                 7 8 9
# 7 8 9
# Add 0 0 5
# Subtract 1 1 2
# END

matrix = [[int(x) for x in input().split()]for _ in range(int(input()))]

mathing = {
    "Add": lambda o, u: o + u,
    "Subtract": lambda o, u: o - u
}

while True:
    commands = input()
    if commands == "END":
        break

    math, row, col, amount = commands.split()
    row,col,amount = int(row),int(col),int(amount)

    if row < 0 or row > len(matrix)-1 or col < 0 or col > len(matrix[0])-1:
        print("Invalid coordinates")
        continue

    matrix[row][col] = mathing[math](matrix[row][col], amount)

for x in matrix:
    print(*x)

# 100/100
