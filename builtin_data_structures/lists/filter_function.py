items = [
    ("Product 1",10),
    ("Product 2",4),
    ("Product 3",14)
]

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