import math

class Line:
    
    object_count:int = 0
    def __init__(self, x:int, y:int)->None:
        self.x = x
        self.y = y
        Line.object_count += 1
    
    @classmethod
    def zero(cls):
      
       return Line(0,0)
    #    return cls(0, 0)

    def draw_line(self):
        print(f'Drawing line at point({self.x}, {self.y})')
    @classmethod
    def get_perimeter(cls, x, y)->int:
        return x + y
    


line = Line(4,4)
# Line.zero()
line.draw_line()

line2 = Line.zero()
line2.draw_line()

obj_count = Line.object_count
print(obj_count)
power = math.pow(4,3)
# print(power)

perimeter = Line.get_perimeter(12,3)
print(perimeter)
