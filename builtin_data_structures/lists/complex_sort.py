items = [
    ("Product 1",10),
    ("Product 2",9),
    ("Product 3",12)
]

items.sort() # Nothing happen here

def sort_item(item):
    return item[1]

items.sort(key=sort_item) # giving a referrence to a function sort_item not calling it
print(items)