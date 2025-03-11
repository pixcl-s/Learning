
# Всяка година Дядо Коледа избира различни дестинации за почивка.
# Тази година той решава да прекара почивните си дни в България.
# Неговите верни приятели – джуджетата, му предлагат да се настани в един
# от най-престижните хотели, а именно "Четири сезона".
# По време на престоя си там, той трябва да избере между следните видове помещения,
# със следните цени за престой:

# "room for one person" – 18.00 лв за нощувка
# "apartment" – 25.00 лв за нощувка
# "president apartment" – 35.00 лв за нощувка

# Според броят на дните, в които Дядо Коледа ще остане в хотела (пример: 11 дни = 10 нощувки)
# и видът на помещението, което ще избере, той може да ползва различно намаление.
# Намаленията спрямо дните и помещението са както следва:

# вид помещение         	по-малко от 10 дни	   между 10 и 15 дни	    повече от 15 дни
# room for one person	   не ползва намаление	  не ползва намаление	   не ползва намаление
# apartment	               30% от крайната цена	  35% от крайната цена	   50% от крайната цена
# president apartment	   10% от крайната цена	  15% от крайната цена	   20% от крайната цена

# След престоя си в хотела, оценката на Дядо Коледа за услугите на хотела може да е
# позитивна (positive) или негативна (negative). Ако оценката му е позитивна,
# към цената с вече приспаднатото намаление Дядо Коледа добавя 25%  към нея.
# Ако оценката му е негативна приспада от цената 10%.

# Входът се чете от конзолата и се състои от три реда:
# Първи ред – дни за престой – цяло число в интервала [0...365]
# Втори ред –  вид помещение –  "room for one person",  "apartment" или "president apartment"
# Трети ред –  оценка - "positive"  или "negative"

# На конзолата трябва да се отпечата един ред.
# Цената за престоят му в хотела, форматирана до втория знак след десетичната запетая

days_to_stay = int(input())
room_type = input()
review = input()

total_price = 0
discount = 0
tax = 0

if room_type == "room for one person":
    total_price = (days_to_stay - 1) * 18

elif room_type == "apartment":
    total_price = (days_to_stay - 1) * 25
    if days_to_stay < 10:
        discount = total_price * 0.30
    elif 10 < days_to_stay < 15:
        discount = total_price * 0.35
    elif days_to_stay > 15:
        discount = total_price * 0.50

elif room_type == "president apartment":
    total_price = (days_to_stay - 1) * 35
    if days_to_stay < 10:
        discount = total_price * 0.10
    elif 10 < days_to_stay < 15:
        discount = total_price * 0.15
    elif days_to_stay > 15:
        discount = total_price * 0.20


if review == "positive":
    tax = (total_price - discount) * 0.25
    print(f"{((total_price - discount) + tax):.2f}")
elif review == "negative":
    tax = (total_price - discount) * 0.10
    print(f"{((total_price - discount) - tax):.2f}")
