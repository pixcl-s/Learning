
# Тони и приятели много обичат да ходят за риба и са толкова запалени по риболова,
# че решават да отидат на риболов с кораб. Цената за наема на кораба зависи от сезона и броя рибари:

# В зависимост от сезона:

# ⦁	Цената за наем на кораба през пролетта е  3000 лв.;
# ⦁	Цената за наем на кораба през лятото и есента е  4200 лв.;
# ⦁	Цената за наем на кораба през зимата е  2600 лв.

# В зависимост от броя на групата има различна отстъпка:

# ⦁	Ако групата е до 6 човека включително  -  отстъпка от 10%;
# ⦁	Ако групата е от 7 до 11 човека включително  -  отстъпка от 15%;
# ⦁	Ако групата е от 12 нагоре  -  отстъпка от 25%.

# Рибарите ползват допълнително 5% отстъпка, ако са четен брой,
# освен ако не е есен - тогава нямат допълнителна отстъпка,
# която се начислява след като се приспадне отстъпката по горните критерии.
# Напишете програма, която да пресмята дали рибарите ще съберат достатъчно пари.

# От конзолата се четат три реда:
# ⦁	Бюджет на групата - цяло число;
# ⦁	Сезон -  текст: "Spring", "Summer", "Autumn" или "Winter";
# ⦁	Брой рибари - цяло число.

# На конзолата да се отпечата следното:
# ⦁	Ако бюджетът е достатъчен:
# "Yes! You have {останалите пари} leva left."
# ⦁	Ако бюджетът НЕ Е достатъчен:
# "Not enough money! You need {сумата, която не достига} leva."
# Сумите трябва да са форматирани с точност до два знака след десетичната запетая.

budget = int(input())
season = input().lower()
fishermen = int(input())

ship_rent = ""
discount = ""

if season == "spring":
    ship_rent = 3000
elif season == "summer" or season == "autumn":
    ship_rent = 4200
elif season == "winter":
    ship_rent = 2600

if fishermen <= 6:
    discount = ship_rent * 0.1
elif 7 <= fishermen <= 11:
    discount = ship_rent * 0.15
elif fishermen >= 12:
    discount = ship_rent * 0.25

discounted_price = ship_rent - discount

if season != "autumn" and fishermen % 2 == 0:
    additional_discount = 0.05
    discounted_price = discounted_price - (ship_rent * additional_discount)

final = budget - discounted_price

if final >= 0:
    print(f"Yes! You have {final:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(final):.2f} leva.")
