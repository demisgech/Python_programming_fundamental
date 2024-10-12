items = [
    ("Product 1",10),
    ("Product 2",4),
    ("Product 3",14)
]

new_mapped_items = map(lambda item: item[1] >= 10,items)

# List comprehension for mapping an item
# prices = [expression for item in items]

mapped_prices = [ item[1]  for item in items ]
print(mapped_prices)


filtered_items = []

for item in items:
    if item[1] >= 10:
        filtered_items.append(item)

print(filtered_items)

# Built in filter function

new_filtered_items = filter(lambda item: item[1] >= 10,items)

for new_filtered_item in new_filtered_items:
    print(new_filtered_item)

# Convert to iterable list from tuple

converted_filtered_items = list(filter(lambda item: item[1] >= 10, items))

print(converted_filtered_items)

items_filtered = filter(lambda item: item[1] >= 10, items)

# List comprehension for filtering an item
# [ expression for item in items if item[1] >= 10]

items_filtered = [ item for item in items if item[1] >= 10]
print(items_filtered)