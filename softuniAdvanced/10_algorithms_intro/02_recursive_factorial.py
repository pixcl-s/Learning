# Write a program that calculates the recursively factorial of a given number.
# NOTE: In practice, this recursion should not be used here (instead use an iterative solution).
# input         output
# 5             120

def factorial(digit, result = 1):
    result *= digit
    if digit == 1:
        return result

    return factorial(digit-1, result)


number = int(input())
print(factorial(number))

# 100/100
