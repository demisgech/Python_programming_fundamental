point = (1,2)
print(type(point))

# NB: if tuples has only one item,
#  you have to use the trailing comma after the item
#  otherwise python treat it as int
# That means:

point = 1
point = (1)
print(type(point))   # <class 'int'>

point = (1,)
point = 1,
print(type(point))   # <class 'tuple'>

empty_tuple = ()

concatinate_tuple = (1,2) + (3,4)
print(concatinate_tuple)

iterable = [1,2,3,4,5]

builtin_tuple = tuple(iterable)
print(builtin_tuple)

builtin_tuple = tuple("Hello Tuple")
print(builtin_tuple)

# Accessing item  using index

point = (12,34)
x = point[0]
y = point[1]

print(f'point(x,y) = ({x},{y})')

# Unpacking tuple
x, y = point
[ x, y ]= point
print(f'point(x,y) = ({x},{y})')

# Extracting item
print(builtin_tuple[0:5])

# Check existence of an item

if 12 in point:
    print('Exist')

# counting item

count = builtin_tuple.count('l')
print(count)

index = builtin_tuple.index('l')
print(index)