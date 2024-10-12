letters = ['a','b','c','d']

for letter in letters:
    print(letter)

for letter in enumerate(letters):
    # print(letter)
    print(letter[0],letter[1])

# Unpacking tuple -> index, letter = (key, value)
for index, letter in enumerate(letters):
    print(index, letter)
    