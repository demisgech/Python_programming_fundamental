values = []

for x in range(10):
    values.append(x*2)
# print(values)

# Mapping values
values = map(lambda value: value*2, range(10))
for value in values:
    print(value)

# Using list comprehension to map a values
new_values = [value * 2 for value in range(10)]
# print(new_values)


dict_values = {}
for value in range(10):
    dict_values[value] = value * 2
print(dict_values)

# Dictionary comprehension
# {expression for item in iterable}

dict_values = { value: value * 2 for value in range(10)}
print(dict_values)