from typing import Type
from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):
    EATS = [Meat]
    WEIGHT_GAIN = 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):
    EATS = [Vegetable, Fruit, Meat, Seed]
    WEIGHT_GAIN = 0.35

    @staticmethod
    def make_sound():
        return "Cluck"
