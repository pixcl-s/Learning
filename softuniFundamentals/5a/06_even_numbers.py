
# Write a program that reads a single string with numbers separated by comma and space ", ".
# Print the indices of all even numbers.

numbers = [int(num) for num in input().split(", ")]

another_list = []

for index in range(len(numbers)):
    if numbers[index] % 2 == 0:
        another_list.append(index)

print(another_list)