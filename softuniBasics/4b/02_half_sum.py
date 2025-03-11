
# Да се напише програма, която чете n-на брой цели числа,
# въведени от потребителя,и проверява дали сред тях съществува число,
# което е равно на сумата на всички останали.

# ⦁	Ако има такъв елемент печата "Yes" и на нов ред "Sum = "  + неговата стойност
# ⦁	Ако няма такъв елемент печата "No" и на нов ред "Diff = "
# + разликата между най-големия елемент и сумата на останалите (по абсолютна стойност)

import sys

how_many = int(input())

sum = 0
max_number = -sys.maxsize

for _ in range(how_many):
    numbers = int(input())
    sum += numbers

    if max_number < numbers:
        max_number = numbers

    sum_without_max = sum - max_number
    difference = abs(sum_without_max - max_number)

if sum_without_max == max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    print(f"Diff = {difference}")
