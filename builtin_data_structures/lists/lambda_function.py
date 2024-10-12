items = [
    ("Product 1",10),
    ("Product 2",9),
    ("Product 3",12)
]


items.sort(key=lambda item:item[1])
print(items)

