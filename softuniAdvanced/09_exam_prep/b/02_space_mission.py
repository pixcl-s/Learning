# You will be given an integer N representing the size of the space field, which is a square grid (each position on the grid represents a sector of space).
# On the next N lines, you will receive the rows of the space grid with symbols, separated by a single space (" ").
# · Your spaceship starts at a random position, marked by 'S'.
# · Meteorites are scattered across space, marked by 'M'.
# o Each time you pass through a meteorite sector, your resources are decreased by 5 units.
# · Planet B, your destination, is marked by 'P'.
# · There are space stations, marked by 'R' (for "Resources").
# o Where you can refuel and gain 10 units of resources (up to a maximum of 100 units).
# · All other sectors are empty and marked by '.'.
# Mission Rules:
# · Your mission is to reach Planet B ('P') with the resources you have and gain during the journey.
# · Your spaceship starts with 100 units of resources initially at a position, marked by 'S'.
# o When the spaceship makes the first move, its starting position is marked by '.'.
# · You will be given commands to move the spaceship.
# o The valid commands are: "up", "down", "left", and "right".
# · Each move decreases your resources by 5 units.
# o If the spaceship moves to a sector with a space station ('R'), you gain 10 units of resources, and the station remains in place.
# § You can refuel at the same station each time you encounter it. But your resources cannot go above 100 units. If they do, set them to 100.
# o If the spaceship moves into a sector with a meteorite ('M'), an additional 5 units are subtracted from your resources, and the meteorite is destroyed by the collision (replaced by '.').
# o If your resources drop below 5 units before reaching Planet B or a space station to refuel, the mission fails, and the spaceship is stranded in space.
# § Remember the last known position of the spaceship.
# o If the spaceship moves out of the grid's boundaries, it is considered lost in space and the mission ends immediately with a failure.
# § Remember the last known position of the spaceship before moving out of boundaries.
# Input
# · On the first line, you will receive an integer N (the size of the square grid).
# · The next N lines will represent the grid, with each sector marked as 'S', 'M', 'P', 'R', or '.'.
# o Letters 'S' and 'P' appear only once. o Symbols are separated by a single space (" "). See the Examples section.
# · After the grid, a series of valid movement commands will follow, each on a new line.
# Output
# · On the first line:
# o If the spaceship reaches Planet B with zero or more resources, print:
# § "Mission accomplished! The spaceship reached Planet B with {resources} resources left."
# o If the spaceship runs out of resources before reaching Planet B or a space station, print:
# § "Mission failed! The spaceship was stranded in space."
# o If the spaceship exits the grid's boundaries and gets lost in space, print:
# § "Mission failed! The spaceship was lost in space."
# · On the next lines:
# o Print the final state of the grid, with the spaceship's last known position marked by 'S'.
# § If the spaceship successfully landed on Planet B, it is not displayed on the grid. § Symbols should be separated by a single space (" "). See the Examples section.
# Constraints
# · The size of the square matrix (grid) will be between [2 -10] inclusive.
# · Each sector will be marked as 'S', 'M', 'P', 'R', or '.'.
# o Letters 'S'and 'P'appear only once.
# · There will always be enough commands to either succeed or fail the mission.
# · The spaceship starts with 100 units of resources initially.

def moving(location, going):
    ct_row, ct_col = location
    go_row, go_col = going
    new_row, new_col = ct_row+go_row, ct_col+go_col
    return new_row, new_col


def field_print(speis):
    for o in speis:
        print(" ".join(o))


resources = 100

space = []

spaceship_location = []
meteorite_location = []
planet_destination = []
stations = []

movement = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

stuff = {
    "S": lambda x, y: spaceship_location.append([x, y]),
    "M": lambda x, y: meteorite_location.append([x, y]),
    "P": lambda x, y: planet_destination.append([x, y]),
    "R": lambda x, y: stations.append([x, y])
}

for x in range(int(input())):
    rows = input().split()
    space.append(rows)
    for y in range(len(rows)):
        if rows[y] == ".":
            continue
        stuff[rows[y]](x, y)

spaceship_location = spaceship_location[0]
planet_destination = planet_destination[0]

mission_accomplished = False

while resources:
    move = input()
    resources -= 5

    current_row, current_col = moving(spaceship_location, movement[move])

    if current_row < 0 or current_row >= len(space) or current_col < 0 or current_col >= len(space):
        print("Mission failed! The spaceship was lost in space.")
        field_print(space)
        exit()

    if spaceship_location in stations:
        space[spaceship_location[0]][spaceship_location[1]] = "R"
    else:
        space[spaceship_location[0]][spaceship_location[1]] = "."
    space[current_row][current_col] = "S"
    spaceship_location = [current_row, current_col]

    if spaceship_location in meteorite_location:
        meteorite_location.remove(spaceship_location)
        resources -= 5
    elif spaceship_location in stations:
        resources += 10
    elif spaceship_location == planet_destination:
        space[spaceship_location[0]][spaceship_location[1]] = "P"
        mission_accomplished = True
        break

    if resources > 100:
        resources = 100

print(f"Mission accomplished! The spaceship reached Planet B with {resources} resources left." if mission_accomplished
      else "Mission failed! The spaceship was stranded in space.")
field_print(space)

# 100/100

# 3
# S . .
# . M .
# . R P
# right
# down
# down
# right
