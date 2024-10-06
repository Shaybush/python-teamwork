class InventoryCalculations:
    def __init__(self, inventory):
        self.inventory = inventory

    def total_value(self):
        total = 0
        for product in self.inventory.products:
            total += product.price * product.quantity
        return total

    def total_items(self):
        total = 0
        for product in self.inventory.products:
            total += product.quantity
        return total