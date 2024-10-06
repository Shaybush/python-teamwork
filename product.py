class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount):
        self.quantity += amount

    def get_info(self):
        return f" name = {self.name}, price = {self.price}, quantity = {self.quantity}"

    def __str__(self):
        return f" name = {self.name}, price = {self.price}, quantity = {self.quantity}"
