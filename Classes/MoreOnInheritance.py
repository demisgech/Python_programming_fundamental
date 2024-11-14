class Employee:
    def greet(self):
        print("Employee Greet!")


class Person:
    def greet(self):
        print("Person Greet!")


# Multiple Inheriatance
class Manager(Employee, Person):
    pass

manager = Manager()
manager.greet()

# Good example of multiple inheritance

class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass


class InvalidOperationError(Exception):
    pass
#  A good examples fo inheritance
class Stream:
    def __init__(self):
        self.opened = False
    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False


class FileStream(Stream):
    def read(self):
        print("Reading data from a file.")
    
    def write(self):
        print("Writing data to a file.")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")
    
    def write(self):
        print("Writing data to a network.")


file_stream = FileStream()
file_stream.open()
file_stream.read()


network_stream = NetworkStream()
network_stream.open()
network_stream.read()