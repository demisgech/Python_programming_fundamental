numbers = [12,34,56]

first = numbers[0]
second = numbers[1]
third = numbers[2]

# print(f'First: {first}, Second: {second}, Third: {third}')

# Unpacking in Python
# Destructuring in JavaScript
# Structure binding in C++

[first,second,third] = numbers
# print(f'First: {first}, Second: {second}, Third: {third}')

# another way(syntax)

first, second, third = numbers
# print(f'First: {first}, Second: {second}, Third: {third}')

number_list = [1,2,3,4,56,76]

# Unpacking multiple item

first, second, *other = number_list
# print(f'First: {first}, Second: {second}, Other: {other}')

# Another syntax
[first, second, *other] = number_list
# print(f'First: {first}, Second: {second}, Other: {other}')

# Getting first and last item
[first, *other, last] = number_list
print(f'First: {first}, last: {last}, Other: {other}')