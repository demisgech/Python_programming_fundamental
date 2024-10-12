items = [
    ("Product 1",10),
    ("Product 2",4),
    ("Product 3",14)
]

prices = []
# Mapping items to new list
for item in items:
    prices.append(item[1])

# print(prices)

new_prices = map(lambda item:item[1],items)

for new_price in new_prices:
    print(new_price)
    
# converting iterable map object to iterable list
converted_price_list = list(map(lambda item:item[1],items))

print(converted_price_list)

