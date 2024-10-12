items = {
    "product 1": 23,
    "product 2": 29.9,
    "product 3": 56.4,
    "product 4": 34
}

# Key of dictionary
for item_key in items:
    print(item_key)

# Values of dictionary
for item_key in items:
    print(items[item_key])

# Producing tuples
for item in items.items():
    print(item)

# Destructuring(unpacking ) the produced tuple
for key, value in items.items():
    print(key,value)