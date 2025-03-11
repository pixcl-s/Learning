
# Снимките за дългоочаквания филм "Годзила срещу Конг" започват.
# Сценаристът Адам Уингард ви моли да напишете програма, която да изчисли,
# дали предвидените средства са достатъчни за снимането на филма.
# За снимките  ще бъдат нужни определен брой статисти, облекло за всеки един статист и декор.
# Известно е, че:
# ⦁	Декорът за филма е на стойност 10% от бюджета.
# ⦁	При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.

budget = float(input())
extras = int(input())
clothes_price = float(input())

clothes = extras

decor = budget * 0.1

if extras > 150:
    clothes_price = clothes_price - clothes_price * 0.1

clothes_and_decor = clothes_price * clothes + decor

budget_left = budget - clothes_and_decor

if clothes_and_decor > budget:
    print("Not enough money!")
    print(f"Wingard needs {abs(budget_left):.2f} leva more.")

if clothes_and_decor <= budget:
    print("Action!")
    print(f"Wingard starts filming with {budget_left:.2f} leva left.")
