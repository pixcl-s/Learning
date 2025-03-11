from project.vehicle import Vehicle


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION: float = 3

    def drive(self, kilometers):
        Vehicle.drive(self, kilometers)
