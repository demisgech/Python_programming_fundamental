x = 10
y = 11
print("x",x)
print("y",y)

temp = x
x = y
y = temp

print("x",x)
print("y",y)

x = 10
y = 11
print("x",x)
print("y",y)

# The following three lines are exaclty the same
# They all are a tuple on the right side and unpacking them on the left side
x , y = y, x
x , y = (y, x)
[ x, y ] = (y, x)

print("x",x)
print("y",y)

# Assiginig a value to a variable in on line using tuple unpacking

a , b = 1, 2
print("a", a) # a 1
print("b", b) # b 2