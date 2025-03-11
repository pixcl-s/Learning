
# You will receive a single line containing some food (keys) and quantities (values).
# They will be separated by a single space (the first element is the key, the second – is the value, and so on).
# Create a dictionary with all the keys and values and print it on the console.

food = input().split()

food_dictionary = {}

for x in range(0, len(food), 2):
    food_dictionary[food[x]] = int(food[x+1])

print(food_dictionary)
