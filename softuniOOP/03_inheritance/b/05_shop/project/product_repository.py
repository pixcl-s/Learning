from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for x in self.products:
            if x.name == product_name:
                return x

    def remove(self, product_name: str):
        to_remove = self.find(product_name)
        if to_remove:
            self.products.remove(to_remove)

    def __repr__(self):
        to_return = ""
        for x in self.products:
            to_return += f"{x.name}: {x.quantity}\n"

        return to_return.strip()
