from product import Product

class Fruit(Product):
    def __init__(self, name, price, expiration_days):
        super().__init__(name, price, expiration_days)


class Bakery(Product):
    def __init__(self, name, price, expiration_days):
        super().__init__(name, price, expiration_days)