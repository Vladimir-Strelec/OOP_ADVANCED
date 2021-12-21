from project.product import Product


class Food(Product):
    def __init__(self, name):
        super(Food, self).__init__(name, 15)

