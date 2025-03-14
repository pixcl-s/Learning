
# Да се напише програма, която чете едно цяло число N, въведено от потребителя,
# и генерира всички възможни "специални" числа от 1111 до 9999.
# За да бъде “специално” едно число, то трябва да отговаря на следното условие:
# ⦁	N да се дели на всяка една от неговите цифри без остатък.
# Пример: при N = 16, 2418 е специално число:
# ⦁	16 / 2 = 8 без остатък
# ⦁	16 / 4 = 4 без остатък
# ⦁	16 / 1 = 16 без остатък
# ⦁	16 / 8 = 2 без остатък
# Вход
# Входът се чете от конзолата и се състои от едно цяло число в интервала [1…600000]
# Изход
# На конзолата трябва да се отпечатат всички “специални” числа, разделени с интервал

number = int(input())

for special in range(1111, 10000):

    flag = True

    for index, digit in enumerate(str(special)):
        if int(digit) == 0:
            flag = False
            break
        elif number % int(digit) != 0:
            flag = False

    if flag:
        print(special, end=" ")
