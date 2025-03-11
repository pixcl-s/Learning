
# Create a class Zoo.
# It should have a class attribute called __animals that stores the total count of the animals in the zoo.
# The __init__ method should only receive the name of the zoo.
# There you should also create 3 empty lists (mammals, fish, birds). The class should also have 2 more methods:
# ⦁	add_animal(species, name) - based on the species, adds the name to the corresponding list
# ⦁	get_info(species) - based on the species returns a string in the following format:
# "{Species} in {zoo_name}: {names}
# Total animals: {total_animals}"
# On the first line, you will receive the name of the zoo.
# On the second line, you will receive number n.
# On the following n lines you will receive animal info in the format: "{species} {name}".
# Add the animal to the zoo to the corresponding list. The species could be "mammal", "fish", or "bird".
# On the final line, you will receive a species.
# At the end, print the info for that species and the total count of animals in the zoo.

class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fish = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fish.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        to_print = ""
        if species == "mammal":
            to_print += f"Mammals in {self.name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            to_print += f"Fish in {self.name}: {', '.join(self.fish)}\nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            to_print += f"Birds in {self.name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"
        return to_print


zoo_name = input()
zoo = Zoo(zoo_name)
number = int(input())

for _ in range(number):
    animals = input().split()
    species, animal = animals
    zoo.add_animal(species, animal)

speciess = input()
print(zoo.get_info(speciess))
