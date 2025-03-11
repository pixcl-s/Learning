
# Write a program, which will take a list of names and print only the unique names in the list.
# The order in which we print the result does not matter.

names = set()

for _ in range(int(input())):
    name = input()
    names.add(name)

for x in names:
    print(x)

# 100/100
