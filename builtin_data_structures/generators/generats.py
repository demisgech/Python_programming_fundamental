# Generators object -> helps to save memory wastage that
# comes from the use of large dataset in lists, sets and dictionary
# (expression for item in iterable)
values = (x * 2 for x in range(10))
print(values)
for x in values:
    print(x)