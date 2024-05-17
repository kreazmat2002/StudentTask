import random
from cashier import Cashier
from department import Department
from childs import Bakery, Fruit
from customer import Customer


class Store:
    def __init__(self):
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def print_statistics(self):
        result = []
        total_inventory = sum(
            quantity
            for dept in self.departments
            for product, quantity in dept.products.items()
        )
        result.append(f"Всего товаров на складе: {total_inventory}\n")
        for dept in self.departments:
            result.append(f"Отдел: {dept.name} \n")
            total_revenue = sum(
                stat["sold_amount"] for stat in dept.sales_statistics.values()
            )
            result.append(f"Всего продаж: ₽{total_revenue:.2f}\n")
            for product, stats in dept.sales_statistics.items():
                result.append(
                    f"  {product.name}: Продано {stats['sold_quantity']} единиц(ы), Стоимость ₽{stats['sold_amount']:.2f}\n"
                )
            result.append("")
        return result

    def simulate_day(self):
        for department in self.departments:
            for _ in range(random.randint(3, 10)):
                customer = Customer(random.randint(200, 1000), random.randint(1, 5))
                customer.shop(department)
                customer.check_out(department)
            for cashier in department.cashiers:
                cashier.process_customers()
        return self.print_statistics()


store = Store()
fruit_dept = Department("Фрукты")
fruit_dept.add_product(Fruit("Яблоко", 50, 10), 100)
fruit_dept.add_product(Fruit("Банан", 30, 5), 120)
fruit_dept.add_product(Fruit("Апельсин", 80, 15), 105)

groceries_dept = Department("Бакалея")
groceries_dept.add_product(Bakery("Белый хлеб", 25, 3), 65)
groceries_dept.add_product(Bakery("Батон", 67, 3), 80)
fruit_dept.add_cashier(Cashier(fruit_dept))
groceries_dept.add_cashier(Cashier(groceries_dept))

store = Store()
store.add_department(fruit_dept)
store.add_department(groceries_dept)
# store.simulate_day()
