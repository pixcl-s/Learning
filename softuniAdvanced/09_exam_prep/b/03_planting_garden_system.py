# Create a function named plant_garden that receives information about the available space in the garden, the plot size for each allowed plant type,
# and the requested plant types for planting with their quantities (pieces) and returns a sorted result as one formatted string. It will receive one positional argument,
# followed by an unknown number of arguments (tuples) and keyword arguments (key-value pairs). See the Examples section.
# The arguments will be passed as follows:
# · The positional argument represents the available garden space (in square meters) - a float number in the range [0.1, 100.0].
# · The next group of arguments represents the allowed types of plants and their space requirements, containing an unknown number of tuples with two elements:
# o The first element represents the unique plant type (a valid string).
# o The second element represents the space required per plant (a positive float number).
# · The last group of arguments represents the planting requests and contains an unknown number of keyword arguments (key-value pairs).
# o The key represents the unique plant type (a valid string).
# o The value represents the pieces (quantity) from that plant type owners want to grow (a positive integer, greater than zero).
# The function should track the planting process:
# · Sort the planting requests by plant type alphabetically.
# · For each requested plant type from the group of sorted keyword arguments (planting requests), check if it exists in the provided group of allowed plant types (first group of arguments with plant type and space requirements).
# o If the plant type exists and there is enough space, plant as many pieces as possible based on the provided quantity and available garden space. See the Examples section.
# § If space allows only partial planting (not all requested plant pieces can be planted), plant as many as possible within the space limits, but this will affect the outcome.
# o If the requested plant type doesn't exist in the first group of allowed types, ignore it and do not count it in the outcome.
# · Stop planting when the available garden space is used up or there are no more requests for planting.
# At the end, return the output, depending on the outcome as described below:
# · If you managed to plant all the requested plants at their full quantity (pieces), return the message:
# "All plants were planted! Available garden space: {available_space} sq meters."
# o Format the available space to the first decimal place.
# o Partial planting of the requested quantity will be considered an unsuccessful outcome.
# · If you ran out of space before planting all requested plants, return the message:
# "Not enough space to plant all requested plants!"
# · On the following lines, return the planted plant types and the pieces of each type planted, sorted alphabetically by plant type, one per line (see the Examples section):
# "Planted plants:
# {plant_type1}: {pieces}
# {plant_type2}: {pieces}
# ...
# {plant_typen}: {pieces}"
# Note: Submit only the function in the judge system
# Output
# · Return the appropriate message based on whether all plants were planted, along with details about the planted types as described above.
# Constraints
# · The first positional argument will always be a float number in the range [0.1, 100.0].
# · The group of arguments will always be before the group of keyword arguments.
# · Each tuple from the first group of arguments will always provide the allowed unique plant type (a valid string) and the space required per plant (a positive float number).
# · Each keyword argument from the second group will always provide a unique plant type (a valid string) and the pieces requested for planting (a positive integer, greater than zero).
# · You will always receive at least one tuple and at least one keyword argument.
# · There will always be at least one planted plant.

def plant_garden(garden, *args, **kwargs):
    to_return = ""
    allowed_flowers = {}
    planted_flowers = {}

    for x in kwargs.keys():
        for y in args:
            if x in y[0]:
                allowed_flowers[x] = {"to_plant": kwargs[x], "space_req": y[1]}
                break

    allowed_flowers = dict(sorted(allowed_flowers.items()))

    plant_check = True

    for flower, seeds in allowed_flowers.items():
        planting = seeds["to_plant"] * seeds["space_req"]
        free_space_for_plant = garden // seeds["space_req"]
        if planting <= garden:
            planted_flowers[flower] = seeds["to_plant"]
            garden -= planting
        elif planting > garden and free_space_for_plant != 0:
            plant_check = False
            planted_flowers[flower] = free_space_for_plant
            garden -= free_space_for_plant * seeds["space_req"]

    if not plant_check or len(planted_flowers) != len(allowed_flowers):
        to_return += "Not enough space to plant all requested plants!\n"
    else:
        to_return += f"All plants were planted! Available garden space: {garden:.1f} sq meters.\n"
    to_return += "Planted plants:\n"
    for key, value in planted_flowers.items():
        to_return += f"{key}: {int(value)}\n"

    return to_return

# 100/100


# test
print(plant_garden(50.0, ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20))
print(plant_garden(20.0, ("rose", 2.0), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, sunflower=5))
print(plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4, tulip=15, sunflower=3, daisy=4))
print(plant_garden(50.0, ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, daisy=1))


# def plant_garden(garden, *args, **kwargs):
#     to_return = ""
#     free_space = garden
#
#     sorted_plants = dict(sorted(kwargs.items()))
#     planted_plants = {}
#     everything_planted = True
#
#     for x, y in sorted_plants.items():
#         for z in args:
#             if x == z[0]:
#                 if free_space//z[1] >= y:
#                     planted_plants[x] = y
#                     free_space -= y*z[1]
#                 elif free_space//z[1] < y:
#                     everything_planted = False
#                     y = free_space // z[1]
#                     if y == 0 or free_space == 0:
#                         break
#                     planted_plants[x] = y
#                     free_space -= y
#                 break
#     to_return += f"All plants were planted! Available garden space: {free_space:.1f} sq meters.\n" if everything_planted\
#         else "Not enough space to plant all requested plants!\n"
#     to_return += "Planted plants:\n"
#     for key, value in planted_plants.items():
#         to_return += f"{key}: {int(value)}\n"
#     return to_return
# # 78/100
