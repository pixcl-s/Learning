
# You will receive three integer numbers.
# Write a program that finds if their multiplication (the result) is negative, positive, or zero.
# Try to do this WITHOUT multiplying the 3 numbers.

def positive():
    print("positive")


def negative():
    print("negative")


def zero():
    print("zero")


def checking(first_digit, second_digit, third_digit):

    if first_digit == 0 or second_digit == 0 or third_digit == 0:
        zero()
    elif first_digit < 0 or second_digit < 0 or third_digit < 0:
        if first_digit < 0 and second_digit < 0 and third_digit < 0:
            negative()
            exit()
        elif (first_digit < 0 and second_digit < 0) or (second_digit < 0 and third_digit < 0) or (first_digit < 0 and third_digit < 0):
            positive()
            exit()
        negative()
    else:
        positive()


first_number = int(input())
second_number = int(input())
third_number = int(input())

checking(first_number, second_number, third_number)
