#
# Напишете програма, която изчислява колко ще струва на група хора да си поръчат храна за вкъщи.
# Групата ще си поръча и десерт, чиято цена е равна на 20% от общата сметка (без доставката).
# Цената на доставка е 2.50 лв и се начислява най-накрая.
#
# ⦁	Пилешко меню –  10.35 лв.
# ⦁	Меню с риба – 12.40 лв.
# ⦁	Вегетарианско меню  – 8.15 лв.

chicken = int(input()) * 10.35
fish = int(input()) * 12.40
vegetarian = int(input()) * 8.15

dessert = (chicken + fish + vegetarian) * 0.20

total_cost = chicken + fish + vegetarian + dessert + 2.50

print(total_cost)