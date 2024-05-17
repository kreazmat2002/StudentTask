class Product:
    def __init__(self, name, price, expiration_days=None):
        self.name = name
        self.price = price
        self.expiration_days = expiration_days

    def update_price(self, seasonal_factor):
        self.price *= seasonal_factor

    def is_perishable(self):
        return self.expiration_days is not None