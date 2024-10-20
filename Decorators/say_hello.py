
def my_decorator(function):
    def wrapper():
        print("Something is happening before function is called!")
        function()
        print("Something is happening after function is called!")

    return wrapper

@my_decorator
def say_hello():
    print("Hello Decorators!")

say_hello()