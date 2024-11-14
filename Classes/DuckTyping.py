from abc import ABC, abstractmethod


# class UIControl(ABC):
#     @abstractmethod
#     def draw(self):
#         pass


class TextBox:
    def draw(self):
        print("Drawing TextBox")


class DropDownList:
    def draw(self):
        print("Drawing DropDownList")


class Button:
    def draw(self):
        print("Drawing Button")


def draw(controls):
    for control in controls:
        control.draw()

# Polymoriphic collection
# Even if we haven't inherit the UIControl class 
# as long as the controls in the draw function 
# is iterable and each objects hava a draw methods 
# polymorphism still happen here, because python is
#  dynamic language meaning we don't know the data 
# type of the variables or object until we run the program,
#  this is what we call it duck typing
# If it walks like a duck and quack likc a duck, it is a duck.
widgets = [TextBox(), DropDownList(), Button()]
draw(widgets)