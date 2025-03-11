
# In the Tribonacci sequence, every number is formed by the sum of the previous 3.
# Write a function that prints numbers from the Tribonacci sequence on one line separated by a single space,
# starting from 1. You will receive a positive integer number as input.


def sequence(digit):
    the_sequence = []
    for x in range(1, digit+1):
        if x == 1 or x == 2:
            the_sequence.append(1)
        elif x == 3:
            the_sequence.append(2)
        else:
            the_sequence.append(the_sequence[len(the_sequence) - 1] + the_sequence[len(the_sequence) - 2]
                                + the_sequence[len(the_sequence) - 3])
    return print(*the_sequence)


number = int(input())

sequence(number)
