from typing import List, Type

from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore, amount_of_types_products
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:
    TOYS_TO_PRODUCE = {Chair.__name__: Chair, HobbyHorse.__name__: HobbyHorse}
    STORES = {FurnitureStore.__name__: FurnitureStore, ToyStore.__name__: ToyStore}

    def __init__(self, name: str):
        self.name = name
        self.income: float = 0.0
        self.products: List[Type[BaseProduct]] = []
        self.stores: List[Type[BaseStore]] = []

    def produce_item(self, product_type: str, model: str, price: float):
        if product_type in self.TOYS_TO_PRODUCE:
            product = self.TOYS_TO_PRODUCE[product_type](model, price)
            self.products.append(product)
            return f"A product of sub-type {product.sub_type} was produced."
        raise Exception("Invalid product type!")

    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type in self.STORES:
            store = self.STORES[store_type](name, location)
            self.stores.append(store)
            return f"A new {store.store_type} was successfully registered."
        raise Exception(f"{store_type} is an invalid type of store!")

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if store.capacity >= len(products):
            correct_products = [x for x in products if x.sub_type in store.store_type]
            if correct_products:
                store.products.extend(correct_products)
                self.products = list(set(self.products) - set(correct_products))
                store.capacity -= len(correct_products)
                self.income += sum([x.price for x in correct_products])
                return f"Store {store.name} successfully purchased {len(correct_products)} items."
            return "Products do not match in type. Nothing sold."
        return f"Store {store.name} has no capacity for this purchase."

    def unregister_store(self, store_name: str):
        the_store = next((x for x in self.stores if x.name == store_name), None)
        if the_store:
            if not the_store.products:
                self.stores.remove(the_store)
                return f"Successfully unregistered store {the_store.name}, location: {the_store.location}."
            return "The store is still having products in stock! Unregistering is inadvisable."
        raise Exception("No such store!")

    def discount_products(self, product_model: str):
        discounted = 0
        for x in self.products:
            if x.model == product_model:
                x.discount()
                discounted += 1
        else:
            return f"Discount applied to {discounted} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        the_store = next((x for x in self.stores if x.name == store_name), None)
        if the_store:
            return the_store.store_stats()
        return "There is no store registered under this name!"

    def statistics(self):
        the_products = amount_of_types_products(self.products)

        to_return = f"Factory: {self.name}\n" \
                    f"Income: {self.income:.2f}\n" \
                    f"***Products Statistics***\n" \
                    f"Unsold Products: {len(self.products)}. Total net price: {sum(x.price for x in self.products):.2f}\n"

        for x, y in the_products.items():
            to_return += f"{x}: {len(y)}\n"

        to_return += f"***Partner Stores: {len(self.stores)}***\n"

        to_return += "\n".join(x.name for x in self.stores)

        return to_return


