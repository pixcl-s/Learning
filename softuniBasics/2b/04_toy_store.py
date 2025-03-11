
# Петя има магазин за детски играчки. Тя получава голяма поръчка,
# която трябва да изпълни. С парите, които ще спечели иска да отиде на екскурзия.
# Цени на играчките:
# ⦁	Пъзел - 2.60 лв.
# ⦁	Говореща кукла - 3 лв.
# ⦁	Плюшено мече - 4.10 лв.
# ⦁	Миньон - 8.20 лв.
# ⦁	Камионче - 2 лв.
# Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена.
# От спечелените пари Петя трябва да даде 10% за наема на магазина.
# Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.

holiday_price = float(input())
puzzle = int(input())
talking_doll = int(input())
teddy_bear = int(input())
minion = int(input())
truck = int(input())

sum_products = puzzle + talking_doll + teddy_bear + minion + truck

total_price = puzzle * 2.6 + talking_doll * 3 + teddy_bear * 4.1 + minion * 8.2 + truck * 2

if sum_products >= 50:
    total_price = total_price - total_price * 0.25

rent = total_price * 0.1

money_left = total_price - rent - holiday_price

if money_left >= 0:
    print(f"Yes! {money_left:.2f} lv left.")
else:
    print(f"Not enough money! {abs(money_left):.2f} lv needed.")
