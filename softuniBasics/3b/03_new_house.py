
# Марин и Нели си купуват къща недалеч от София. Нели толкова много обича цветята,
# че Ви убеждава да напишете програма, която да изчисли колко ще им струва,
# за да засадят определен брой цветя и дали наличният бюджет ще им е достатъчен.

#        Роза	Далия	Лале	Нарцис	Гладиола
#   	  5 	3.80	2.80	  3	      2.50

# Съществуват следните отстъпки:

# ⦁	Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# ⦁	Ако Нели купи повече от 90  Далии - 15% отстъпка от крайната цена;
# ⦁	Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# ⦁	Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# ⦁	Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.

# От конзолата се четат 3 реда:
# ⦁	Вид цветя - текст с възможности "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
# ⦁	Брой цветя - цяло число;
# ⦁	Бюджет - цяло число.
# Да се отпечата на конзолата на един ред:

# ⦁	Ако бюджетът им е достатъчен - "Hey, you have a great garden
# with {броя цвета} {вид цветя} and {останалата сума} leva left.";

# ⦁	Ако бюджета им е НЕ достатъчен - "Not enough money, you need {нужната сума} leva more.".

# Сумата да бъде форматирана до втория знак след десетичната запетая.

flower = input()
quantity = int(input())
budget = int(input())

roses = quantity * 5
dahlias = quantity * 3.80
tulips = quantity * 2.80
narcissus = quantity * 3
gladiolus = quantity * 2.50

discount = ""
budget_left = ""

if flower == "Roses":
    budget_left = budget - roses
    if quantity > 80:
        discount = 0.1
        roses = roses - (roses * discount)
        budget_left = budget - roses
elif flower == "Dahlias":
    budget_left = budget - dahlias
    if quantity > 90:
        discount = 0.15
        dahlias = dahlias - (dahlias * discount)
        budget_left = budget - dahlias
elif flower == "Tulips":
    budget_left = budget - tulips
    if quantity > 80:
        discount = 0.15
        tulips = tulips - (tulips * discount)
        budget_left = budget - tulips
elif flower == "Narcissus":
    budget_left = budget - narcissus
    if quantity < 120:
        discount = -0.15
        narcissus = narcissus - (narcissus * discount)
        budget_left = budget - narcissus
elif flower == "Gladiolus":
    budget_left = budget - gladiolus
    if quantity < 80:
        discount = -0.2
        gladiolus = gladiolus - (gladiolus * discount)
        budget_left = budget - gladiolus


if budget_left >= 0:
    print(f"Hey, you have a great garden with {quantity} {flower} and {budget_left:.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(budget_left):.2f} leva more.")

