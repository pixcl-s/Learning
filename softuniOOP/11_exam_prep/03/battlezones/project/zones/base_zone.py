from abc import ABC, abstractmethod

from project.battleships.base_battleship import BaseBattleship


class BaseZone(ABC):
    def __init__(self, code: str, volume: int):
        self.code = code
        self.volume = volume
        self.ships: list[BaseBattleship] = []

    def get_ships(self):
        the_ships = sorted(self.ships, key=lambda ship: (-ship.hit_strength, ship.name))
        return the_ships

    @abstractmethod
    def zone_info(self):
        pass

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value):
        if not value.isdigit():
            raise ValueError("Zone code must contain digits only!")
        self.__code = value
