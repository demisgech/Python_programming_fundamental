
numbers = [1,1,2,3,4,4]

first = set(numbers)
second = {3,5,6}

union = first | second
print(union)

intersection = first & second
print(intersection)

difference = first - second 
print(difference)

semetric_difference = first ^ second
print(semetric_difference)

# Check existence

if 1 in first:
    print('yes')

