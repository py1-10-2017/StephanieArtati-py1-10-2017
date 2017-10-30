class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()

    def display_all(self):
        print("Price: ", self.price)
        print("Speed: ", self.speed, "mph")
        print("Fuel: ", self.fuel)
        print("Mileage: ", self.mileage, "mpg")
        print("Tax: ", self.tax)
        print("")


Car1 = Car(2000,35,"Full",15)
Car2 = Car(2000,5,"Not Full",105)
Car3 = Car(2000,15,"Kind of Full",95)
Car1 = Car(2000,25,"Full",25)
Car1 = Car(2000,45,"Empty",25)
Car1 = Car(20000000,35,"Empty",15)
