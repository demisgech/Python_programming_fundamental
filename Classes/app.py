from abc import ABC,abstractmethod

class Shape(ABC):

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
     def draw(self):
        print('Drawing a circle')

circle = Circle()
circle.draw()

class Person:
    def __int__(self,name):
        self.name = name
    def say_hi(self, name):
        return f'Hello {name}'

person = Person()
message = person.say_hi("Demis")
print(message)