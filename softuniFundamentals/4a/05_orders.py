
# Write a function that calculates the total price of an order and returns it.
# The function should receive one of the following products: "coffee", "coke", "water", or "snacks",
# and a quantity of the product. The prices for a single piece of each product are:
# ⦁	coffee - 1.50
# ⦁	water - 1.00
# ⦁	coke - 1.40
# ⦁	snacks - 2.00
#
# Print the result formatted to the second decimal place.

def coffee(amount):
    return amount * 1.5


def water(amount):
    return amount * 1


def coke(amount):
    return amount * 1.4


def snacks(amount):
    return amount * 2


def complete_order(drink):
    if drink == "coffee":
        return coffee(quantity)
    elif drink == "water":
        return water(quantity)
    elif drink == "coke":
        return coke(quantity)
    elif drink == "snacks":
        return snacks(quantity)


order = input()
quantity = int(input())

print(f"{complete_order(order):.2f}")
