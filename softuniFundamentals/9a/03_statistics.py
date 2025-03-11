
# You will be receiving key-value pairs on separate lines separated by ": " until you receive the command "statistics".
# Sometimes you may receive a product more than once.
# In that case, you have to add the new quantity to the existing one.
# When you receive the "statistics" command, print the following:
# "Products in stock:
# - {product1}: {quantity1}
# - {product2}: {quantity2}
# …
# - {productN}: {quantityN}
# Total Products: {count_all_products}
# Total Quantity: {sum_all_quantities}"

the_products = {}

while True:
    product = input()

    if product == "statistics":
        break

    product = product.split(": ")

    if product[0] in the_products:
        the_products[product[0]] += int(product[1])
    else:
        the_products[product[0]] = int(product[1])

print("Products in stock:")
for product, quantity in the_products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(the_products)}")
print(f"Total Quantity: {sum(the_products.values())}")
