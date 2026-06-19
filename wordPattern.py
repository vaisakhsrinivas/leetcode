'''
You are given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
'''

def wordPattern(pattern, string):

    patterndict = {}
    stringdict = {}

    words = string.split()

    for char, word in zip(pattern, words):
        if char in patterndict and patterndict[char] != word:
            return False
        if word in stringdict and stringdict[word] != char:
            return False
        patterndict[char] = word
        stringdict[word] = char
    return True

pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern, s))
#output True

pattern = "abba"
s = "dog cat cat fish"
print(wordPattern(pattern, s))
#output False

pattern = "aaaa"
s = "dog cat cat fish"
print(wordPattern(pattern, s))
#output False

