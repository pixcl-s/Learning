# First, you will be given two sequences of integers representing chocolates and cups of milk.
# You have to start with the last chocolate and try to match it with the first cup of milk.
# If their values are equal, you should make a milkshake and remove both ingredients.
# Otherwise, you should move the cup of milk at the end of the sequence and decrease the value of the chocolate by 5
# without moving it from its position.
# If any of the values are equal to or below 0,
# you should remove them from the records right before mixing them with the other ingredients.
# When you successfully prepare 5 chocolate milkshakes,
# or you have no more chocolate or cups of milk left, you need to stop making chocolate milkshakes.
# Input
# · On the first line of input, you will receive the integers representing the chocolate, separated by ", ".
# · On the second line of input, you will receive the integers representing the cups of milk, separated by ", ".
# Output
# · On the first line, print:
# o If you successfully made 5 milkshakes: "Great! You made all the chocolate milkshakes needed!"
# o Otherwise: "Not enough milkshakes."
# · On the second line - print:
# o If there are chocolates left: "Chocolate: {chocolate1}, {chocolate2}, (…)"
# o Otherwise: "Chocolate: empty"
# · On the third line - print:
# o If there are cups of milk left: "Milk: {milk1}, {milk2}, {milk3}, (…)"
# o Otherwise: "Milk: empty"
# Constraints
# · All given numbers will be valid integers in the range [-100 … 100].
# input                           output
# 20, 24, -5, 17, 22, 60, 26      Great! You made all the chocolate milkshakes needed!
# 26, 60, 22, 17, 24, 10, 55      Chocolate: 20
#                                 Milk: 10, 55


from collections import deque

chocolate = [int(x) for x in input().split(", ")]
cups = deque(int(x) for x in input().split(", "))

milkshakes = 0

while chocolate and cups and milkshakes != 5:
    choco = chocolate[-1]
    cup = cups[0]

    # if choco <= 0 and cup <= 0:
    #     chocolate.pop()
    #     cups.popleft()
    #     continue
    if choco <= 0:
        chocolate.pop()
        continue
    elif cup <= 0:
        cups.popleft()
        continue

    if choco == cup:
        milkshakes += 1
        chocolate.pop()
        cups.popleft()
    elif choco != cup:
        cups.rotate(-1)
        chocolate[-1] -= 5

if milkshakes < 5:
    print("Not enough milkshakes.")
else:
    print("Great! You made all the chocolate milkshakes needed!")

if chocolate:
    print(f"Chocolate: {', '.join(str(x) for x in chocolate)}")
else:
    print("Chocolate: empty")

if cups:
    print(f"Milk: {', '.join(str(x) for x in cups)}")
else:
    print("Milk: empty")

# 100/100