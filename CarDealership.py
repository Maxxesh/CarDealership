import json

from Car import Car
from Employee import Employee
from Sale import Sale


class CarDealership:
    """
    Основний клас, що представляє автосалон.
    """

    def __init__(self):
        self.employees = []
        self.cars = []
        self.sales = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, email):
        """
        Видалення співробітника за email.
        """
        self.employees = [e for e in self.employees if e.email != email]

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, manufacturer, model):
        """
        Видалення авто за виробником та моделлю.
        """
        self.cars = [c for c in self.cars if not (c.manufacturer == manufacturer and c.model == model)]

    def get_sales(self):
        """Отримати список усіх продажів."""
        return self.sales

    def add_sale(self, sale):
        self.sales.append(sale)

    def remove_sale(self, sale_date):
        """
        Видалення продажу за датою.
        """
        self.sales = [s for s in self.sales if s.sale_date != sale_date]

    def save_data_to_file(self, filename):
        """
        Збереження даних автосалону у файл.
        """
        data = {
            "employees": [e.__dict__ for e in self.employees],
            "cars": [c.__dict__ for c in self.cars],
            "sales": [
                {"employee": s.employee.full_name, "car": s.car.get_car_info(),
                 "sale_date": s.sale_date, "actual_price": s.actual_price}
                for s in self.sales
            ]
        }
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_data_from_file(self, filename):
        """
        Завантаження даних автосалону з файлу.
        """
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        self.employees = [Employee(**e) for e in data["employees"]]
        self.cars = [Car(**c) for c in data["cars"]]
        # Відновлення продажів потребує складнішої логіки, залежно від Employee та Car.
        self.sales = Sale.load_data_from_file(filename, self.employees, self.cars)

    def generate_reports(self):
        """
        Генерація базових звітів.
        """
        print("Список співробітників:")
        for employee in self.employees:
            print(employee)

        print("\nСписок автомобілів:")
        for car in self.cars:
            print(car)

        print("\nСписок продажів:")
        for sale in self.sales:
            print(sale)

    def calculate_total_profit(self, start_date, end_date):
        """
        Обчислення загального прибутку за вказаний період.
        """
        return sum(sale.calculate_profit() for sale in self.sales if start_date <= sale.sale_date <= end_date)

    def get_employee_list(self):
        """Отримати список усіх співробітників."""
        return [str(employee) for employee in self.employees]

    def get_car_list(self):
        """Отримати список усіх автомобілів."""
        return [str(car) for car in self.cars]

    def get_total_profit(self):
        """Розрахувати сумарний прибуток."""
        total_profit = sum(sale.actual_price - sale.car.cost_price for sale in self.sales)
        return total_profit

    def get_best_seller(self):
        """Знайти найуспішнішого продавця за всі продажі."""
        if not self.sales:
            return None
        sales_count = {}
        for sale in self.sales:
            sales_count[sale.employee.full_name] = sales_count.get(sale.employee.full_name, 0) + 1
        best_seller = max(sales_count, key=sales_count.get)
        return best_seller

    def get_best_selling_car(self):
        """Знайти найбільш продаваний автомобіль."""
        if not self.sales:
            return None
        car_count = {}
        for sale in self.sales:
            car_model = f"{sale.car.manufacturer} {sale.car.model}"
            car_count[car_model] = car_count.get(car_model, 0) + 1
        best_selling_car = max(car_count, key=car_count.get)
        return best_selling_car
