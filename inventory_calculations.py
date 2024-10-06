class InventoryCalculations:
    def __init__(self, inventory):
        self.inventory = inventory

    def total_value(self):
        total = 0
        for product in self.inventory.products:
            total += product.price * product.quantity
        return total