def isAnagram(s, t):

    word1 = {}
    word2 = {}

    for char in s:
        word1[char] = word1.get(char, 0) + 1

    for char in t:
        word2[char] = word2.get(char, 0) + 1

    if word1 == word2:
        return True
    return False


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))

s = "rat"
t = "cat"
print(isAnagram(s, t))