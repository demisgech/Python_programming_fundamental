class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Addition
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    # Subtraction
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    # Multiplication
    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)

    # Division
    def __truediv__(self, other):
        denominator = other.real**2 + other.imag**2
        real = (self.real * other.real + self.imag * other.imag) / denominator
        imag = (self.imag * other.real - self.real * other.imag) / denominator
        return ComplexNumber(real, imag)

    # String Representation
    def __str__(self):
        return f"{self.real} + {self.imag}i"

# Example Usage
num1 = ComplexNumber(3, 4)
num2 = ComplexNumber(1, 2)

print(f"num1 + num2 = {num1 + num2}")
print(f"num1 - num2 = {num1 - num2}")
print(f"num1 * num2 = {num1 * num2}")
print(f"num1 / num2 = {num1 / num2}")
