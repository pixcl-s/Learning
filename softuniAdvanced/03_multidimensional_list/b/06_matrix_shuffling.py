# Write a program that reads a matrix from the console and performs certain operations with its elements.
# User input is provided similarly to the problems above - first, you read the dimensions and then the data.
# Your program should receive commands in the format:
# "swap {row1} {col1} {row2} {col2}" where ("row1", "col1") and ("row2", "col2")
# are the coordinates of two points in the matrix.
# A valid command starts with the "swap" keyword along with four valid coordinates (no more, no less),
# separated by a single space.
# · If the command is valid, you should swap the values at the given indexes and
# print the matrix at each step (thus, you will be able to check if the operation was performed correctly).
# · If the command is not valid (does not contain the keyword "swap",
# has fewer or more coordinates entered, or the given coordinates are not valid),
# print "Invalid input!" and move on to the following command. A negative value makes the coordinates not valid.
# Your program should finish when the command "END" is entered.
# input                 output
# 2 3                   5 2 3
# 1 2 3                 4 1 6
# 4 5 6                 Invalid input!
# swap 0 0 1 1          5 4 3
# swap 10 9 8 7         2 1 6
# swap 0 1 1 0
# END

from _collections import deque

row, col = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(row)]

a_flag = False
while True:
    command = deque(input().split())
    to_do = command.popleft()
    if to_do == "END":
        break

    if to_do != "swap" or len(command) != 4:
        print("Invalid input!")
        continue
    command = deque([int(y) for y in command])
    for y in command:
        if y > row or y > col or y < 0:
            print("Invalid input!")
            a_flag = True
            break
    if a_flag:
        a_flag = False
        continue
    location_one = command.popleft()
    location_two = command.popleft()
    location_one_one = command.popleft()
    location_two_two = command.popleft()

    matrix[location_one][location_two], matrix[location_one_one][location_two_two] =\
        matrix[location_one_one][location_two_two], matrix[location_one][location_two]
    for z in matrix:
        print(*z)

# 100/100
