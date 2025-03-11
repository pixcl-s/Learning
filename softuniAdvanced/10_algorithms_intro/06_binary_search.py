# Implement an algorithm that finds the index of an element in a sorted array of integers in logarithmic time.
# input         output
# 1 2 3 4 5     0
# 1

def locator(digits, look):
    right_index = len(digits)
    copy_of_digits = digits.copy()
    while True:
        left_index = 0
        middle_index = len(copy_of_digits) // 2
        if copy_of_digits[middle_index] == look:
            return digits.index(copy_of_digits[middle_index])
        elif copy_of_digits[middle_index] < look:
            left_index = middle_index
        elif copy_of_digits[middle_index] > look:
            right_index = middle_index
        copy_of_digits = copy_of_digits[left_index:right_index]
        if len(copy_of_digits) == 1:
            return  -1


numbers = [int(x) for x in input().split()]
looking_for = int(input())
print(locator(numbers, looking_for))

# 100/100
