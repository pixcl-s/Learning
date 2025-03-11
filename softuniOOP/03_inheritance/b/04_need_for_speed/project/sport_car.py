from project.car import Car


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION: float = 10

    def drive(self, kilometers):
        Car.drive(self, kilometers)
