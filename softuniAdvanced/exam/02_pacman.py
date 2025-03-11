# You will be given an integer N for the size of the square game field (grid). On the next lines, you will receive the rows of the field.
# The Pacman is marked with the letter 'P' and starts at a random position on the grid. The goal is to guide Pacman in collecting all the stars while avoiding health loss caused by ghosts.
# Star positions are marked with the symbol '*' while the ghost positions are marked with 'G'. Pacman initially starts with 100 units of health.
# When Pacman receives a command, it can move in four directions (up, down, left, and right) or stop and finish the game upon receiving a command "end".
#  When Pacman makes the first move, mark its starting position as empty with a dash '-'.
#  If Pacman reaches an empty position ('-' dash), it waits for the next direction.
#  Pacman collects a star '*' when moving onto a star cell. The star is removed from the grid, and the total count of remaining stars is decreased by 1. The cell must be marked as empty with a dash  '-'.
# Hint: Consider determining the total count of stars placed initially on the grid.
#  Moving onto a ghost position ('G') reduces Pacman's health by 50 units. The cell must be marked as empty with a dash '-'.
# o If Pacman hits two ghosts, his health reaches zero 0, and the game ends.
#  Moving onto a freezer 'F' freezes Pacman temporarily and gives him immunity against the next encountered ghost (the ghost will take no damage but just for once).
# The position must be marked with a dash '-'.
#  A movement outside (leaving the grid's boundaries) positions Pacman to the opposite side.
# Example: Moving out of the top boundary repositions Pacman at the bottom of the same column.
# The program ends instantly in one of the following cases:
#  Pacman collects all the stars placed initially on the field.
#  Pacman's health reaches zero 0.
#  Pacman receives the command "end" which forces it to stop moving and quits the game.
# Input
#  An integer N representing the square grid (field) size.
#  The next N lines hold the values for every row.
#  Following are direction commands or command "end", each on a new line.
# Output
#  If Pacman's health reaches zero 0, print:
# "Game over! Pacman last coordinates [{row},{col}]"
#  If Pacman manages to collect all the stars, print:
# "Pacman wins! All the stars are collected."
#  If Pacman's health is more than zero 0 but it did not collect all the stars due to receiving a command
# "end", print:
# "Pacman failed to collect all the stars."
#  Following print:
# o In all cases:
# "Health: {remaining_health}"
# o If there are still stars to collect, print (otherwise skip it):
# "Uncollected stars: {uncollected_stars_count}"
#  Finally print the final state of the grid (field) with the last known position of Pacman, marked with 'P' on it.
# Constraints
#  The square grid (field) size will be between [3…8] inclusive.
#  Commands will always be valid (up, down, left, right, end).
#  Pacman will always have a valid starting position 'P'.
#  Stars marked by '*' will always be present on the field.
#  Ghosts 'G' will always be at least two.
#  Freezers 'F' can be zero or one.
#  Empty cells marked with a dash '-'.

health = 100

movement = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

pacman_location = []
stars = []
ghosts = []
freezer = []

field = []

for x in range(int(input())):
    row = list(input())
    field.append(row)
    for y in range(len(row)):
        if row[y] == "-":
            continue
        elif row[y] == "P":
            pacman_location = [x, y]
        elif row[y] == "*":
            stars.append([x, y])
        elif row[y] == "G":
            ghosts.append([x, y])
        elif row[y] == "F":
            freezer = [x, y]

stars_to_collect = len(stars)
armor = False

while True:
    commands = input()
    if commands == "end":
        print("Pacman failed to collect all the stars.")
        break

    current_row, current_col = pacman_location[0], pacman_location[1]
    new_row, new_col = pacman_location[0] + movement[commands][0], pacman_location[1] + movement[commands][1]

    if new_row < 0:
        # new_row = field.index(field[new_row])
        new_row = len(field)-1
    elif new_col < 0:
        new_col = len(field)-1
    elif new_row >= len(field):
        new_row = 0
    elif new_col >= len(field):
        new_col = 0

    field[current_row][current_col] = "-"
    field[new_row][new_col] = "P"
    pacman_location = [new_row, new_col]

    if pacman_location in ghosts:
        ghosts.remove(pacman_location)
        if armor:
            armor = False
            continue
        health -= 50
        if not health:
            print(f"Game over! Pacman last coordinates [{new_row},{new_col}]")
            break
    elif pacman_location in stars:
        stars_to_collect -= 1
        stars.remove(pacman_location)
        if not stars_to_collect:
            print("Pacman wins! All the stars are collected.")
            break
    elif pacman_location == freezer:
        armor = True
        freezer = []

    # for q in field:
    #     print("".join(q))

print(f"Health: {health}")
if stars_to_collect:
    print(f"Uncollected stars: {stars_to_collect}")
for q in field:
    print("".join(q))

# 88/100

# 3
# P--
# ***
# G-G
# down
# down
# right
# right
# right
# end
# 5
# P----
# --G*-
# -*--F
# -*G*-
# -----
# up
# right
# down
# down
# left
# end
