numbers = list(range(10))
numbers.insert(3,12)
numbers.insert(5,11)
numbers.sort() # ascending order
numbers.sort(reverse=True) # descending order

# print(numbers)

# Built in sorted function creates a new sorted list which is other than the original list

sorted_numbers_in_asc_order = sorted(numbers) 
# print(sorted_numbers_in_asc_order)

sorted_numbers_in_desc_order = sorted(numbers,reverse=True) 
print(sorted_numbers_in_desc_order)