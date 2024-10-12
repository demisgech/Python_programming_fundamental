numbers = [1,1,2,2,3,4]
uniques = set(numbers)
# print(uniques)

uniques.add('d')
uniques.add('3')
# print(uniques)

second = {1,2,3}
second.add(4)
# second.remove(5) # throw a KeyError exception
second.pop()
second.discard(1) # it removes the item if it exist without throwing exeption like remove() method

third = {23,34,56}
second.update(third)
# print(second)

length = len(third)
intersection = second.intersection(third)
# print(intersection)

union = second.union(third)
# print(union)

fourth = {1,2,'a','b'}
fourth_differ_second = fourth.difference(second)

print(second)
print(fourth_differ_second)

second_differ_fourth = second.difference(fourth)
print(second_differ_fourth)
