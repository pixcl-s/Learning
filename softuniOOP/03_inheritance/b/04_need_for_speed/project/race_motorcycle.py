from project.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION: float = 8

    def drive(self, kilometers):
        super().drive(kilometers)
