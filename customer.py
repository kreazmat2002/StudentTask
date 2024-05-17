import random

class Customer:
    def __init__(self, budget, patience_threshold):
        self.budget = budget
        self.cart = []
        self.patience_threshold = patience_threshold

    def shop(self, department):
        for product, available_quantity in department.products.items():
            if self.budget >= product.price:
                quantity = min(
                    random.randint(1, 5), available_quantity
                )
                if self.budget >= product.price * quantity:
                    self.cart.append((product, quantity))
                    department.products[product] -= quantity
                    self.budget -= product.price * quantity

    def check_out(self, department):
        cashier = department.find_least_busy_cashier()
        if len(cashier.queue) > self.patience_threshold:
            for product, quantity in self.cart:
                department.products[
                    product
                ] += quantity
        else:
            cashier.queue.append(self)

    def process_my_cart(self, cashier):
        for product, quantity in self.cart:
            cashier.department.record_sale(product, quantity)