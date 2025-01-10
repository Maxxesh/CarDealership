class Employee:
    """
    Клас представляє співробітника автосалону.
    """

    def __init__(self, full_name, position, phone, email):
        self.full_name = full_name
        self.position = position
        self.phone = phone
        self.email = email

    def get_full_name(self):
        return self.full_name

    def update_contact(self, phone, email):
        """
        Оновлення контактної інформації співробітника.
        """
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Співробітник: {self.full_name}, Посада: {self.position}, Телефон: {self.phone}, Email: {self.email}"
