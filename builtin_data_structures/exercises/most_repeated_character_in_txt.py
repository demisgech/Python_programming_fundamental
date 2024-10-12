from pprint import pprint

sentence = "This is a common interview question"
letters = [*sentence]
# print(letters)

# The long way
# letter_dict = {}
# for letter in letters:
#    letter_dict[letter] = letters.count(letter)
# print(letter_dict)

# The short way
new_letter_dict = {
    letter: letters.count(letter)
      for letter in letters}
# print(new_letter_dict)

most_repeated_chars = [ 
    (key,value) for [key,value] 
    in new_letter_dict.items() 
    if value >= max(*[ new_letter_dict[k] for k in new_letter_dict]) ]
print(most_repeated_chars)

for most_repeated_char in most_repeated_chars:
    print(most_repeated_char[0],most_repeated_char[1])

# Aanother techniques

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
# pprint(char_frequency, width=1)

# print(sorted(char_frequency.items(), key=lambda kv:kv[1], reverse=True))
char_frequency_sorted = sorted(char_frequency.items(),
                                key=lambda kv:kv[1], 
                                reverse=True)
print(char_frequency_sorted[0]) # However, it is not much ellegant than the previous solution