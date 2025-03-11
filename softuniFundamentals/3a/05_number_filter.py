
# On the first line, you will receive a single number n.
# On the following n lines, you will receive integers.
# After that, you will be given one of the following commands:
# ⦁	even
# ⦁	odd
# ⦁	negative
# ⦁	positive
# Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.

some_list = []
some_list_but_better = []

how_many = int(input())

for _ in range(how_many):
    some_numbers = int(input())
    some_list.append(some_numbers)

command = input()

for index in range(len(some_list)):
    if command == "even" and some_list[index] % 2 == 0:
        some_list_but_better.append(some_list[index])
    elif command == "odd" and some_list[index] % 2 != 0:
        some_list_but_better.append(some_list[index])
    elif command == "negative" and some_list[index] < 0:
        some_list_but_better.append(some_list[index])
    elif command == "positive" and some_list[index] >= 0:
        some_list_but_better.append(some_list[index])

print(some_list_but_better)
