
# Write a function that receives two integer numbers. Calculate the factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal point.

def factorial(digit):
    factor = digit
    for i in range(1, digit):
        factor *= i
    return factor


number = int(input())
divisor = int(input())

print(f"{(factorial(number) / factorial(divisor)):.2f}")
