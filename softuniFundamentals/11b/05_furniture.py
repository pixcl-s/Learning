import re

bought_furniture = []
total_price = 0

while True:
    buying = input()
    pattern = r"(?i)>>([a-z]+)<<([0-9]+[.0-9]*)!([0-9]+)"
    if buying == "Purchase":
        break

    valid = re.search(pattern, buying)

    if valid:
        furniture, price, quantity = valid.groups()
        bought_furniture.append(furniture)
        total_price += float(price) * int(quantity)

print("Bought furniture:")
for x in bought_furniture:
    print(x)
print(f"Total money spend: {total_price:.2f}")
