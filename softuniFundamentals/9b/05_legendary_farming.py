
# You are playing a game, and your goal is to win a legendary item - any legendary item will be good enough.
# However, it's a tedious process, and it requires quite a bit of farming. The possible items are:
# "Shadowmourne" - requires 250 Shards
# "Valanyr" - requires 250 Fragments
# "Dragonwrath" - requires 250 Motes
# "Shards", "Fragments", and "Motes" are the key materials 	(case-insensitive), and everything else is junk.
# You will be given lines of input in the format:
# "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
# Keep track of the key materials - the first one that reaches 250, wins the race.
# At that point, you have to print that the corresponding legendary item is obtained.
# In the end, print the remaining shards, fragments, and motes in the format:
# "shards: {number_of_shards}
# fragments: {number_of_fragments}
# motes: {number_of_motes}"
# Finally, print the collected junk items in the order of appearance.
# Input
# Each line comes in the following format: "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
# Output
# On the first line, print the obtained item in the format: "{Legendary item} obtained!"
# On the next three lines, print the remaining key materials
# On the several final lines, print the junk items
# All materials should be printed in the format: "{material}: {quantity}"
# The output should be lowercase, except for the first letter of the legendary

legendary_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
breaking = False

while True:
    farmed = input().split()
    farmed = [y.lower() for y in farmed]

    for x in range(0, len(farmed), 2):
        if farmed[x + 1] == "shards" or farmed[x + 1] == "fragments" or farmed[x + 1] == "motes":
            legendary_materials[farmed[x + 1]] += int(farmed[x])
        else:
            junk[farmed[x + 1]] = 0
            junk[farmed[x + 1]] += int(farmed[x])

        if legendary_materials["shards"] >= 250:
            print("Shadowmourne obtained!")
            legendary_materials["shards"] -= 250
            breaking = True
            break
        elif legendary_materials["fragments"] >= 250:
            print("Valanyr obtained!")
            legendary_materials["fragments"] -= 250
            breaking = True
            break
        elif legendary_materials["motes"] >= 250:
            print("Dragonwrath obtained!")
            legendary_materials["motes"] -= 250
            breaking = True
            break
    if breaking:
        break

for z in legendary_materials:
    print(f"{z}: {legendary_materials[z]}")

for trash, quantity in junk.items():
    print(f"{trash}: {quantity}")
