from typing import List
from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity() -> int:
        return 15

    @staticmethod
    def customer_capacity() -> int:
        return 10

    def add_customer(self, customer: Customer) -> None:
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        the_dvd = next((x for x in self.dvds if x.id == dvd_id), None)
        the_customer = next((x for x in self.customers if x.id == customer_id), None)

        if the_dvd.is_rented:
            if the_dvd in the_customer.rented_dvds:
                return f"{the_customer.name} has already rented {the_dvd.name}"
            return f"DVD is already rented"

        if the_customer.age < the_dvd.age_restriction:
            return f"{the_customer.name} should be at least {the_dvd.age_restriction} to rent this movie"

        the_customer.rented_dvds.append(the_dvd)
        the_dvd.is_rented = True
        return f"{the_customer.name} has successfully rented {the_dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int) -> str:
        the_dvd = next(x for x in self.dvds if x.id == dvd_id)
        the_customer = next(x for x in self.customers if x.id == customer_id)

        if the_dvd in the_customer.rented_dvds:
            the_dvd.is_rented = False
            the_customer.rented_dvds.remove(the_dvd)
            return f"{the_customer.name} has successfully returned {the_dvd.name}"
        return f"{the_customer.name} does not have that DVD"

    def __repr__(self):
        to_return = ""
        for x in self.customers:
            to_return += f"{x}\n"
        for y in self.dvds:
            to_return += f"{y}\n"
        return to_return
