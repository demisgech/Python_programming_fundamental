from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("Drawing TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("Drawing DropDownList")


class Button(UIControl):
    def draw(self):
        print("Drawing Button")


def draw(controls):
    for control in controls:
        control.draw()

# Polymoriphic collection
widgets = [TextBox(), DropDownList(), Button()]
draw(widgets)