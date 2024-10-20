class Word:
    def __init__(self, word):
        self.word = word

    # Don't do this for comparing things
    def __cmp__(self, other):
        return (len(self.word) != len( other.word) or
                len(self.word) < len( other.word) or 
                len(self.word) <= len( other.word) or 
                len(self.word) == len( other.word) or 
                len(self.word) > len( other.word) or 
                len(self.word) >= len( other.word) )

    def __gt__(self, other):
        return len(self.word) > len(other.word)
    
    def __ge__(self, other):
        return len(self.word) >= len(other.word)
    
    def __lt__(self, other):
        return len(self.word) < len(other.word)
    
    def __le__(self, other):
        return len(self.word) <= len(other.word)
    
    
    def __eq__(self, other):
        return len(self.word) == len(other.word)
    

    
    def __ne__(self, other):
        return len(self.word) != len(other.word)
    

word_one = Word("Hello")
word_two = Word("hello")

print(word_one == word_two)
print(word_one != word_two)
print(word_one > word_two)
print(word_one >= word_two)
print(word_one < word_two)
print(word_one <= word_two)