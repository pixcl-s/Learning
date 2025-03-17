# You are provided with code containing class Rectangle and class AreaCalculator.
# Refactor the code using the Open/Closed Principle so that the code is open for extension (adding more shapes)
# but closed for modification.
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    def __init__(self, width, height=0):
        self.width = width
        self.height = height

    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def calculate_area(self):
        return self.width * self.height


class Triangle(Shape):
    def calculate_area(self):
        return 1/2 * self.width * self.height


class Circle(Shape):
    def calculate_area(self):
        return pi * self.width**2


class AreaCalculator:
    def __init__(self, shape):
        self.shapes = shape

    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        assert isinstance(value, list), "`shapes` should be of type `list`."
        self.__shapes = value

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calculate_area()

        return total


# test
shapes = [Rectangle(1, 6), Triangle(2, 3), Circle(6)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)
# output
# The total area is: 9.0


# old

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
# class AreaCalculator:
#     def __init__(self, shapes):
#
#         assert isinstance(shapes, list), "`shapes` should be of type `list`."
#         self.shapes = shapes
#
#     @property
#     def total_area(self):
#         total = 0
#         for shape in self.shapes:
#             total += shape.width * shape.height
#
#         return total
# test
# shapes = [Rectangle(2, 3), Rectangle(1, 6)]
# calculator = AreaCalculator(shapes)
# print("The total area is: ", calculator.total_area)
# output
# The total area is: 12
