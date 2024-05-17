class Department:
    def __init__(self, name):
        self.name = name
        self.products = {}
        self.cashiers = []
        self.sales_statistics = {}

    def add_product(self, product, quantity):
        self.products[product] = quantity
        self.sales_statistics[product] = {"sold_quantity": 0, "sold_amount": 0}

    def record_sale(self, product, quantity):
        self.sales_statistics[product]["sold_quantity"] += quantity
        self.sales_statistics[product]["sold_amount"] += quantity * product.price

    def add_cashier(self, cashier):
        self.cashiers.append(cashier)
        cashier.department = self

    def find_least_busy_cashier(self):
        return min(self.cashiers, key=lambda c: len(c.queue))