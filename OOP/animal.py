
class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def display_health(self):
        print("Health Score: ", self.health)
        print("")

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

class Dog(Animal):
    def __init__(self, name, health=150):
        super(Dog, self).__init__(name, health)

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name, health=170):
        super(Dragon, self).__init__(name, health)

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        super(Dragon, self).display_health()
        print("I am a Dragon")

MyAnimal = Animal("Animale", 100)
MyAnimal.walk().walk().walk().run().run().display_health()

MyDog = Dog("Dawg")
MyDog.walk().walk().walk().run().run().pet().display_health()

MyDragon = Dragon("Drag")
MyDragon.display_health()
