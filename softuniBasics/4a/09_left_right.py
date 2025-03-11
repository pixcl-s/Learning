
# Да се напише програма, която чете 2 * n-на брой цели числа,
# подадени от потребителя, и проверява дали сумата на първите n числа (лява сума)
# е равна на сумата на вторите n числа (дясна сума).
# При равенство печата "Yes, sum = " + сумата;
# иначе печата "No, diff = " + разликата.
# Разликата се изчислява като положително число (по абсолютна стойност).

how_many = int(input())

sum_left = 0
sum_right = 0

for i in range(how_many):
    numbers_left = int(input())
    sum_left += numbers_left
for i in range(how_many):
    numbers_right = int(input())
    sum_right += numbers_right

difference = abs(sum_right - sum_left)

if sum_left == sum_right:
    print(f"Yes, sum = {sum_left}")
else:
    print(f"No, diff = {difference}")
