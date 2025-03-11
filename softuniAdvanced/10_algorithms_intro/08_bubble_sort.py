# Write an implementation of Bubble Sort. You should read an array of integers and sort them.
# Output
# · You should print out the sorted list in the format described below.
# input         output
# 5 4 3 2 1     1 2 3 4 5

def sortage(digits):
    for _ in range(len(digits)):
        for x in range(1, len(digits)):
            y = x-1
            if digits[x] < digits[y]:
                stop = True
                digits[x], digits[y] = digits[y], digits[x]
    return ' '.join(str(x) for x in digits)


numbers = [int(x) for x in input().split()]
print(sortage(numbers))

# 100/100

# def sortage(digits):
#     stop = True
#     while stop:
#         stop = False
#         for x in range(1, len(digits)):
#             y = x-1
#             if digits[x] < digits[y]:
#                 stop = True
#                 digits[x], digits[y] = digits[y], digits[x]
#     return ' '.join(str(x) for x in digits)
#
#
# numbers = [int(x) for x in input().split()]
# print(sortage(numbers))

# 100/100

