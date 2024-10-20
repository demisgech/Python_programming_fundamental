class MyClass:

    def __init__(self, value):
        self.value = value
    @staticmethod
    def static_method(slef):
        print("Static method...")
    
    @classmethod
    def class_method(self):
        print("Class method...")
    @property
    def properties(self):
        print("Some properties...")
        return self.value
    @properties.setter
    def properties(self, new_value):
        print("Set properties...")
        self.value = new_value