
# Write a program that reads an integer number representing a budget.
# On the following lines, it reads integer numbers representing
# the prices of each product you should buy until it receives the command "End".
# During the iterations, if there is not enough budget left to buy the next product,
# it prints "You went in overdraft!" and end the program.
# Otherwise, if you accomplished to buy all products before receiving "End", it prints "You bought everything needed."

budget = int(input())
product_price = input().lower()

spending = 0

while product_price != "end":
    spending += int(product_price)

    if spending > budget:
        print("You went in overdraft!")
        exit()

    product_price = input().lower()

print("You bought everything needed.")
