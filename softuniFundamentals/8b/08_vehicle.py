
# Create a class Vehicle.
# The __init__ method should receive a type, a model, and a price.
# You should also set an owner to None.
# The class should have the following methods:
# buy(money: int, owner: str)
# If the person has enough money and the vehicle has no owner, returns:
# "Successfully bought a {type}. Change: {change}" and sets the owner to the given one
# If the money is not enough, return: "Sorry, not enough money"
# If the car already has an owner, return: "Car already sold"
# sell()
# If the car has an owner, set it to None again.
# Otherwise, return: "Vehicle has no owner"
# __repr__()
# If the vehicle has an owner, returns: "{model} {type} is owned by: {owner}".
# Otherwise, return: "{model} {type} is on sale: {price}"

class Vehicle:
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money, owner):
        if self.price <= money and self.owner is None:
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {money - self.price:.2f}"
        elif self.price > money:
            return "Sorry, not enough money"
        elif self.owner is not None:
            return "Car already sold"

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        return f"{self.model} {self.type} is on sale: {self.price}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)