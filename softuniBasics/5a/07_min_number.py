
# Напишете програма, която до получаване на командата "Stop",
# чете цели числа, въведени от потребителя, намира най-малкото измежду тях и
# го принтира. Въвежда се по едно число на ред.

import sys

number = input().lower()

min_number = sys.maxsize

while True:

    if number == "stop":
        break
    elif min_number > int(number):
        min_number = int(number)

    number = input().lower()
print(min_number)
