from sys import getsizeof

values = (x * 2 for x in range(100000))
size_of_generators = getsizeof(values)
print("gen:",size_of_generators)


values = [x * 2 for x in range(100000)]
size_of_lists = getsizeof(values)
print("List:",size_of_lists)
