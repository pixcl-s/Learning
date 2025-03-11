
# Атанас решава да прекара отпуската си в Банско и да кара ски.
# Преди да отиде обаче, трябва да резервира хотел и да изчисли колко ще му струва престоя.
# Налични са следните видове помещения, със следните цени за престой:

# ⦁	"room for one person" – 18.00 лв за нощувка
# ⦁	"apartment" – 25.00 лв за нощувка
# ⦁	"president apartment" – 35.00 лв за нощувка

# Според броят на дните, в които ще остане в хотела (пример: 11 дни = 10 нощувки)
# и видът на помещението, което ще избере, той може да ползва различно намаление.
# Намаленията са както следва:

# вид помещение	            по-малко от 10 дни	    между 10 и 15 дни	    повече от 15 дни

# room for one person   	не ползва намаление	    не ползва намаление  	не ползва намаление
# apartment	                30% от крайната цена	35% от крайната цена	50% от крайната цена
# president apartment   	10% от крайната цена	15% от крайната цена	20% от крайната цена

# След престоя, оценката на Атанас за услугите на хотела може да е позитивна (positive)
# или негативна (negative) . Ако оценката му е позитивна,
# към цената с вече приспаднатото намаление Атанас добавя 25% от нея.
# Ако оценката му е негативна приспада от цената 10%.

# Вход
# Входът се чете от конзолата и се състои от три реда:
# ⦁	Първи ред - дни за престой - цяло число в интервала [0...365]
# ⦁	Втори ред - вид помещение - "room for one person", "apartment" или "president apartment"
# ⦁	Трети ред - оценка - "positive"  или "negative"

# Изход
# На конзолата трябва да се отпечата един ред:
# ⦁	Цената за престоят му в хотела, форматирана до втория знак след десетичната запетая.

days = int(input())
room = input()
rating = input()

one_person = 18
apartment = 25
president = 35

nights = days - 1

discount = 0
additional_discount = 0

if rating == "positive":
    additional_discount = 0.25
else:
    additional_discount = -0.1

if room == "room for one person":
    price_one_person = nights * one_person
    discounted_one_person = price_one_person + (price_one_person * additional_discount)
    print(f"{discounted_one_person:.2f}")
elif room == "apartment":
    price_apartment = nights * apartment
    if days < 10:
        discount = 0.3
    elif days <= 15:
        discount = 0.35
    elif days > 15:
        discount = 0.5
    discounted_apartment = price_apartment - (price_apartment * discount)
    additional_apartment = discounted_apartment + (discounted_apartment * additional_discount)
    print(f"{additional_apartment:.2f}")
elif room == "president apartment":
    price_president = nights * president
    if days < 10:
        discount = 0.1
    elif days <= 15:
        discount = 0.15
    elif days > 15:
        discount = 0.2
    discounted_president = price_president - (price_president * discount)
    additional_president = discounted_president + (discounted_president * additional_discount)
    print(f"{additional_president:.2f}")
