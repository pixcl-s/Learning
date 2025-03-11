# On the first line, you will be given a number representing the size of the field.
# In the following few lines, you will be given a field with:
# · One bunny - randomly placed in it and marked with the symbol "B"
# · Number of eggs placed at different positions of the field and traps marked with "X"
# Your job is to determine the direction in which the bunny should go to collect the maximum number of eggs.
# The directions that should be considered as possible are up, down, left, and right.
# If you reach a trap while checking some of the directions,
# you should not consider the fields after the trap in this direction.
# The bunny can move within the field and cannot go outside its boundaries.
# Do not consider negative indices as valid ones. For more clarifications, see the examples below.
# Note: In some directions, the collected eggs can happen to be zero or a negative number.
# Input
# · A number representing the size of the field
# · The matrix representing the field (each position separated by a single space)
# Output
# · The direction which should be considered as best (lowercase)
# · The field positions from which we are collecting eggs as lists
# · The total number of eggs collected
# Constraints
# · There will NOT be two or more paths consisting of the same total amount of eggs.
# input                 output
# 5                     right
# 1 3 7 9 11            [3, 1]
# X 5 4 X 63            [3, 2]
# 7 3 21 95 1           [3, 3]
# B 1 73 4 9            [3, 4]
# 9 2 33 2 0            87


def check(one, two, three):
    if one < 0 or one >= three or two < 0 or two >= three:
        return True


bunny_movement = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

field_dimensions = int(input())

field = []

bunny_location = []

points = float("-inf")
direction = []

for _ in range(field_dimensions):
    stuff = [int(x) if x.isnumeric() else x for x in input().split()]
    field.append(stuff)
    if "B" in stuff:
        bunny_location = [len(field)-1, stuff.index("B")]

bunny_row, bunny_col = bunny_location

for x in bunny_movement.values():
    move_row, move_col = x
    moving_row = bunny_row
    moving_col = bunny_col
    current_points = 0
    while True:
        moving_row += move_row
        moving_col += move_col

        if check(moving_row, moving_col, field_dimensions):
            break

        if field[moving_row][moving_col] != "X":
            current_points += field[moving_row][moving_col]

    if current_points > points:
        points = current_points
        direction = x

print(*[key for key, value in bunny_movement.items() if value == direction])
to_print_one = bunny_row
to_print_two = bunny_col
for _ in range(field_dimensions):
    to_print_one += direction[0]
    to_print_two += direction[1]
    if check(to_print_one, to_print_two, field_dimensions):
        break
    print([to_print_one, to_print_two])
print(points)

# 37/100
