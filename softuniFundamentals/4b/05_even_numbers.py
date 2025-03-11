
# Write a program that receives a sequence of numbers (integers) separated by a single space
# . It should print a list of only the even numbers. Use filter().

def the_filter(digits):
    return digits % 2 == 0


numbers = [int(digit) for digit in input().split()]

even_numbers = list(filter(the_filter, numbers))

print(even_numbers)
