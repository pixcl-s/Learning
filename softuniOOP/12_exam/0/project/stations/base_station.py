from abc import ABC, abstractmethod
import re

from project.astronauts.base_astronaut import BaseAstronaut


class BaseStation(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.astronauts: list[BaseAstronaut] = []

    def calculate_total_salaries(self):
        total_salaries = sum(x.salary for x in self.astronauts)
        return f"{total_salaries:.2f}"

    def status(self):
        to_return = f"Station name: {self.name};"

        to_return += f" Astronauts: {' #'.join(x.id_number for x in sorted(self.astronauts, key=lambda astronaut: astronaut.id_number))};" if self.astronauts else f" Astronauts: N/A;"

        to_return += f" Total salaries: {self.calculate_total_salaries()}"

        return to_return

    @abstractmethod
    def update_salaries(self, min_value: float):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        # x = re.search(r"[a-zA-Z-\d]*", value)
        # if x:
        #     self.__name = value
        # else:
        #     raise ValueError("Station names can contain only letters, numbers, and hyphens!")

        x = re.findall(r"[a-zA-Z-\d]+", value)

        if len(x) > 1 or len(x[0]) != len(value):
            raise ValueError("Station names can contain only letters, numbers, and hyphens!")

        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("A station cannot have a negative capacity!")
        self.__capacity = value
