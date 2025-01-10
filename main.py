from Employee import Employee
from Car import Car
from Sale import Sale
from CarDealership import CarDealership


def main():
    dealership = CarDealership()
    dealership.load_data_from_file("dealership_data.json")

    while True:
        print("\nМеню:")
        print("1. Додати співробітника")
        print("2. Додати автомобіль")
        print("3. Додати продаж")
        print("4. Показати всі продажі")
        print("5. Список співробітників")
        print("6. Список автомобілів")
        print("7. Сумарний прибуток")
        print("8. Топ-продавець")
        print("9. Найбільш продаваний автомобіль")
        print("10. Вийти")
        choice = input("Введіть номер опції: ")

        try:
            if choice == "1":
                name = input("Ім'я співробітника: ")
                position = input("Посада: ")
                phone = input("Телефон: ")
                email = input("Email: ")
                employee = Employee(name, position, phone, email)
                dealership.add_employee(employee)
            elif choice == "2":
                manufacturer = input("Виробник: ")
                model = input("Модель: ")
                year = int(input("Рік випуску: "))
                cost_price = float(input("Собівартість: "))
                sale_price = float(input("Ціна продажу: "))
                car = Car(manufacturer, model, year, cost_price, sale_price)
                dealership.add_car(car)
            elif choice == "3":
                sale_date = input("Дата продажу (ДД-ММ-РРРР): ")
                employee_name = input("Продавець (ім'я): ")
                car_info = input("Автомобіль (модель): ")
                actual_price = float(input("Ціна продажу: "))
                employee = next((e for e in dealership.employees if e.full_name == employee_name), None)
                car = next((c for c in dealership.cars if f"{c.manufacturer} {c.model}" == car_info), None)
                if employee and car:
                    sale = Sale(employee, car, sale_date, actual_price)
                    dealership.add_sale(sale)
                else:
                    print("Помилка: Невірні дані про співробітника або автомобіль.")
            elif choice == "4":
                dealership.generate_reports()
            elif choice == "5":
                print(dealership.get_employee_list())
            elif choice == "6":
                print(dealership.get_car_list())
            elif choice == "7":
                print(f"Сумарний прибуток: {dealership.get_total_profit()}")
            elif choice == "8":
                print(f"Топ-продавець: {dealership.get_best_seller()}")
            elif choice == "9":
                print(f"Найбільш продаваний автомобіль: {dealership.get_best_selling_car()}")
            elif choice == "10":
                dealership.save_data_to_file("dealership_data.json")
                break
            else:
                print("Невірна опція.")
        except Exception as e:
            print(f"Помилка: {e}")


if __name__ == "__main__":
    main()
