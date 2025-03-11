
# Напишете програма, която чете цяло число n, въведено от потребителя,
# и отпечатва пирамида от числа като в примерите:

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12

number = int(input())

row = 1
digits = 0

while digits < number:
    for _ in range(row):
        digits += 1
        print(digits, end=" ")
        if number <= digits:
            break

    print()
    row += 1
