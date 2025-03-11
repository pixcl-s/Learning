
# You will be given a sequence of strings, each on a new line until you receive the "stop" command.
# Every odd line on the console represents a resource (e.g., Gold, Silver, Copper, and so on) and every even - quantity.
# Your task is to collect the resources and print them each on a new line.
# Print the resources and their quantities in the following format:
# "{resource} -> {quantity}"

mining = {}

while True:
    mineral = input()
    if mineral == "stop":
        break
    quantity = int(input())

    if mineral not in mining:
        mining[mineral] = 0
    mining[mineral] += quantity

for x, y in mining.items():
    print(f"{x} -> {y}")
