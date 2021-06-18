class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.purchases = [] #tracks customer's purchases

    def purchase(self, inventory, product):
        inventory_dict = inventory.inventory #inventory dictionary usingcInventory() object
        if product in inventory_dict:
            if inventory_dict[product] > 0:
                self.purchases.append(product)
                inventory_dict[product] -= 1
            else:
                print("Product is out of stock!")
        else:
            print("Product isn't available!")
    
    def print_purchases(self):
        print(self.name + " has purchased:")
        for item in self.purchases:
            print(item.name)


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Inventory:
    def __init__(self):
        self.inventory = {} #keeps stock of items in the store
        # {'product_object', quantity}

    def add_product(self, product, quantity):
        if product not in self.inventory: #adding to the stock
            self.inventory[product] = quantity
        else: #increasing the stock if product is already present
            self.inventory[product] += quantity

    def print_inventory(self):
        for key, value in self.inventory.items():
            print(key.name + ':' + str(value))
        print()

#instantiating the objects
customer = Customer('Joe', 'joe@gmail.com')
apple_watch = Product('Apple Watch', 299)
mac = Product('Mac', 1999)

#adding items to inventory
inventory = Inventory()
inventory.add_product(apple_watch, 100)
inventory.add_product(mac, 500)
inventory.print_inventory()

#making the purchase
customer.purchase(inventory, apple_watch)
customer.purchase(inventory, mac)

#displaying the stock and purchase after checking out
inventory.print_inventory()
customer.print_purchases()