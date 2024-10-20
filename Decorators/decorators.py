""""
Decorators are a feature in Python 
that allows you to modify the behavior 
of functions or methods without changing their actual code.
they use @ sign followed by decorators name like this @my_decorators
"""

def decorators(function):
    def wrapper():
        print("Before function called")

        function()

        print("After function called")
        
    return wrapper

@decorators
def call_decorators():
    print("Hello the powerful decorators")


call_decorators()