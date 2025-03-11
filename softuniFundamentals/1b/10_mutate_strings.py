
# You will be given two strings.
# Transform the first string into the second one, letter by letter,
# starting from the first one. After each interaction, print the resulting string only if it is unique.
# Note: the strings will have the same length.

first = list(input())
second = input()

counter = 0
printed = []

for x in second:
    first.pop(counter)
    first.insert(counter, x)
    counter += 1

    if "".join(first) not in printed:
        print("".join(first))
        printed.append("".join(first))
