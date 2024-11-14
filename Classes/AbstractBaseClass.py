from abc import ABC, abstractmethod

class InvalidOperationError(Exception):
    pass
#  A good examples fo inheritance
class Stream(ABC):
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

    @abstractmethod
    def read(self):
        pass
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


class MemoryStream(Stream):
    def read(self):
        print("Reading from memory stream")


momory = MemoryStream()
momory.read()

file_stream = FileStream()
file_stream.open()
file_stream.read()


network_stream = NetworkStream()
network_stream.open()
network_stream.read()