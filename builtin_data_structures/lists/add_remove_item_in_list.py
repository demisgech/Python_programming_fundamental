letters = ['a','b','c']

# Add 
letters.append('d')
letters.insert(2,'F')

# Remove
letters.pop(-1) # same as letters.pop()
letters.pop(0) # remove from the beginning
letters.remove("c") # remove the first occurrence of the item if exist

del letters[0] # delete by its index
del letters[0:3] # delete a group of items starting from index all the way to 3
letters.clear() # to remove all items in the list

letters = ['a','b','c','a']
cloned = letters.copy() # copying a list
# print(cloned)
count_letter = letters.count('a')
print(count_letter)

# Extending list
letters.extend(['d','e','f'])
print (letters)
letters.sort() # ascending order
letters.sort(key=None,reverse=True) # decending order

sorted_letters = letters
print(sorted_letters)
