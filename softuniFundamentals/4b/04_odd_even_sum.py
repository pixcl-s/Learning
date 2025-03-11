
# You will receive a single number.
# You should write a function that returns the sum of all even and all odd digits in a given number.
# The result should be returned as a single string in the format:
# "Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
# Print the result of the function on the console.


def odd(digits):
    odd_sum = 0
    for i in digits:
        if i % 2 != 0:
            odd_sum += i
    return odd_sum


def even(digits):
    even_sum = 0
    for i in digits:
        if i % 2 == 0:
            even_sum += i
    return even_sum


numbers = [int(digit) for digit in list(input())]

print(f"Odd sum = {odd(numbers)}, Even sum = {even(numbers)}")
