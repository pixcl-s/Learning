
# You will be given key-value pairs of products and quantities (on a single line separated by space).
# On the following line, you will be given products to search for. Check for each product.
# You have 2 possibilities:
# ⦁	If you have the product, print "We have {quantity} of {product} left".
# ⦁	Otherwise, print "Sorry, we don't have {product}".

items = input().split()
look_for = input().split()

item_dictionary = {}

for x in range(0, len(items), 2):
    item_dictionary[items[x]] = int(items[x+1])

for y in look_for:
    if y in item_dictionary.keys():
        print(f"We have {item_dictionary[y]} of {y} left")
    else:
        print(f"Sorry, we don't have {y}")