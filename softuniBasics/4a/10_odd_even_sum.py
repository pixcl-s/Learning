
# Да се напише програма, която чете n на брой цели числа,
# подадени от потребителя и проверява дали сумата от числата на четни позиции
# е равна на сумата на числата на нечетни позиции.

# ⦁	Ако сумите са равни да се отпечатат два реда: "Yes" и на нов ред "Sum = " + сумата;
# ⦁	Ако сумите не са равни да се отпечат два реда: "No" и на нов ред "Diff = " + разликата.

# Разликата се изчислява по абсолютна стойност

how_many = int(input())

odd_numbers = 0
even_numbers = 0

for i in range(how_many):
    numbers = int(input())
    if i % 2 == 0:
        even_numbers += numbers
    else:
        odd_numbers += numbers

difference = abs(odd_numbers - even_numbers)

if odd_numbers == even_numbers:
    print("Yes")
    print(f"Sum = {odd_numbers}")
else:
    print("No")
    print(f"Diff = {difference}")
