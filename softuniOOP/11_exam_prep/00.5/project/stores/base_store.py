from abc import ABC, abstractmethod
from typing import List, Type

from project.products.base_product import BaseProduct


def amount_of_types_products(products):
    the_products = {}
    for x in products:
        if x.model not in the_products:
            the_products[x.model] = []
        the_products[x.model].append(x.price)
    return the_products


class BaseStore(ABC):
    def __init__(self, name: str, location: str, capacity: int):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products: List[Type[BaseProduct]] = []

    def get_estimated_profit(self):
        sum_of_products = sum([x.price for x in self.products])
        estimated_profit = sum_of_products * 0.1
        return f"Estimated future profit for {len(self.products)} products is {estimated_profit:.2f}"

    @property
    @abstractmethod
    def store_type(self):
        pass

    @abstractmethod
    def store_stats(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Store name cannot be empty!")
        self.__name = value

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        if len(value) != 3 and any(x for x in value if x in [" ", "\t", "\v", "\n", "\r", "\f"]):
            raise ValueError("Store location must be 3 chars long!")
        self.__location = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Store capacity must be a positive number or 0!")
        self.__capacity = value

