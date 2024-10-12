def multiply(x,y):
    return x * y


multiply(12,34)

def multiple_numbers(*numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

print("Start")

print(multiple_numbers(1,3,2,4,5))

print("End")