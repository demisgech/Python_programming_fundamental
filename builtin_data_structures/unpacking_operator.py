numbers = [1,2,3,4,5]
# JavaScript(spread operator(...))
# values = [...numbers]
# Pytho (unpacking operator(*))
# values = [*numbers]

values = [*numbers,*range(3),*"Hello"]
print(values)

new_values = list(range(5))
print(new_values)

new_values = [*range(5)]
print(new_values)

first = [10,20,30]
second = [40,50,60,90]
combined = [*first, *second]
print(combined)

another_combined = [*first, *"abc","g",*second,*range(3)]
print(another_combined)

# Unpacking dictionary -> use **

first = {"X": 1, "Y": 3}
second = {"Z": 4, "F": 54}

unpacked_dictionary = {**first, **second}
unpacked_dictionary = {**first, "M": 45, **second}
unpacked_dictionary = {**first, "M": 45, **second, **{"L": 12,"N": 13}}
print(unpacked_dictionary)