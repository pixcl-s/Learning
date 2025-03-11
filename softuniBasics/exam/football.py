
# Като един истински запалянко Пепи решил да се подготви за световното първенство,
# като си закупи екип на любимия си футболен отбор.
# В магазина, в който пазарувал предлагали тениски, шорти, чорапи и бутонки.

# Знае се, че цената на шортите е 75% от цената на тениските,
# а цената на чорапите е 20% от цената на шортите.
# Бутонките струват два пъти колкото тениската и шортите взети заедно.

# Тъй като Пепи редовно пазарува от този магазин,
# той има карта за отстъпка на стойност 15% от общата сума на покупката.
# Ако сметката на Пепи е по-висока или равна на дадена сума,
# той получава подарък – точно копие на топката от световното.
# Напишете програма, която изчислява дали Пепи е спечелил топката.

# Входът се чете от конзолата и съдържа точно 2 реда:
# На първия ред - цената на тениската – реално число в интервала [1.00 ... 1000.00]
# На втория ред - сумата, която трябва да достигне, за да спечели топка – реално число в интервала [100.00...10 000.00]

# На конзолата се отпечатват два реда:
# Ако топката Е спечелена:
# "Yes, he will earn the world-cup replica ball!"
# "His sum is {сумата} lv."
# Ако  топката НЕ Е спечелена:
# "No, he will not earn the world-cup replica ball."
# "He needs {недостигащи пари} lv. more."
# Резултатът да бъде форматиран до втората цифра след десетичната запетая.

shirt_price = float(input())
ball_money_needed = float(input())

shorts_price = shirt_price * 0.75
socks_price = shorts_price * 0.20
shoes_price = (shirt_price + shorts_price) * 2

discount = 0.15

total_price = shirt_price + shorts_price + socks_price + shoes_price

discounted_price = total_price - (total_price * discount)

if discounted_price >= ball_money_needed:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {discounted_price:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {(ball_money_needed - discounted_price):.2f} lv. more.")
