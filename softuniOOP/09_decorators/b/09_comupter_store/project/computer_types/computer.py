import math
from abc import ABC, abstractmethod
from typing import Optional


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor: Optional[str] = None
        self.ram: Optional[int] = None
        self.price: int = 0

    def configure_computer(self, processor: str, ram: int):
        if processor in self.AVAILABLE_PROCESSOR:
            idk = math.log2(ram)
            if ram <= self.MAX_RAM and idk.is_integer():
                self.processor = processor
                self.ram = ram
                self.price = int(self.AVAILABLE_PROCESSOR[processor] + idk*100)
                return f"Created {self.__repr__()} for {self.price}$."
            raise ValueError(f"{ram}GB RAM is not compatible with {self.__str__()} {self.manufacturer} {self.model}!")
        raise ValueError(f"{processor} is not compatible with {self.__str__()} {self.manufacturer} {self.model}!")

    def __repr__(self):
        return f"{self.__manufacturer} {self.__model} with {self.processor} and {self.ram}GB RAM"

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if not value.strip():
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    @abstractmethod
    def __str__(self):
        pass
