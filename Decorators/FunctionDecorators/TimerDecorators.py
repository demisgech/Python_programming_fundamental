import time

def timer_decorator(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        print(f"Function {function.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(3)
    return "Functio completed!"

print(slow_function())