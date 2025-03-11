# Напишете програма, която изчислява необходимата сума,
# която Божидара ще трябва да заплати на фирмата изпълнител на проекта.
# Цената на един кв. м. е 7.61 лв със ДДС.
# Понеже нейният двор е доста голям, фирмата изпълнител предлага 18% отстъпка от крайната цена.


square_meter = float(input())
full_price = square_meter * 7.61
discount = 0.18 * full_price
final_price = full_price - discount


print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")