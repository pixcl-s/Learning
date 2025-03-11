
# Write a program that reads a text from the console and counts the occurrences of each character in it.
# Print the results in alphabetical (lexicographical) order.

text = input()
counting = {}

for x in text:
    if x not in counting:
        counting[x] = 0
    counting[x] += 1

for letter, digit in sorted(counting.items()):
    print(f"{letter}: {digit} time/s")

# 100/100
