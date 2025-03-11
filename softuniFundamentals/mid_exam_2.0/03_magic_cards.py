
deck = input().split(":")

new_deck = []

while True:
    command = input().split()

    if command[0] == "Ready":
        break

    if command[0] == "Add":
        if command[1] in deck:
            new_deck.append(command[1])
        else:
            print("Card not found.")
    elif command[0] == "Insert":
        if command[1] in deck and int(command[2]) <= len(new_deck) - 1:
            new_deck.insert(int(command[2]), command[1])
        else:
            print("Error!")
    elif command[0] == "Remove":
        if command[1] in new_deck:
            new_deck.remove(command[1])
        else:
            print("Card not found.")
    elif command[0] == "Swap":
        index_one = new_deck.index(command[1])
        index_two = new_deck.index(command[2])

        new_deck[index_one], new_deck[index_two] = new_deck[index_two], new_deck[index_one]
    elif command[0] == "Shuffle":
        new_deck.reverse()


print(" ".join(new_deck))
