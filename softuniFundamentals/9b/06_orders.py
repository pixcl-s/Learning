
# Write a program that keeps the information about products and their prices.
# Each product has a name, a price, and a quantity:
# If the product doesn't exist yet, add it with its starting quantity.
# If you receive a product, that already exists, increase its quantity by the input quantity
# and if its price is different, replace the price as well.
# You will receive products' names, prices, and quantities on new lines.
# Until you receive the command "buy", keep adding items.
# Finally, print all items with their names and the total price of each product.
# Input
# Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
# The product data is always delimited by a single space.
# Output
# Print information about each product in the following format:
# "{product_name} -> {total_price}"
# Format the total price to the 2nd digit after the decimal separator.

storage = {}
lul = "lul"
pog = "pog"
while True:
    product = input()
    if product == "buy":
        break
    item, price, quantity = product.split()
    if item not in storage:
        storage[item] = {"lul": 0, "pog": 0}
    storage[item][lul] = float(price)
    storage[item][pog] += float(quantity)

for x in storage:
    print(f"{x} -> {float(storage[x][lul]) * float(storage[x][pog]):.2f}")

