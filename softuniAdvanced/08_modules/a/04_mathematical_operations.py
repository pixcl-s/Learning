# Create a module that does basic calculations. You will receive 2 numbers and a sign between them all in one string
# Input
# You will receive a single string in the following format
# "{number1} {sign} {number2}"
# o number1 - a float number in the range (0.0, 1000.0)
# o sign - a char that can be
# '/' - divide the first number by the second
# '*' - multiply the 2 numbers
# '-' - subtract the first number from the second
# '+' - add the 2 numbers
# '^' - raise the first number to the second
# o number2 - an integer number in the range (0, 1000)
# Output
# Print only the result of the operation
# The result should be formatted to the second decimal point
# 2.5 * 2

from my_modules import math

stuff = input().split()

math.start(stuff)


