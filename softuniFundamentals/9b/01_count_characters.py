
# Write a program that counts all characters in a string except for space (" ").
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"

a_string = input()
counting = {}

for x in a_string:
    if x == " ":
        continue
    elif x not in counting:
        counting[x] = 0
    counting[x] += 1

for y in counting:
    print(f"{y} -> {counting[y]}")
