# First, you will receive a sequence of integers representing the number of materials for crafting toys in one box.
# After that, you will be given another sequence of integers – their magic level.
# Your task is to mix materials with magic so you can craft presents,
# listed in the table below with the exact magic level:

# Present        Magic needed
# Doll               150
# Wooden train       250
# Teddy bear         300
# Bicycle            400

# You should take the last box with materials and the first magic level value to craft a toy.
# Their multiplication calculates the total magic level.
# If the result equals one of the levels described in the table above,
# you craft the present and remove both materials and magic value.
# Otherwise:
# · If the product of the operation is a negative number, you should sum the values together,
# remove them both from their positions, and add the result to the materials.
# · If the product doesn't equal one of the magic levels in the table and is a positive number,
# remove only the magic value and increase the material value by 15.
# · If the magic or material (or both) equals 0, remove it (or both) and continue crafting the presents.
# Stop crafting presents when you run out of boxes of materials or magic-level values.
# Your task is considered done if you manage to craft either one of the pairs:
# · a doll and a train
# · a teddy bear and a bicycle
# Input
# · The first line of input will represent the values of boxes with materials - integers, separated by a single space
# · On the second line, you will be given the magic values - integers again, separated by a single space
# Output
# · On the first line - print whether you've succeeded in crafting the presents:
# o "The presents are crafted! Merry Christmas!"
# o "No presents this Christmas!"
# · On the next two lines print the materials and magic that are left, if there are any (otherwise skip the line)
# o "Materials left: {material_N}, {material_N-1}, … {material_1}"
# o "Magic left: {magicValue_1}, {magicValue_2}, … {magicValue_N}"
# · On the next lines print the presents you have crafted, ordered alphabetically in the format:
# o "{toy_name1}: {amount}
# {toy_name2}: {amount}
# ...
# {toy_nameN}: {amount}"
# Constraints
# · All the materials' values will be integers in the range [-100, 100]
# · Magic level values will be integers in the range [-100, 100]
# · In all cases, at least one present will be crafted
# input                                               output
# 10 -5 20 15 -30 10                  The presents are crafted! Merry Christmas!
# 40 60 10 4 10 0                     Materials left: 20, -5, 10 Bicycle: 1 Teddy bear: 2

from collections import deque


def removal(list_one, list_two):
    list_one.pop()
    list_two.popleft()
    return list_one, list_two


box_of_materials = [int(x) for x in input().split()]
magic_level = deque(int(x) for x in input().split())

toys_to_craft = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

needed_pairs = [["Doll", "Wooden train"], ["Teddy bear", "Bicycle"]]

crafted_toys = {}

while box_of_materials and magic_level:
    material = box_of_materials[-1]
    magic = magic_level[0]
    total_magic_level = material * magic

    # if material == 0 and magic == 0:
    #     removal(box_of_materials, magic_level)
    #     continue
    # if material == 0:
    #     box_of_materials.pop()
    #     continue
    # if magic == 0:
    #     magic_level.popleft()
    #     continue

    if total_magic_level in toys_to_craft:
        if toys_to_craft[total_magic_level] not in crafted_toys:
            crafted_toys[toys_to_craft[total_magic_level]] = 0
        crafted_toys[toys_to_craft[total_magic_level]] += 1
        removal(box_of_materials, magic_level)
    elif total_magic_level < 0:
        new_material = material + magic
        removal(box_of_materials, magic_level)
        box_of_materials.append(new_material)
    elif total_magic_level > 0:
        magic_level.popleft()
        box_of_materials[-1] += 15
    else:
        if material == 0:
            box_of_materials.pop()
        if magic == 0:
            magic_level.popleft()

ding_ding = False
for pair, pear in needed_pairs:
    if pair in crafted_toys and pear in crafted_toys:
        ding_ding = True
print("The presents are crafted! Merry Christmas!" if ding_ding else "No presents this Christmas!")

if box_of_materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(box_of_materials))}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

for present, amount in crafted_toys.items():
    print(f"{present}: {amount}")

# 60/100