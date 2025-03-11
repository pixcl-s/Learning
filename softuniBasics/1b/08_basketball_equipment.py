
# Джеси решава, че иска да се занимава с баскетбол, но за да тренира е нужна екипировка.
# Напишете програма, която изчислява какви разходи ще има Джеси, ако започне да тренира,
# като знаете колко е таксата за тренировки по баскетбол за период от 1 година.
# Нужна екипировка:
# ⦁	Баскетболни кецове – цената им е 40% по-малка от таксата за една година
# ⦁	Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
# ⦁	Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
# ⦁	Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка

yearly_tax = int(input())

basketball_shoes = yearly_tax - (yearly_tax * 0.40)
basketball_clothes = basketball_shoes - (basketball_shoes * 0.20)
basketball_ball = basketball_clothes / 1/4
basketball_accessories = basketball_ball / 1/5

total = basketball_shoes + basketball_clothes + basketball_ball +basketball_accessories + yearly_tax

print(total)
