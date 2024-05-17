from store import store

quantities = []
revenues_by_product = []
revenue_by_department = {}
TOTAL = 0
current_department = None


class StoreDataAnalyzer:
    def get_data(self):
        global quantities, revenues_by_product, revenue_by_department, TOTAL, current_department
        self._clear_data()
        result = store.simulate_day()
        print(*result)
        self._process_data(result)

    def _clear_data(self):
        global quantities, revenues_by_product, revenue_by_department, TOTAL
        quantities.clear()
        revenue_by_department.clear()
        revenues_by_product.clear()
        TOTAL = 0

    def _process_data(self, result):
        global current_department, TOTAL
        for line in result:
            line = line.strip()

            if "Отдел:" in line:
                current_department = line.replace("Отдел: ", "").strip()
            elif "Продано" in line and "Стоимость" in line:
                self._process_product_line(line)
            elif "Всего продаж:" in line:
                total_revenue = float(line.split("₽")[1])
                if current_department:
                    revenue_by_department[current_department] = total_revenue
            elif "Всего товаров на складе:" in line:
                TOTAL = float(line.split(" ")[4])

    def _process_product_line(self, line):
        global quantities, revenues_by_product
        product_info = line.split(":")
        product_name = product_info[0].strip()

        sold_revenue_info = product_info[1].split(",")
        quantity = int(sold_revenue_info[0].strip().split(" ")[1])
        revenue = float(sold_revenue_info[1].strip().split("₽")[1])

        quantities.append((product_name, quantity))
        revenues_by_product.append((product_name, revenue))


analyzer = StoreDataAnalyzer()
