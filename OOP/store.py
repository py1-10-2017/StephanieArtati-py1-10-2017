from product import Product

class Store(object):
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner
        self.display_all()

    def display_all(self):
        print("Products: ", self.products)
        print("Location: ", self.location)
        print("Owner: ", self.owner)
        print("")

    def add_product(self, product):
        self.products.append(product)
        return self

    def remove_product(self, product_name):
        for i in range(0,len(self.products)):
            if self.products[i].item_name == product_name:
                del self.products[i]
                break
        return self

    def inventory(self):
        print("Current inventory: ")
        for product in self.products:
            product.display_all()

if __name__ == "__main__":
    Product1 = Product(20,"Toddler shoes",1, "Carter's","for sale")
    Product2 = Product(10,"Toddler socks",1, "Carter's","for sale")
    Product1.sell()
    Product2.sell()
    Product2.return_product("used")

    Store1 = Store([Product1, Product2], "Redmond", "Stephanie Artati")
    Product3 = Product(25,"Toddler sleepsack",2, "Gymboree","for sale")
    Store1.add_product(Product3)
    Store1.inventory()

    Store1.remove_product("Toddler socks")
    Store1.inventory()
