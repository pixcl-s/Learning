from typing import List

from project.clients.base_client import BaseClient
from project.clients.business_client import BusinessClient
from project.clients.regular_client import RegularClient
from project.plants.base_plant import BasePlant
from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant


class FlowerShopManager:
    VALID_PLANT_TYPES = {"Flower": Flower, LeafPlant.__name__: LeafPlant}
    VALID_CLIENT_TYPES = {BusinessClient.__name__: BusinessClient, RegularClient.__name__: RegularClient}

    def __init__(self):
        self.income: float = 0
        self.plants: List[BasePlant] = []
        self.clients: List[BaseClient] = []

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int, plant_extra_data: str):
        if plant_type not in self.VALID_PLANT_TYPES:
            raise ValueError("Unknown plant type!")

        the_plant = self.VALID_PLANT_TYPES[plant_type](plant_name, plant_price, plant_water_needed, plant_extra_data)

        self.plants.append(the_plant)

        return f"{plant_name} is added to the shop as {plant_type}."

    def add_client(self, client_type: str, client_name: str, client_phone_number: str):
        if client_type not in self.VALID_CLIENT_TYPES:
            raise ValueError("Unknown client type!")

        already_registered = self.client_search(client_phone_number)

        if already_registered:
            raise ValueError("This phone number has been used!")

        the_client = self.VALID_CLIENT_TYPES[client_type](client_name, client_phone_number)

        self.clients.append(the_client)

        return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        the_client = self.client_search(client_phone_number)
        if not the_client:
            raise ValueError("Client not found!")

        the_plants = [x for x in self.plants if x.name == plant_name]
        if not the_plants:
            raise ValueError("Plants not found!")

        if len(the_plants) >= plant_quantity:
            order_income = 0

            for x in range(plant_quantity):
                the_plant = the_plants[x]
                self.plants.remove(the_plant)
                order_income += the_plant.price

            order_income -= order_income*the_client.discount
            self.income += order_income
            the_client.update_total_orders()
            the_client.update_discount()

            return f"{plant_quantity}pcs. of {plant_name} plant sold for {order_income:.2f}"

        return "Not enough plant quantity."

    def remove_plant(self, plant_name: str):
        the_plant = next((x for x in self.plants if x.name == plant_name), None)

        if the_plant:
            self.plants.remove(the_plant)
            return f"Removed {the_plant.plant_details()}"
        return "No such plant name."

    def remove_clients(self):
        clients_without_orders = [x for x in self.clients if x.total_orders == 0]
        for x in clients_without_orders:
            self.clients.remove(x)
        # self.clients = list(set(self.clients) - set(clients_without_orders))
        return f"{len(clients_without_orders)} client/s removed."

    def shop_report(self):
        to_return = f"~Flower Shop Report~\n" \
                    f"Income: {self.income:.2f}\n" \
                    f"Count of orders: {sum(x.total_orders for x in self.clients)}\n" \
                    f"~~Unsold plants: {len(self.plants)}~~\n"

        each_plant = self.each_plant()
        to_return += "".join(f"{x}: {y}\n" for x, y in each_plant.items())
        to_return += f"~~Clients number: {len(self.clients)}~~\n"
        to_return += "\n".join(x.client_details() for x in sorted(self.clients, key=lambda client: (-client.total_orders, client.phone_number)))

        return to_return

    def client_search(self, number):
        return next((x for x in self.clients if x.phone_number == number), None)

    def each_plant(self):
        each = {}
        for x in self.plants:
            if x.name not in each:
                each[x.name] = 0

            each[x.name] += 1

        return dict(sorted(each.items(), key=lambda y: (-y[1], y[0])))

