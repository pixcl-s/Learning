
# Write a program that receives a single string containing positive and negative numbers separated by a single space.
# Print a list containing the opposite of each number.


random_string = input()

issa_list = random_string.split()
reversed_list = []

for character in issa_list:
    x = int(character) * -1
    reversed_list.append(x)

print(reversed_list)

