'''
Given two strings ransomNote and magazine,
return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
'''

def ransomNote(ransomNote, magazine):

    ransomNoteDict = {}
    magazineDict = {}

    for char in magazine:
        magazineDict[char] = 1 + magazineDict.get(char, 0)

    for char in ransomNote:
        ransomNoteDict[char] = ransomNoteDict.get(char, 0) + 1
        if char not in magazineDict or ransomNoteDict[char] > magazineDict[char]:
            return False
    return True


print(ransomNote('a', 'b'))
print(ransomNote('aa', 'ab'))
print(ransomNote('aa', 'aab'))