import re

looking = input()
pattern = r"\d+"
numbers = []

while looking:

    number = re.findall(pattern, looking)
    looking = input()
    numbers.append(number)

numbers = sum(numbers, [])

print(" ".join(numbers))

