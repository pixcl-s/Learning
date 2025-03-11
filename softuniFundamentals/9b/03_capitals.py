
# Using dictionary comprehension, write a program that receives country names on the first line,
# separated by comma and space ", ", and their corresponding capital cities on the second line
# (again separated by comma and space ", ").
# Print each country with its capital on a separate line in the following format: "{country} -> {capital}".

countries = input().split(", ")
capitals = input().split(", ")

combined = {key: value for key, value in zip(countries, capitals)}

for pog, dog in combined.items():
    print(f"{pog} -> {dog}")
