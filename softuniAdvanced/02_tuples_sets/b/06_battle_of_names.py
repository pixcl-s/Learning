
# You will receive a number N. On the following N lines, you will be receiving names.
# You should sum the ASCII values of each letter in the name and integer divide it by
# the number of the current row (starting from 1).
# Save the result to a set of either odd or even numbers, depending on if the resulting number is odd or even.
# After that, sum the values of each set.
# If the sums of the two sets are equal, print the union of the values, separated by ", ".
# If the sum of the odd numbers is bigger than the sum of the even numbers,
# print the different values, separated by ", ".
# If the sum of the even numbers is bigger than the sum of the odd numbers,
# print the symmetric-different values, separated by ", ".
# NOTE: On every operation, the starting set should be the odd set

odd_set = set()
even_set = set()

for x in range(1, int(input()) + 1):
    name_values = sum([ord(y) for y in input()])
    name_values //= x
    if name_values % 2 == 0:
        even_set.add(name_values)
    else:
        odd_set.add(name_values)

if sum(odd_set) == sum(even_set):
    print(*odd_set | even_set, sep=", ")
elif sum(odd_set) > sum(even_set):
    print(*odd_set - even_set, sep=", ")
elif sum(odd_set) < sum(even_set):
    print(*odd_set ^ even_set, sep=", ")

# 100/100
