class Point:
    # Class attributes
    default_color = "red" # class level attribute shared over all instances of a class

    # constructor
    def __init__(self, x, y):
        # Instances attributes
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point({self.x},{self.y})")

Point.default_color = "Yellow"
point = Point(1,2)
print(type(point))
 
# is_instance =  isinstance(point,Point)
# print(is_instance)
point.draw()

another = Point(12,34)
another.draw()

print(point.default_color)
print(Point.default_color)