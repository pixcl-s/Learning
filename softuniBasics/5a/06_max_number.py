
# Напишете програма, която до получаване на командата "Stop",
# чете цели числа, въведени от потребителя,
# намира най-голямото измежду тях и го принтира. Въвежда се по едно число на ред.

import sys

number = input().lower()

max_number = -sys.maxsize

while number != "stop":
    if max_number < int(number):
        max_number = int(number)
    number = input().lower()

print(max_number)
