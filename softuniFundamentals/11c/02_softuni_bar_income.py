
import re

pattern = r"%([A-Z][a-z]+)%[^\|\$\%\.]*<(\w+)>[^\|\$\%\.]*\|(\d*)\|[^\|\$\%\.\d]*(\d+\.*\d*)\$"      #r"%([A-Z][a-z]+)%<(\w+)>\|(\d*)\|(\d+\.?\d*)\$"
total_income = 0

while True:
    customer = input()
    if customer == "end of shift":
        break
    valid_customer = re.search(pattern, customer)

    if valid_customer:
        name, product, quantity, price = valid_customer.groups()
        spend = int(quantity) * float(price)
        total_income += spend

        print(f"{name}: {product} - {spend:.2f}")

print(f"Total income: {total_income:.2f}")
