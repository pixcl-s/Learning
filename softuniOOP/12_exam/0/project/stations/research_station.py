from project.stations.base_station import BaseStation


class ResearchStation(BaseStation):
    INITIAL_CAPACITY = 5

    def __init__(self, name):
        super().__init__(name, self.INITIAL_CAPACITY)

    def update_salaries(self, min_value: float):
        scientists = [x for x in self.astronauts if x.specialization == "ScientistAstronaut"]
        for y in scientists:
            if y.salary <= min_value:
                y.salary += 5000
