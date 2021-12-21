from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for obj in self.products:
            if obj.name == product_name:
                return obj

    def remove(self, product_name):
        for obj in self.products:
            if obj.name == product_name:
                self.products.remove(obj)

    def __repr__(self):
        return '\n'.join([f"{obj.name}: {obj.quantity}" for obj in self.products])