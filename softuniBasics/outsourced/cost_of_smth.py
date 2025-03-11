#
# A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.

quantity = int(input())

price = quantity * 100

if quantity > 1000:
    discount = price * 0.1

final_price = price - discount

print(f"{final_price:.2f}")

