
letters = ['A','B','C','D',"F"]

# Accessing single item
first_letter = letters[0]
# print(first_letter)

last_letter = letters[len(letters) - 1]
last_letter = letters[-1]
# print(last_letter)

# Modifyinig item
first_letter = 'a'
letters[0] = first_letter
# print(letters)

# Extracting items

some_letters_from_beginning = letters[0:3]
# print(some_letters_from_beginning)

some_letters_from_end = letters[3:]
# print(some_letters_from_end)

all_letters = some_letters_from_beginning + some_letters_from_end
# print(all_letters)

cloned = letters[:]
# print(cloned)

# Slicing

sliced_by_2 = letters[::2]
# print(sliced_by_2)

sliced_by_negative_2 = letters[::-2]
# print(sliced_by_negative_2)