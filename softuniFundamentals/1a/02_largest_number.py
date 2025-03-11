
# Write a program that receives three whole numbers and prints the largest one.

first_number = int(input())
second_number = int(input())
third_number = int(input())

if first_number > third_number and first_number > second_number:
    print(first_number)
elif second_number > third_number and second_number > first_number:
    print(second_number)
elif third_number > first_number and third_number > second_number:
    print(third_number)
