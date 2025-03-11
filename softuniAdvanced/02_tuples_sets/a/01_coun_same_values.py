
# You will be given numbers separated by a space.
# Write a program that prints the number of occurrences of each number in the format
# "{number} - {count} times".
# The number must be formatted to the first decimal point.

numbers = tuple(float(x) for x in input().split())

counting = {}

for x in numbers:
    if x not in counting:
        counting[x] = 0
    counting[x] += 1

for num, times in counting.items():
    print(f"{num} - {times} times")

# 100/100
