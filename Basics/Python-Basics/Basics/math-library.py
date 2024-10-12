import math

print(round(12.53))
print(abs(-3.4))

# Lowest-Greatest integer function
print("---- Lowest-Greatest Integer ----")
print(math.ceil(2.3))  # Lowest
print(math.floor(2.3))  # Greatest

# absolute value
print("--- Absolute value ----")
print(math.fabs(-2.3))

# Hypotenuse of a triangle
print("---- Pythagorean Identity ---- ")
print(math.hypot(4, 3))

# Greatest Common Divisor (GCD)
print("---- Common Factor and Multiple -----")
print(math.gcd(25, 75))

# List Common Multiple (LCM)
print(math.lcm(12, 13))

# root
print("----- Root -----")
print(math.sqrt(5))
print(math.cbrt(125))

# power(exponent)
print(" ----- Power -----")
print(math.erfc(5))  # reciprocal of e
print(math.exp(5))  # power of e
print(math.pow(5, 3))

# Logarithm
print("----- Logarithm -----")
print(math.log(16, 4))
print(math.log2(10))

# Distance between numbers (points (coordinates))
print("----- Distance between points ------")
numberList1 = [1]
numberList2 = [11]
print(math.dist(numberList1, numberList2))

numberList1 = [1, 2]
numberList2 = [4, 6]

print(math.dist(numberList1, numberList2))

# factorial, permutation and combination
print("---- Factorial, Permutation and Combination ----")
# Factorial of a number
print(math.factorial(5))

# combination
print(math.comb(10, 4))

# permutation
print(math.perm(5, 3))

# Trigonometric function
print("---- Trigonometric function ---- ")
radian = 57.3
x = 45/radian
print(math.sin(x))
print(math.cos(x))
print(math.tan(x))

# Hyperbolic function
print("---- Hyperbolic function -----")
y = 0
print(math.sinh(y))
print(math.cosh(y))

