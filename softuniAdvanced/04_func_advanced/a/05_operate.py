# Write a function called operate that receives an operator ("+", "-", "*" or "/")
# as а first argument and multiple numbers (integers) as additional arguments (*args).
# The function should return the result of the operator applied to all the numbers.
# For more clarification, see the examples below.
# Submit only your function in the Judge system.
# Note: Be careful when you have multiplication and division
# test                              output
# print(operate("+", 1, 2, 3))      6

from functools import reduce


def operate(operator, *args):

    def plus():
        return reduce(lambda x, y: x + y, args)

    def minus():
        return reduce(lambda x, y: x - y, args)

    def addition():
        return reduce(lambda x, y: x * y, args)

    def division():
        return reduce(lambda x, y: x / y, args)


    math = {
        "+": plus,
        "-": minus,
        "*": addition,
        "/": division
    }

    return math[operator]()


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))

# 100/100
