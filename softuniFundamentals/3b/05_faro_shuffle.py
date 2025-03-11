
# A faro shuffle is a method for shuffling a deck of cards,
# in which the deck is split exactly in half.
# Then the cards in the two halves are perfectly interleaved,
# such that the original bottom card is still on the bottom and
# the original top card is still on top.
# For example, faro shuffling the list
# ['ace', 'two', 'three', 'four', 'five', 'six']
# once, gives
# ['ace', 'four', 'two', 'five', 'three', 'six']
# Write a program that receives a single string (cards separated by space)
# and on the second line receives a count of faro shuffles that should be made.
# Print the state of the deck after the shuffle.
# Note: The length of the deck of cards will always be an even number.

deck = input().split(" ")
shuffles = int(input())

for i in range(shuffles):
    first_half = []
    second_half = []
    shuffled_deck = []
    for x in range(len(deck)):
        if x // (len(deck) / 2) == 0:
            first_half.append(deck[x])
        else:
            second_half.append(deck[x])
    for y in range(len(first_half)):
        shuffled_deck.append(first_half[y])
        shuffled_deck.append(second_half[y])

    deck = shuffled_deck

print(deck)
