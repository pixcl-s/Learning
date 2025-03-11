# Write an implementation of Insertion Sort. You should read an array of integers and sort them.
# Output
# · You should print out the sorted list in the format described below.
# input         output
# 5 4 3 2 1     1 2 3 4 5

def sortage(digits):
    for x in range(1, len(digits)):
        for y in range(x-1, -1, -1):
            if digits[y] > digits[x]:
                digits[x], digits[y] = digits[y], digits[x]
            x -= 1
    return ' '.join(str(x) for x in digits)


numbers = [int(x) for x in input().split()]
print(sortage(numbers))

# 100/100
