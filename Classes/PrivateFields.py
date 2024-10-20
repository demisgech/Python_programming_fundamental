class TagCloud:
    def __init__(self):
        self.__tags = {}
    
    def add(self, tag):
        # self.__tags[tag] = self.__tags.get(tag, 0) + 1
        # Take care case-sensitivity
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    # get item using subscript opertator like obj[key]
    def __getitem__(self,tag):
        return self.__tags.get(tag.lower(), 0)

    # set item using subscript operator like obj[key] = value
    # def __setitem__(self, key, value):
    #     self.__tags[key] = value

    def __setitem__(self, tag, count):
        self.__tags[tag] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)
    
    def __str__(self):
        return str(self.__tags)
    

cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")


# tags = cloud.__tags # AttributeError: 'TagCloud' object has no attribute '__tags'
# print(tags)

attribute_holder = cloud.__dict__
print(attribute_holder)

# accessing private fields
private_fieds = cloud._TagCloud__tags
print(private_fieds)

""""
GENERALLY SPEAKING:
In Python, there's no formal way to specify 
access levels (like public, private, protected) 
as you would find in languages like C++ or Java. 
Instead, Python relies on naming conventions to 
indicate the intended use of attributes and methods
"""

# Here's a class demonstrating these conventions:
class MyClass:
    def __init__(self, public_value, protected_value, private_value):
        self.public_value = public_value
        self._protected_value = protected_value
        self.__private_value = private_value

    def public_method(self):
        return "This is a public method."

    def _protected_method(self):
        return "This is a protected method."

    def __private_method(self):
        return "This is a private method."

    def access_private_method(self):
        return self.__private_method()

# Example Usage
obj = MyClass(1, 2, 3)
print(obj.public_method())  # Accessible
print(obj._protected_method())  # Accessible, but should be treated as protected
print(obj.access_private_method())  # Correct way to access private method
print(obj._MyClass__private_method())  # Access via name mangling (not recommended)
