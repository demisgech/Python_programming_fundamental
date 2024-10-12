point = {"x":1,"y":2}
point = dict(x=1,y=2)
x = point['x']
# print(x)

point['z'] = 20
print(point)

if "key" in point:
    print(point["key"])

print(point.get("key"))

# default value
print(point.get("key","Default value if key is not exist"))

# removing an item
if "key" in point:
    del point["key"]

# loop over dictionary

for key in point:
    print(key)

# Produces a tuple
for x in point.items():
    print(x)

# unpacking tuples

for key, value in point.items():
    print(key,value)
