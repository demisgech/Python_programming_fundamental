
class MagicPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show_result(self):
        print(f"{self.x} {self.y}")

    def __str__(self):
        return f"Magic dirction{self.x, self.y}"

    # Comparing other object (equality(==))
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

   # greater than operator(>)
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y
    
    # less than operator(<)
    def __lt__(self, other):
        return self.x < other.x and self.y < other.y
    
    # less or equal 
    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y
    
    # less or equal 
    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y
    
    def __ne__(self, other):
        return self.x != other.x and self.y != other.y
    
    def draw(self):
        print(f"({self.x}, {self.y})")


magic_point = MagicPoint(2,4)
magic_point.show_result()
print(str(magic_point))


other_magic_point =  MagicPoint(1,2)
# print(other_magic_point == magic_point) -> True

print(other_magic_point != magic_point)
print(other_magic_point < magic_point)
print(other_magic_point <= magic_point)
print(other_magic_point == magic_point)
print(other_magic_point > magic_point)
print(other_magic_point >= magic_point)
