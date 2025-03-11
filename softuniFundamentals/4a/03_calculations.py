
# Create a function that receives three parameters,
# calculates a result depending on the given operator, and returns it.
# Print the result of the function.
# The input comes as three parameters – an operator as a string and two integer numbers.
# The operator can be one of the following:  "multiply", "divide", "add", and "subtract".

def multiply(a, b):
    print(a * b)


def divide(a, b):
    print(a // b)


def add(a, b):
    print(a + b)


def subtract(a, b):
    print(a - b)


operation = input()
number_one = int(input())
number_two = int(input())

if operation == "multiply":
    multiply(number_one, number_two)
elif operation == "divide":
    divide(number_one, number_two)
elif operation == "add":
    add(number_one, number_two)
elif operation == "subtract":
    subtract(number_one, number_two)
