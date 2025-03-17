# class Animal:
#     def __init__(self, species):
#         self.species = species
#
#     def get_species(self):
#         return self.species
#
#
# def animal_sound(animals: list):
#     for animal in animals:
#         if animal.species == 'cat':
#             print('meow')
#         elif animal.species == 'dog':
#             print('woof-woof')
#
#
# animals = [Animal('cat'), Animal('dog')]
# animal_sound(animals)

# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
# Refactor the provided code, so you do not need to make any changes to it when you want to add
# new species to the animals' list


class AnimalSound:
    @staticmethod
    def animal_sound(sound):
        return sound


class Animal(AnimalSound):
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def get_species(self):
        return self.species


animals = [Animal('cat', "meow"), Animal('dog', "bark"), Animal('chicken', "cluck"),
           Animal("Horse", "lol"), Animal("Fly", "bzz")]


for animal in animals:
    print(animal.get_species())
    print(animal.animal_sound(animal.sound))