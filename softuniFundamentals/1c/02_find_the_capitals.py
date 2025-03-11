
# Write a program that takes a single string and prints a list of all the capital letters indices.

# Input	    Output
# pYtHoN	[1, 3, 5]
# CApiTAls	[0, 1, 4, 5]

word = list(input())

output = []

for index in range(len(word)):
    if 65 <= ord(word[index]) <= 90:
        output.append(index)

print(output)

