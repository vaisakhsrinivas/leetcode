def isAnagram(s, t):

    anagram = {}

    if len(s) != len(t):
        return False

    for char in s:
        anagram[char] = 1 + anagram.get(char, 0)

    for char in t:
        if char not in anagram:
            return False
        else:
            anagram[char] = anagram.get(char, 0) - 1

        if anagram[char] == 0:
            del anagram[char]

    if len(anagram) == 0:
        return True
    else:
        return False


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))

s = "rat"
t = "cat"
print(isAnagram(s, t))