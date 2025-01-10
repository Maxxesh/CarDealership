import unittest
from CarDealership import CarDealership
from Employee import Employee
from Car import Car
from Sale import Sale


class TestCarDealership(unittest.TestCase):
    def setUp(self):
        self.dealership = CarDealership()
        self.employee = Employee("Іван Іванов", "Менеджер", "123456789", "ivanov@gmail.com")
        self.car = Car("Toyota", "Camry", 2020, 20000, 25000)
        self.dealership.add_employee(self.employee)
        self.dealership.add_car(self.car)

    def test_add_employee(self):
        self.assertEqual(len(self.dealership.employees), 1)

    def test_add_car(self):
        self.assertEqual(len(self.dealership.cars), 1)

    def test_add_sale(self):
        sale = Sale(self.employee, self.car, "2023-01-01", 24000)
        self.dealership.add_sale(sale)
        self.assertEqual(len(self.dealership.sales), 1)


if __name__ == "__main__":
    unittest.main()
