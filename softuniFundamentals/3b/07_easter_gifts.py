
# Create a program that helps you plan the gifts for your friends and family.
# First, you are going to receive the gifts you plan on buying on a single line,
# separated by space, in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"
# Then you will start receiving commands until you read the "No Money" message.
# There are three possible commands:
# "OutOfStock {gift}"
# Find the gifts with this name in your collection, if any, and change their values to "None".
# "Required {gift} {index}"
# If the index is valid, replace the gift on the given index with the given gift.
# "JustInCase {gift}"
# Replace the value of your last gift with this one.
# In the end, print the gifts on a single line, except the ones with the value "None",
# separated by a single space in the following format:
# "{gift1} {gift2} {gift3} … {giftn}"
# Input / Constraints
# On the 1st line,  you will receive the names of the gifts, separated by a single space.
# On the following lines, until the "No Money" command is received, you will be receiving commands.
# The input will always be valid.
# Output
# Print the gifts in the format described above.

gifts = input().split()

while True:
    commands = input()

    if commands == "No Money":
        break

    list_command = commands.split()

    if list_command[0] == "OutOfStock":
        while list_command[1] in gifts:
            index = gifts.index(list_command[1])
            gifts[index] = "None"
    elif list_command[0] == "Required":
        index = int(list_command[2])
        if index >= len(gifts):
            continue
        else:
            gifts[index] = list_command[1]
    elif list_command[0] == "JustInCase":
        gifts[-1] = list_command[1]

while "None" in gifts:
    gifts.remove("None")

print(" ".join(gifts))
