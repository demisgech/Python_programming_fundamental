
def log_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"Calling function {function.__name__} with arguments {args } and {kwargs}")

        result = function(*args, **kwargs)

        print(f"Function {function.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(x, y):
    return x + y

add(x=9,y=89)
