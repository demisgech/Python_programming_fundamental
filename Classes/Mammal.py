class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1


    def eat(self):
        print("Eating...")
    
# Animal: Parent, Super, Base
# Mammal: Child, Sub, Drived
class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal Constructor")
        self.weight = 2

    def walk(self):
        print("Walking....")


class Fish(Animal):
    def swim(self):
        print("Swimming....")

class Bird(Animal):
    def fly(self):
        print("fly")

# Multilevel Inheritance
# Inheritance abuse cause checken can't fly
class Chicken(Bird): # 
    pass

mammal = Mammal()
mammal.eat()
mammal.walk()
# print(isinstance(mammal, Mammal))
# print(isinstance(mammal, Animal))
# print(issubclass(Mammal, Mammal)) # Python interpreter said me a class is a sub class for itself
# print(issubclass(Mammal, Animal))
# print(issubclass(Mammal, object))
print(mammal.weight)
print(mammal.age)

fish = Fish()
fish.eat()
fish.swim()
print(issubclass(Fish, Mammal))