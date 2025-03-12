# Create an abstract class called Vehicle that should have abstract methods drive and refuel. Create 2 vehicles
# that inherit the Vehicle class (a Car and a Truck) and simulate driving and refueling them. Car and Truck both
# receive fuel_quantity and fuel_consumption in liters per km upon initialization. They both can be driven a
# given distance: drive(distance) and refueled with a given amount of fuel: refuel(fuel). It is summer, so
# both vehicles use air conditioners, and their fuel consumption per km when driving is increased by 0.9 liters for the
# car and 1.6 liters for the truck. Also, the Truck has a tiny hole in its tank, and when it is refueled, it keeps only 95%
# of the given fuel. The car has no problems and adds all the given fuel to its tank. If a vehicle cannot travel the given
# distance, its fuel does not change.

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    SUMMER_TAX = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        required_fuel = distance * (self.fuel_consumption + self.SUMMER_TAX)
        if required_fuel <= self.fuel_quantity:
            self.fuel_quantity -= required_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    SUMMER_TAX = 1.6
    HOLE_FUEL_PERCENTAGE = 0.95

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        required_fuel = distance * (self.fuel_consumption + self.SUMMER_TAX)
        if required_fuel <= self.fuel_quantity:
            self.fuel_quantity -= required_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel * self.HOLE_FUEL_PERCENTAGE


# 100/100
# test
car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
# output
# 2.299999999999997
# 12.299999999999997
#
# 17.0
# 64.5