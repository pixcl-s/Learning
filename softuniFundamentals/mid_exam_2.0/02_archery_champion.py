
archery_field = [int(i) for i in input().split("|")]

points = 0

while True:
    command = input().split("@")

    if command[0] == "Game over":
        break
    if command[0] == "Reverse":
        archery_field.reverse()
        continue

    direction, index, spaces = command
    index = int(index)
    spaces = int(spaces)

    if spaces > len(archery_field):
        spaces %= len(archery_field)

    if direction == "Shoot Left":
        if int(index) > len(archery_field) - 1:
            continue
        elif archery_field[index - spaces] < 5:
            points += archery_field[index - spaces]
            archery_field[index - spaces] -= archery_field[index - spaces]
        else:
            archery_field[index - spaces] -= 5
            points += 5
    elif direction == "Shoot Right":
        if int(index) > len(archery_field) - 1:
            continue
        elif archery_field[index + spaces - len(archery_field)] < 5:
            points += archery_field[index + spaces - len(archery_field)]
            archery_field[index + spaces - len(archery_field)] -= archery_field[index + spaces - len(archery_field)]
        else:
            archery_field[index + spaces - len(archery_field)] -= 5
            points += 5

archery_field = [str(i) for i in archery_field]

print(" - ".join(archery_field))
print(f"John finished the archery tournament with {points} points!")

