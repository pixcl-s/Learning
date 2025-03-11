# Write an implementation of Selection Sort. You should read an array of integers and sort them.
# Output
# · You should print out the sorted list in the format described below.
# input         output
# 5 4 3 2 1     1 2 3 4 5

def sortage(digits):
    for x in range(len(digits)):
        smallest = x
        for y in range(x, len(digits)):
            if digits[smallest] > digits[y]:
                smallest = y
        if digits[x] > digits[smallest]:
            digits[x], digits[smallest] = digits[smallest], digits[x]
    return ' '.join(str(x) for x in digits)


numbers = [int(x) for x in input().split()]
print(sortage(numbers))

# 100/100
