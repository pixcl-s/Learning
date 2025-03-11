
# Хотел предлага 2 вида стаи: студио и апартамент.
# Напишете програма, която изчислява цената за целия престой за студио и апартамент.

# Цените зависят от месеца на престоя:
# Май и октомври                       Юни и септември                        Юли и август
# Студио - 50 лв./нощувка              Студио - 75.20 лв./нощувка             Студио - 76 лв./нощувка
# Апартамент - 65 лв./нощувка          Апартамент - 68.70 лв./нощувка         Апартамент - 77 лв./нощувка

# Предлагат се и следните отстъпки:
# ⦁	За студио, при повече от 7 нощувки през май и октомври : 5% намаление.
# ⦁	За студио, при повече от 14 нощувки през май и октомври : 30% намаление.
# ⦁	За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
# ⦁	За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление.

# Вход
# Входът се чете от конзолата и съдържа точно 2 реда, въведени от потребителя:
# ⦁	На първия ред е месецът - May, June, July, August, September или October;
# ⦁	На втория ред е броят на нощувките - цяло число.

# Изход
# Да се отпечатат на конзолата 2 реда:
# ⦁	На първия ред: "Apartment: {цена за целият престой} lv."
# ⦁	На втория ред: "Studio: {цена за целият престой} lv."
# Цената за целия престой да е форматирана с точност до два знака след десетичната запетая.

month = input().lower()
nights = int(input())

studio = 0
apartment = 0
discount_studio = 0
discount_apartment = 0

if month == "may" or month == "october":
    studio = 50
    apartment = 65
    if nights > 14:
        discount_studio = 0.3
        discount_apartment = 0.1
    elif nights > 7:
        discount_studio = 0.05
elif month == "june" or month == "september":
    studio = 75.20
    apartment = 68.70
    if nights > 14:
        discount_studio = 0.2
        discount_apartment = 0.1
elif month == "july" or month == "august":
    studio = 76
    apartment = 77
    if nights > 14:
        discount_apartment = 0.1

night_studio = studio * nights
night_apartment = apartment * nights

total_studio = night_studio - (night_studio * discount_studio)
total_apartment = night_apartment - (night_apartment * discount_apartment)

print(f"Apartment: {total_apartment:.2f} lv.")
print(f"Studio: {total_studio:.2f} lv.")
