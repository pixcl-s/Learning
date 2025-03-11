
# Напишете програма, която чете n на брой цели числа.
# Принтирайте най-голямото и най-малкото число сред въведените.

import sys

numbers = int(input())

max_number = -sys.maxsize
min_number = sys.maxsize

for i in range(numbers):
    more_numbers = int(input())
    if max_number < more_numbers:
          max_number = more_numbers
    if min_number > more_numbers:
        min_number = more_numbers

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
