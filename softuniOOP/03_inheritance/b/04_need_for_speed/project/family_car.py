from project.car import Car


class FamilyCar(Car):
    def drive(self, kilometers):
        Car.drive(self, kilometers)
