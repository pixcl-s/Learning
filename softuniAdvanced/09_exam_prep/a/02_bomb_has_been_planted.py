# You will be given two, comma and space-separated, integer values, representing the dimensions (N and M) of a map with a rectangular shape. Following this, you will receive the N count lines,
# each containing M count characters describing the map's initial layout.
# The mission of the counter-terrorist is to defuse the bomb successfully. On the way, he might have to face some terrorists. When the bomb is defused the mission is accomplished and the counter-terrorist wins!
# The counter-terrorist must complete his mission in 16 seconds, or the bomb will explode.
# The map will contain randomly positioned elements - a counter-terrorist, terrorists, a bomb, and "empty" spaces:
# · A counter-terrorist will be placed randomly, marked with the letter 'C'
# · There will be some terrorists placed somewhere on the map, marked with the letter 'T'
# · There will be a bomb, marked with the letter 'B'
# · All of the empty positions will be marked with '*'
# Commands are received until:
# · the counter-terrorist defuses the bomb
# · OR is killed by a terrorist
# · OR the bomb explodes
# You will be given commands for the counter-terrorist's movement. The move commands will be "left", "right", "up", and "down". A "defuse" command is also possible.
# The counter-terrorist starts moving only if he has enough time. Be careful, for every move command 1 second passes! If the time is over, the bomb explodes, no matter where the counter-terrorist is positioned, and the program ends.
# · If he steps on a '*' nothing happens and the program should continue running.
# · If he steps on a 'B' the bomb is ready to be defused, only if a proper command ("defuse") is received next. If the next command is different than "defuse", the movement continues.
# · If he steps on a 'T' the counter-terrorist is killed. Both disappear from the map and the position is marked with '*'. The program ends.
# · If he receives a command to step outside of the map, the counter-terrorist remains in position without taking a step. Time keeps tickin' away!
# The "defuse" command:
# · If the counter-terrorist is in a position different from the bomb's position, skip the command. 2 seconds have passed.
# · If the counter-terrorist is placed at the same coordinates as the bomb he starts defusing. The defuse time is 4 seconds:
# o If he successfully defuses it (there are 0 or more remaining seconds after defusing), the position is marked with 'D', and the program ends.
# o Else, counter-terrorist is dead. Both, the bomb and counter-terrorist disappear from the map, and the position is marked with 'X'. Do not forget to see the Output section, and build the correct result.
# In the end, print the final state of the map, with the counter-terrorist in his starting position.
# Input
# · On the first line, you are given two integer values, separated by a comma and space – the dimensions (rows, columns) of a rectangular-shaped matrix.
# · The next rows count lines contain the values (string format) for every matrix row.
# · After that, you will get commands (each one on a new line).
# Output
# At the end of the program:
# · If the bomb has exploded OR the counter-terrorist was defusing and did NOT have enough time, calculate the time needed for successful defuse and print on the console:
# o "Terrorists win!"
# o "Bomb was not defused successfully!"
# o "Time needed: {needed_time_for_bomb_defuse} second/s."
# § Note: The counter-terrorist defuses the bomb only if the bomb's position is the same as the counter-terrorist position and the command "defuse" is given.
# The needed time for bomb defuse will be 0 (zero) if the counter-terrorist is not defusing it. See the Examples section.
# · If the counter-terrorist successfully defused the bomb, track the time left and print on the console:
# o "Counter-terrorist wins!"
# o "Bomb has been defused: {remaining_seconds} second/s remaining."
# · If the counter-terrorist was killed by a terrorist, print on the console:
# o "Terrorists win!"
# · Finally, print the matrix in its final state. Remember to put the counter-terrorist in his initial position.
# Constraints
# · The dimensions of the matrix (map) will be in the range [2…10].
# · Only the letters 'C', 'T', and 'B' will initially be present on the map.
# · There will always be enough commands to finish the program.

timer = 16


def moving(location, going):
    ct_row, ct_col = location
    go_row, go_col = going
    new_row, new_col = ct_row+go_row, ct_col+go_col
    return new_row, new_col


def field_print(fields):
    for o in fields:
        print("".join(o))


def failure(taim):
    print("Terrorists win!")
    print("Bomb was not defused successfully!")
    print(f"Time needed: {abs(taim)} second/s.")
    field_print(field)


row, col = [int(z) for z in input().split(", ")]

field = []

bomb_location = []
t_location = []
ct_location = []

movement = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

for x in range(row):
    huh = list(input())
    for y in range(len(huh)):
        if huh[y] == "*":
            continue
        elif huh[y] == "T":
            t_location.append([x, y])
        elif huh[y] == "C":
            ct_location = [x, y]
        elif huh[y] == "B":
            bomb_location = [x, y]
    field.append(huh)

while timer:
    command = input()
    timer -= 1

    if command == "defuse":
        if ct_location == bomb_location:
            timer -= 3
            if timer >= 0:
                field[ct_location[0]][ct_location[1]] = "D"
                print("Counter-terrorist wins!")
                print(f"Bomb has been defused: {timer} second/s remaining.")
                field_print(field)
                exit()
            elif timer < 0:
                field[ct_location[0]][ct_location[1]] = "X"
                failure(timer)
                exit()
        else:
            timer -= 1
            continue

    ct_current_row, ct_current_col = moving(ct_location, movement[command])

    if ct_current_row < 0 or ct_current_row >= row or ct_current_col < 0 or ct_current_col >= col:
        continue

    ct_location = [ct_current_row, ct_current_col]

    if [ct_current_row, ct_current_col] in t_location:
        field[ct_current_row][ct_current_col] = "*"
        print("Terrorists win!")
        field_print(field)
        exit()

failure(timer)

# 100/100

# 5, 7
# *****T*
# ****T**
# **B****
# ***T**T
# C*****T
# up
# up
# down
# right
# right
# up
# up
# defuse
# down
# defuse
