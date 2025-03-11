# You will receive a sequence of numbers (integers) separated by a single space.
# Separate the negative numbers from the positive.
# Find the total sum of the negatives and positives, and print the following:
# · On the first line, print the sum of the negatives
# · On the second line, print the sum of the positives
# · On the third line:
# o If the absolute negative number is larger than the positive number: "The negatives are stronger than the positives"
# o If the positive number is larger than the absolute negative number: "The positives are stronger than the negatives"
# Note: you will not receive any zeroes in the input.
# input                         output
# 1 2 -3 -4 65 -98 12 57 -84    -189
#                               137
#                               The negatives are stronger than the positives

# def calculation(digits):
#     return sum(digits)
#
#
# negative_num = []
# positive_num = []
#
# for x in input().split():
#     if "-" in x:
#         negative_num.append(int(x))
#     else:
#         positive_num.append(int(x))
#
# sum_negative = calculation(negative_num)
# sum_positive = calculation(positive_num)
#
# print(sum_negative)
# print(sum_positive)
# print("The negatives are stronger than the positives" if abs(sum_negative)>sum_positive else
#       "The positives are stronger than the negatives")

# 100/100

def calculation(*args):
    # sum_negative = 0
    # sum_positive = 0
    # for x in args:
    #     if x < 0:
    #         sum_negative += x
    #     else:
    #         sum_positive += x
    sum_negative = sum(y for y in args if y < 0)
    sum_positive = sum(y for y in args if y > 0)

    print(f"{sum_negative}\n{sum_positive}")
    return "The negatives are stronger than the positives" if abs(sum_negative)>sum_positive else \
        "The positives are stronger than the negatives"


digits = [int(x) for x in input().split()]

print(calculation(*digits))

# 100/100
