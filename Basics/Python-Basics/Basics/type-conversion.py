x = input("X: ")
print(type(x))  # type(param) is a function to return its data type

# built-in function to convert a value
# int(x) - to integer
# float(x) - to floating point numbers
# bool(x) - to boolean(True or False)
# str(x) - to string

y = float(x) + 1
print(F"x: {x}, y: {y}")

# Falsy
print(bool(False))
print(bool(0))
print(bool(""))

# Truthy
print(bool(True))
print(bool(1))
print(bool(-1))
print(bool("False"))
print(bool("True"))
