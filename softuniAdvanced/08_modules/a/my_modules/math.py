# '/' - divide the first number by the second
# '*' - multiply the 2 numbers
# '-' - subtract the first number from the second
# '+' - add the 2 numbers
# '^' - raise the first number to the second

def multiply(num, num2):
    return num * num2


def divide(num, num2):
    return num / num2


def addition(num, num2):
    return num + num2


def subtraction(num, num2):
    return num - num2


def exponentiation(num, num2):
    return num ** num2


calling = {
    "*": multiply,
    "/": divide,
    "+": addition,
    "-": subtraction,
    "^": exponentiation
}


def start(huh):
    first_number = float(huh[0])
    operation = huh[1]
    second_number = int(huh[2])
    hm = calling[operation](first_number, second_number)
    print(f"{hm:.2f}")
