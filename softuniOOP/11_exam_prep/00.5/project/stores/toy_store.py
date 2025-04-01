from project.stores.base_store import BaseStore, amount_of_types_products


class ToyStore(BaseStore):
    def __init__(self, name: str, location: str):
        super().__init__(name, location, capacity=100)

    @property
    def store_type(self):
        return __class__.__name__

    def store_stats(self):
        the_products = amount_of_types_products(self.products)

        to_return = f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}\n" \
                    f"{self.get_estimated_profit()}\n" \
                    f"**Toys for sale:\n" \

        for x, y in the_products.items():
            prices = sum(y)
            to_return += f"{x.model}: {y}pcs, average price: {prices / len(y):.2f}\n"

        return to_return
