# 
# Mapping values
values = map(lambda value: value*2, range(10))
for value in values:
    print(value)

# Using list comprehension to map a values
new_values = [value * 2 for value in range(10)]
# print(new_values)

# set comprehension
# {expression for item in iterable}

dict_values = { value * 2 for value in range(10)}
print(dict_values)