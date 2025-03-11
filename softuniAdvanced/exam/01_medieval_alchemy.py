# Input Data
#  On the first line you will receive quantities of different substances the alchemist has stored, separated by a comma and space (", ").
#  On the second line you will receive levels of crystal energy, also separated by a comma and space (", ").
# End Conditions
# The alchemist's quest will end immediately, under the following circumstances:
#  The alchemist has successfully crafted all five potions.
#  If the alchemist runs out of substances or crystals before crafting all five potions.
# Alchemy Process
# Once per day, the alchemist enters a secret room where he carefully stores his substances and crystals.
#  To maintain their stability, he has stored the substances in a special container, placing each one on top of the previous. When he needs a substance, he takes the last one he stored.
#  He uses crystals as an energy source and always takes the first crystal.
# Crafting Logic
# Each day, the alchemist combines the last stored substance with the first crystal in line to try to craft a new potion:
#  The alchemist will not attempt to craft the same potion if it has already been crafted.
# o In this case, he tries to craft the next possible potion (follow the instructions below).
#  If the sum of the substance and crystal energy is equal to one of the required energy levels from the list of potions and it has not been crafted yet, the potion is successfully crafted and should be memorized.
# o The substance is consumed and disappears from its respective collection.
# o The crystal is exhausted and disappears from its collection too.
#  If the sum does not exactly match any of the required energy levels for the potions:
# o The alchemist tries to use the energy to craft the potion with the highest possible energy requirements which is less than the combined energy:
#  The used substance is removed from its collection.
#  The crystal is returned to the back of the sequence with a reduced (decreased by 20 units) energy level.
#  Do not return zero values to the collection.
#  If the crystal's energy drops to 0 or less, it is removed entirely.
# o If there is no potion with an energy requirement that matches or is less than the combined energy, the attempt fails.
#  The substance is lost entirely (remove it).
#  The crystal is returned to the back of the sequence with a reduced (decreased by 5 units) energy level.
#  Do not return zero values to the collection.
#  If the crystal's energy drops to 0 or less, it is removed entirely.
# Output
#  On the first line, print the outcome based on whether all five potions were crafted successfully:
# o If all potions are crafted: "Success! The alchemist has forged all potions!"
# o If not all potions are crafted: "The alchemist failed to complete his quest."
#  On the next line, print the crafted potions in the order they were prepared:
# "Crafted potions: {potion1}, {potion2} … {potionn}"
# o If no potions were crafted, skip this line.
#  Finally, print the state of both sequences on separate lines.
# o If a sequence is empty, skip its line.
# o Substances must be printed in stack order (from the last to the first element).
# "Substances: {substancen}, {substancen-1} … {substance1}"
# "Crystals: {crystal1}, {crystal2} … {crystaln}"
# Constraints
#  All given numbers will be valid integers in the range [1 - 120]
#  Both sequences will initially have at least one element

from collections import deque

potions_to_craft = {110: "Brew of Immortality", 100: "Essence of Resilience",
                    90: "Draught of Wisdom", 80: "Potion of Agility", 70: "Elixir of Strength"}

crafted_potions = []

substances = [int(x) for x in input().split(", ")]
crystals = deque([int(x) for x in input().split(", ")])

while substances and crystals:
    substance = substances.pop()
    crystal = crystals.popleft()

    magic = substance + crystal

    if magic in potions_to_craft:
        crafted_potions.append(potions_to_craft[magic])
        del potions_to_craft[magic]
        if not potions_to_craft:
            break
        continue

    for y in potions_to_craft:
        if magic > y:
            crafted_potions.append(potions_to_craft[y])
            del potions_to_craft[y]
            if crystal - 20 > 0:
                crystals.append(crystal-20)
            break
    else:
        if crystal - 5 > 0:
            crystals.append(crystal - 5)

    if not potions_to_craft:
        break

print("The alchemist failed to complete his quest." if potions_to_craft
      else "Success! The alchemist has forged all potions!")

if crafted_potions:
    print(f"Crafted potions: {', '.join(crafted_potions)}")

if substances:
    print(f"Substances: {', '.join(str(x) for x in substances[::-1])}")

if crystals:
    print(f"Crystals: {', '.join(str(x) for x in crystals)}")

# 100/100

# 40, 5, 80, 60, 75, 60, 65, 70
# 20, 35, 45, 25, 10, 30, 15

# 45, 65, 35, 25, 70
# 15, 30, 20, 10, 5, 40