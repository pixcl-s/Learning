
# You will receive three integer numbers.
# Write functions named:
# sum_numbers() that returns the sum of the first two integers
# subtract() that returns the difference between the returned result of the first function and the third integer
# Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters.
# Print the result of the subtract() function on the console.

def sum_numbers(digit1, digit2):
    return digit1 + digit2


def subtract(digit1, digit2):
    return digit1 - digit2


def add_and_subtract(digit_one, digit_two, digit_three):
    the_sum = sum_numbers(digit_one, digit_two)
    final = subtract(the_sum, digit_three)
    print(final)


number_one = int(input())
number_two = int(input())
number_three = int(input())

add_and_subtract(number_one, number_two, number_three)
