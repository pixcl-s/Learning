
# Write a program that reads an integer n.
# Then, for all numbers in the range [1, n],
# print the number and if it is special or not (True / False).
# A number is special when the sum of its digits is 5, 7, or 11.

number = int(input())

for digit in range(1, number + 1):
    split = str(digit)

    if digit <= 10:
        if digit == 5 or digit == 7 or digit == 11:
            print(f"{digit} -> True")
        else:
            print(f"{digit} -> False")
    elif digit > 10:
        if int(split[1:]) + int(split[:1]) == 5 or \
             int(split[1:]) + int(split[:1]) == 7 or\
             int(split[1:]) + int(split[:1]) == 11:
            print(f"{digit} -> True")
        else:
            print(f"{digit} -> False")

