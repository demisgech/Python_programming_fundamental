
def say_hello(response):
    match response:
        case _ :
            return "Hello"
        
result = say_hello("Demis")
print(result)

# Another example

def factorial(n:int)->int:
    if n in (1, 0):
        return 1
    return n * factorial(n - 1)
    
fact = factorial(4)
print(fact)

# match and case also know as switch and case for other languages like C++, Java, JS, C#
def factorial_another_way(n:int)->int:
    match n:
        case 0 | 1:
            return 1
        case _ :
            return n * factorial(n - 1)
    
fact = factorial_another_way(4)
print(fact)

def factorial_another_ellegant_way(n:int)->int:
   return 1 if n in (1, 0) else n * factorial_another_ellegant_way(n - 1)
    
fact = factorial_another_ellegant_way(4)
print(fact)