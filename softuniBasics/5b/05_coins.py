
# Производителите на вендинг машини искали да направят машините
# си да връщат възможно най-малко монети ресто. Напишете програма,
# която приема сума - рестото, което трябва да се върне и изчислява
# с колко най-малко монети може да стане това.

change = float(input())

coin = 0

while change > 0:
    change = round(change, 2)
    if change >= 2:
        coin += 1
        change -= 2
    elif change >= 1:
        coin += 1
        change -= 1
    elif change >= 0.50:
        coin += 1
        change -= 0.50
    elif change >= 0.20:
        coin += 1
        change -= 0.20
    elif change >= 0.10:
        coin += 1
        change -= 0.10
    elif change >= 0.05:
        coin += 1
        change -= 0.05
    elif change >= 0.02:
        coin += 1
        change -= 0.02
    else:
        coin += 1
        change -= 0.01

print(coin)
