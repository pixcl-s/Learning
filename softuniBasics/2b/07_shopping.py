#
# Петър иска да купи N видеокарти, M процесора и P на брой рам памет.
# Ако броя на видеокартите е по-голям от този на процесорите получава 15% отстъпка от крайната сметка.
# Важат следните цени:
# ⦁	Видеокарта – 250 лв./бр.
# ⦁	Процесор – 35% от цената на закупените видеокарти/бр.
# ⦁	Рам памет – 10% от цената на закупените видеокарти/бр.
# Да се изчисли нужната сума за закупуване на материалите и да се пресметне дали бюджета ще му стигне.

budget = float(input())
video_card = int(input())
processor = int(input())
ram = int(input())

video_card_price = video_card * 250
processor_price = (video_card_price * 0.35) * processor
ram_price = (video_card_price * 0.1) * ram

total_price = video_card_price + processor_price + ram_price

if video_card > processor:
    total_price = total_price - (total_price * 0.15)

leftover = budget - total_price

if total_price <= budget:
    print(f"You have {leftover:.2f} leva left!")
else:
    print(f"Not enough money! You need {abs(leftover):.2f} leva more!")
