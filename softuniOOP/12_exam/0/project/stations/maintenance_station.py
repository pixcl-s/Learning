from project.stations.base_station import BaseStation


class MaintenanceStation(BaseStation):
    INITIAL_CAPACITY = 3

    def __init__(self, name: str):
        super().__init__(name, capacity=self.INITIAL_CAPACITY)

    def update_salaries(self, min_value: float):
        engineers = [x for x in self.astronauts if x.specialization == "EngineerAstronaut"]
        for y in engineers:
            if y.salary <= min_value:
                y.salary += 3000
