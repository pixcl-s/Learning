
# Write a program that receives a list of integer numbers
# (separated by a single space) and a number n.
# The number n represents the count of numbers to remove from the list.
# You should remove the smallest ones, and then,
# you should print all the numbers that are left in the list,
# separated by a comma and a space ", ".

from sys import maxsize

numbers = input().split()
numbers = [int(i) for i in numbers]

how_many_die = int(input())

for _ in range(how_many_die):
    smallest_number = maxsize
    for x in numbers:
        if x < smallest_number:
            smallest_number = x

    numbers.remove(smallest_number)

print(*numbers, sep= ", ")
