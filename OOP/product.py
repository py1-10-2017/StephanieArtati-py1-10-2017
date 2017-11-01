class Product(object):
    def __init__(self, price, item_name, weight, brand, status="for sale"):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status
        self.display_all()

    def display_all(self):
        print("Price: ", self.price)
        print("Item name ", self.item_name)
        print("Weight: ", self.weight)
        print("Brand: ", self.brand)
        print("Status: ", self.status)
        print("")

    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self, tax):
        return self.price + tax

    def return_product(self, condition = "like new", reason = None):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        else:
            if condition == "like new":
                self.status = "for sale"
            elif condition == "used":
                self.status = "used"
                self.price *= 0.8
        return self

if __name__ == "__main__":
    Product1 = Product(200,"Toddler shoes",1, "Carter's","for sale")
    Product1.sell()
    Product1.display_all()
    Product1.return_product("used")
    Product1.display_all()
