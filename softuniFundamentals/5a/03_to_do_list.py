
# You will be receiving to-do notes until you get the command "End".
# The notes will be in the format: "{importance}-{note}".
# Return a list containing all to-do notes sorted by importance in ascending order.
# The importance value will always be an integer between 1 and 10 (inclusive).

to_do = []

while True:
    command = input()

    if command == "End":
        break

    to_do.append(command)

to_do.sort()
the_list = []

for x in to_do:
    y = list(x)
    y.remove(y[0])
    y.remove(y[0])
    the_list.append("".join(y))

print(the_list)