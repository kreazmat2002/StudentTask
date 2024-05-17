class Cashier:
    def __init__(self, department):
        self.department = department
        self.queue = []

    def process_customers(self):
        while self.queue:
            customer = self.queue.pop(0)
            customer.process_my_cart(self)