import json


class Sale:
    """
    Клас представляє інформацію про продаж.
    """

    def __init__(self, employee, car, sale_date, actual_price):
        self.employee = employee  # Сотрудник, который осуществил продажу
        self.car = car  # Автомобиль, который был продан
        self.sale_date = sale_date  # Дата продажи
        self.actual_price = actual_price  # Реальная цена продажи

    def get_sale_info(self):
        """
        Повертає детальну інформацію про продаж.
        """
        return (f"Дата продажу: {self.sale_date}, Авто: {self.car.get_car_info()}, "
                f"Продавець: {self.employee.get_full_name()}, Ціна: {self.actual_price}")

    def calculate_profit(self):
        """
        Обчислює прибуток від продажу.
        """
        return self.actual_price - self.car.cost_price

    def __str__(self):
        return self.get_sale_info()

    @staticmethod
    def load_data_from_file(filename, employees, cars):
        """
        Завантаження даних автосалону з файлу та створення списку продажів.
        Параметри:
        - employees: список співробітників
        - cars: список автомобілів
        """
        sales = []
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Відновлення продажів
        for s in data["sales"]:
            # Пошук відповідного об'єкта Employee та Car
            employee = next((e for e in employees if e.full_name == s["employee"]), None)
            car = next((c for c in cars if f"{c.manufacturer} {c.model} ({c.year})" == s["car"]), None)

            if employee and car:
                sale = Sale(employee, car, s["sale_date"], s["actual_price"])
                sales.append(sale)
        return sales
