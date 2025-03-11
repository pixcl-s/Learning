
# You want to go to France by train, and the train ticket costs exactly 150$.
# You do not have enough money, so you decide to buy some items within your budget
# and then sell them at a higher price – with a 40% markup.
# You will receive a collection of items and a budget in the following format:
# {type->price|type->price|type->price……|type->price}
# {budget}
# The prices for each of the types cannot exceed a specific price, which is given below:

#       Type	    Maximum Price
#      Clothes	        50.00
#       Shoes	        35.00
#     Accessories	    20.50

# If the price for a particular item is higher than the maximum price, don't buy it.
# Every time you buy an item, you have to reduce the budget with its price value.
# If you don't have enough money for it, you can't buy it. Buy as many items as you can.
# Next, you should increase the price of each item you have successfully bought by 40% and then sell it.
# Calculate if the budget after selling all the items is enough to buy the train ticket.

# Input / Constraints
# On the 1st line, you will receive the items with their prices
# in the format described above – real numbers in the range [0.00……1000.00]
# On the 2nd line, you are going to be given the budget – a real number in the range [0.0….1000.0]

# Output
# First, print the list with the bought item’s new prices,
# formatted to the second decimal point in the following format:
# "{price1} {price2} {price3} … {priceN}"
# Second, print the profit, formatted to the second decimal point in the following format:
# "Profit: {profit}"
# Finally:
# If the budget is enough to buy the train ticket, print: "Hello, France!"
# Otherwise, print: "Not enough money."

merchandise = input().split("|")
budget = float(input())

bought_merch = []
sold_merch = []

for x in merchandise:
    individual_merch = x.split("->")
    item, cost = individual_merch[0], float(individual_merch[1])

    if item == "Clothes" and cost <= 50:
        if cost <= budget:
            budget -= cost
            bought_merch.append(cost)
    elif item == "Shoes" and cost <= 35:
        if cost <= budget:
            budget -= cost
            bought_merch.append(cost)
    elif item == "Accessories" and cost <= 20.50:
        if cost <= budget:
            budget -= cost
            bought_merch.append(cost)

for piece in bought_merch:
    sold_merch.append(piece + piece * 0.40)

for y in sold_merch:
    print(f"{y:.2f}",end=" ")
print("")

print(f"Profit: {sum(sold_merch) - sum(bought_merch):.2f}")

if sum(sold_merch) + budget >= 150:
    print("Hello, France!" )
else:
    print("Not enough money.")
