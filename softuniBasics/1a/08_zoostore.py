# Напишете програма, която пресмята нужните разходи за закупуването на храна за кучета и котки.
# Храната се пазарува от зоомагазин, като една опаковка храна за кучета е на цена 2.50 лв,
# а опаковка храна за котки струва 4 лв.

dog_food = int(input())
cat_food = int(input())

total = str(dog_food * 2.50 + cat_food * 4)

print(total + " lv.")

