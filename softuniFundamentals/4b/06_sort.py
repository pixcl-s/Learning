
# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a sorted list of numbers in ascending order. Use sorted().

numbers = [int(digit) for digit in input().split()]

numbers.sort()

print(numbers)
