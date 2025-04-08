from project.astronauts.base_astronaut import BaseAstronaut
from project.astronauts.engineer_astronaut import EngineerAstronaut
from project.astronauts.scientist_astronaut import ScientistAstronaut
from project.stations.base_station import BaseStation
from project.stations.maintenance_station import MaintenanceStation
from project.stations.research_station import ResearchStation


class SpaceAgency:
    def __init__(self):
        self.astronauts: list[BaseAstronaut] = []
        self.stations: list[BaseStation] = []

    def add_astronaut(self, astronaut_type: str, astronaut_id_number: str, astronaut_salary: float):
        VALID_ASTRONAUT_TYPES = {"EngineerAstronaut": EngineerAstronaut, "ScientistAstronaut": ScientistAstronaut}

        if astronaut_type not in VALID_ASTRONAUT_TYPES:
            raise ValueError("Invalid astronaut type!")

        existing_astronaut = self.exist(self.astronauts, astronaut_id_number)
        if existing_astronaut:
            raise ValueError(f"{astronaut_id_number} has been already added!")

        self.astronauts.append(VALID_ASTRONAUT_TYPES[astronaut_type](astronaut_id_number, astronaut_salary))
        return f"{astronaut_id_number} is successfully hired as {astronaut_type}."

    def add_station(self, station_type: str, station_name: str):
        VALID_STATION_TYPES = {"ResearchStation": ResearchStation, "MaintenanceStation": MaintenanceStation}

        if station_type not in VALID_STATION_TYPES:
            raise ValueError("Invalid station type!")

        existing_station = self.exist(self.stations, station_name)
        if existing_station:
            raise ValueError(f"{station_name} has been already added!")

        self.stations.append(VALID_STATION_TYPES[station_type](station_name))
        return f"{station_name} is successfully added as a {station_type}."

    def assign_astronaut(self, station_name: str, astronaut_type: str):
        existing_station = self.exist(self.stations, station_name)
        existing_astronaut = next((x for x in self.astronauts if x.specialization == astronaut_type), None)

        if existing_station:
            if existing_astronaut:
                if existing_station.capacity:
                    self.astronauts.remove(existing_astronaut)
                    existing_station.astronauts.append(existing_astronaut)
                    existing_station.capacity -= 1
                    return f"{existing_astronaut.id_number} was assigned to {station_name}."
                return "This station has no available capacity."
            raise ValueError("No available astronauts of the type!")
        raise ValueError(f"Station {station_name} does not exist!")

    @staticmethod
    def train_astronauts(station: BaseStation, sessions_number: int):
        for x in station.astronauts:
            for _ in range(sessions_number):
                x.train()
        return f"{station.name} astronauts have {sum(x.stamina for x in station.astronauts)} total stamina after {sessions_number} training session/s."

    def retire_astronaut(self, station: BaseStation, astronaut_id_number: str):
        existing_astronaut = self.exist(station.astronauts, astronaut_id_number)
        if existing_astronaut and existing_astronaut.stamina < existing_astronaut.MAX_STAMINA:
            station.astronauts.remove(existing_astronaut)
            station.capacity += 1
            return f"Retired astronaut {existing_astronaut.id_number}."
        return "The retirement process was canceled."

    def agency_update(self, min_value: float):
        [x.update_salaries(min_value) for x in self.stations]

        to_return = f"*Space Agency Up-to-Date Report*\n" \
                    f"Total number of available astronauts: {len(self.astronauts)}\n" \
                    f"**Stations count: {len(self.stations)}; Total available capacity: {sum(x.capacity for x in self.stations)}**\n"

        to_return += '\n'.join([x.status() for x in sorted(self.stations, key=lambda station: (-len(station.astronauts), station.name))])

        return to_return

    @staticmethod
    def exist(lists, parameter):
        if lists:
            if isinstance(lists[0], BaseStation):
                return next((x for x in lists if x.name == parameter), None)
            elif isinstance(lists[0], BaseAstronaut):
                return next((x for x in lists if x.id_number == parameter), None)
