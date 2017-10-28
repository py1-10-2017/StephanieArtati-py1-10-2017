class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print("Price: ", self.price)
        print("Maximum speed: ", self.max_speed)
        print("Total miles: ", self.miles)

    def ride(self):
        print("Riding")
        self.miles += 10
        return self

    def reverse(self):
        print("Reversing")
        self.miles -= 5
        if (self.miles < 0):
            self.miles = 0
        return self

First_Bike = Bike(100, 25)
First_Bike.ride().ride().ride().reverse().displayInfo()
Second_Bike = Bike(100, 25)
Second_Bike.ride().ride().reverse().reverse().displayInfo()
Third_Bike = Bike(100, 25)
Third_Bike.reverse().reverse().reverse().displayInfo()
