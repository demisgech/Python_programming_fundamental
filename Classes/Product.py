class Product:
    def __init__(self, price):
        self.set__price(price)

    def get__price(self):
        return self.__price

    def set__price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self.__price = value

try:
    product = Product(2)
    price = product.get__price()
    print(price)
    product.set__price(-9)
except ValueError as exception:
    print(exception)

class ProductWithAnotherTechnique:
    def __init__(self, price):
        self.set__price(price)

    def get__price(self):
        return self.__price

    def set__price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self.__price = value
    price = property(get__price, set__price)


productWithAnotherTechnique = ProductWithAnotherTechnique(12)
price = productWithAnotherTechnique.price
# print(price)

productWithAnotherTechnique.price = 20
price = productWithAnotherTechnique.price
print(price)


class ProductWithDecorators:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self.price = value
  

productWithDecorator = ProductWithAnotherTechnique(12)
price = productWithDecorator.price
# print(price)

productWithDecorator.price = 20
price = productWithDecorator.price
print(price)