
# Фирма дава следните комисионни на търговците си според града,
# в който работят и обема на продажбите:
# Град | 0 ≤ s ≤ 500 | 500 < s ≤ 1 000 | 1 000 < s ≤ 10 000 | s > 10 000
# Sofia      5%              7%                  8%               12%
# Varna     4.5%            7.5%                 10%              13%
# Plovdiv   5.5%             8%                  12%             14.5%
# Напишете конзолна програма, която чете име на град (текст
# ) и обем на продажби (реално число), въведени от потребителя,
# и изчислява и извежда размера на търговската комисионна според горната таблица.
# Резултатът да се изведе форматиран до 2 цифри след десетичната точка.
# При невалиден град или обем на продажбите (отрицателно число) да се отпечата "error".

city = input().lower()
sales = float(input())

if 0 <= sales <= 500:
    if city == "sofia":
        print(f"{sales * 0.05:.2f}")
    elif city == "varna":
        print(f"{sales * 0.045:.2f}")
    elif city == "plovdiv":
        print(f"{sales * 0.055:.2f}")
    else:
        print("error")
elif 500 <= sales <= 1000:
    if city == "sofia":
        print(f"{sales * 0.07:.2f}")
    elif city == "varna":
        print(f"{sales * 0.075:.2f}")
    elif city == "plovdiv":
        print(f"{sales * 0.08:.2f}")
    else:
        print("error")
elif 1000 <= sales <= 10000:
    if city == "sofia":
        print(f"{sales * 0.08:.2f}")
    elif city == "varna":
        print(f"{sales * 0.10:.2f}")
    elif city == "plovdiv":
        print(f"{sales * 0.12:.2f}")
    else:
        print("error")
elif sales > 10000:
    if city == "sofia":
        print(f"{sales * 0.12:.2f}")
    elif city == "varna":
        print(f"{sales * 0.13:.2f}")
    elif city == "plovdiv":
        print(f"{sales * 0.145:.2f}")
    else:
        print("error")
else:
    print("error")
