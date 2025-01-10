class Car:
    """
    Клас представляє автомобіль у базі автосалону.
    """

    def __init__(self, manufacturer, model, year, cost_price, sale_price):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.cost_price = cost_price
        self.sale_price = sale_price

    def get_car_info(self):
        """
        Повертає інформацію про автомобіль у вигляді рядка.
        """
        return f"{self.manufacturer} {self.model} ({self.year})"

    def update_sale_price(self, new_price):
        """
        Оновлення ціни продажу.
        """
        self.sale_price = new_price

    def __str__(self):
        return f"Авто: {self.get_car_info()}, Собівартість: {self.cost_price}, Ціна продажу: {self.sale_price}"
