class RealNumber:
    def __init__(self, value):
        self.value = value

    # Addition
    def __add__(self, other):
        if isinstance(other, RealNumber):
            return RealNumber(self.value + other.value)
        return RealNumber(self.value + other)

    # Subtraction
    def __sub__(self, other):
        if isinstance(other, RealNumber):
            return RealNumber(self.value - other.value)
        return RealNumber(self.value - other)

    # Multiplication
    def __mul__(self, other):
        if isinstance(other, RealNumber):
            return RealNumber(self.value * other.value)
        return RealNumber(self.value * other)

    # Division
    def __truediv__(self, other):
        if isinstance(other, RealNumber):
            return RealNumber(self.value / other.value)
        return RealNumber(self.value / other)

    # String Representation
    def __str__(self):
        return str(self.value)

# Example Usage
num1 = RealNumber(10)
num2 = RealNumber(2)

print(f"num1 + num2 = {num1 + num2}")
print(f"num1 - num2 = {num1 - num2}")
print(f"num1 * num2 = {num1 * num2}")
print(f"num1 / num2 = {num1 / num2}")
print(f"num1 / num2 = {num1 / 7}")
