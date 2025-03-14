from typing import Type

from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit


class Mouse(Mammal):
    EATS = [Vegetable, Fruit]
    WEIGHT_GAIN = 0.1

    @staticmethod
    def make_sound():
        return "Squeak"


class Dog(Mammal):
    EATS = [Meat]
    WEIGHT_GAIN = 0.4

    @staticmethod
    def make_sound():
        return "Woof!"


class Cat(Mammal):
    EATS = [Vegetable, Meat]
    WEIGHT_GAIN = 0.3

    @staticmethod
    def make_sound():
        return "Meow"


class Tiger(Mammal):
    EATS = [Meat]
    WEIGHT_GAIN = 1

    @staticmethod
    def make_sound():
        return "ROAR!!!"

