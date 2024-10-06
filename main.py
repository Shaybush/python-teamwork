from inventory import Inventory
from product import Product
from inventory_calculations import InventoryCalculations

bamba = Product("bamba", 88, 100)
bisli = Product("bisli", 56, 200)
my_Products = Inventory()
my_Products.add_product(bisli)
my_Products.add_product(bamba)
my_Products.remove_product(bamba)
for product in my_Products.products:
    print(product)
total = InventoryCalculations(my_Products)
total_value = total.total_value()
print(total_value)
total_items = total.total_items()
print(total_items)

