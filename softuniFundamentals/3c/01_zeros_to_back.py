
# Write a program that receives a single string (integers separated by a comma and space ", "),
# finds all the zeros, and moves them to the back without messing up the other elements.
# Print the resulting integer list.

number = input().split(", ")
number = [int(i) for i in number]

counter = 0

while 0 in number:
    number.remove(0)
    counter += 1

for _ in range(counter):
    number.append(0)

print(number)