def process(item):
    match item:
        case (x, y) if x > y:
            print(f"x ({x}) is greater than y ({y})")
        case (x, y) if x < y:
            print(f"x ({x}) is less than y ({y})")
        case (x, y):
            print(f"x ({x}) is equal to y ({y})")
        case _:
            print("No match found")


def versatile_syntax(value, SomeClass:object):
    match value:
        case 1:
            print("One")

        case [x, y]:
            print(f"List with two elements: {x}, {y}")

        case {"key": value}:
            print(f"Value for key: {value}")

        case SomeClass(attr1, attr2):
            print(f"Attributes: {attr1}, {attr2}")

        case x if x > 10:
            print(f"x is greater than 10")

        case x:
            print(f"x is {x}")

        # case _:
        #     print("Anything")
                            
class SomeClass:
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

instance = SomeClass('value1', 'value2')

match instance:
    case SomeClass(attr1, attr2):
        print(f"Attributes: {attr1}, {attr2}")
