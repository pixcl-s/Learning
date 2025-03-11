
# Write a function that receives three integer numbers and returns the smallest.
# Print the result on the console. Use an appropriate name for the function.


def smallest(digit1, digit2, digit3):
    return min(digit1, digit2, digit3)


number_one = int(input())
number_two = int(input())
number_three = int(input())

print(smallest(number_one, number_two, number_three))
