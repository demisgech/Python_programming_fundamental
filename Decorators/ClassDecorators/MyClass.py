# Class decorators are applied to classes to modify their behavior or add functionality

def singleton(cls):
    instances = {}

    def get_instances(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instances

@singleton
class MyClass:
    def __init__(self, value):
        self.value = value

obj1 = MyClass(89)
obj2 = MyClass(78)

print(obj1 is obj2)