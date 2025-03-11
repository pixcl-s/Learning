# Write a program that finds the sum of all elements in an integer array. Use recursion.
# Note: In practice, this recursion should not be used here (instead use an iterative solution),this is just an exercise
# input         output
# 1 2 3 4       10

def summage(digits, result = 0):
    if not digits:
        return result

    result += digits.pop()

    return summage(digits, result)


numbers = [int(x) for x in input().split()]
print(summage(numbers))

# 100/100
