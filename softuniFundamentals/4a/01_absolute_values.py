
# Write a program that receives a sequence of numbers,
# separated by a single space, and prints their absolute value as a list. Use abs().


def abs_numbers(numbers):
    the_numbers = []
    for digit in numbers:
        the_numbers.append(abs(float(digit)))
    return the_numbers


some_input = input().split()

answer = abs_numbers(some_input)

print(answer)
