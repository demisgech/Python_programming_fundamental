class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other):
        return self.x != other.x and self.y != other.y

p1 = Point(1,2)
p2 = Point(1,2)
print(p1 == p2)
print(p1 != p2)
# id(object) => returns the memory location of the object
print(id(p1))
print(id(p2))

# Instead of using the above techniques 
# we can use a more cleaner way to achieve the same behaviour

from collections import namedtuple
NewPoint = namedtuple('NewPoint',['x','y'])
point1 = NewPoint(x=1,y=3)
point2 = NewPoint(x=1,y=3)
print(point1 == point2) # True