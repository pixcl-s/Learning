
# A palindrome is a number that reads the same backward as forward, such as 323 or 1001.
# Write a function that receives a list of positive integers, separated by comma and space ", ".
# The function should check if each integer is a palindrome - True or False. Print the result.

def is_palindrome(digits):
    for digit in digits:
        reversed_digit = (str(digit)[::-1])
        if digit == int(reversed_digit):
            print("True")
        else:
            print("False")


numbers = [int(digit) for digit in input().split(", ")]

is_palindrome(numbers)
