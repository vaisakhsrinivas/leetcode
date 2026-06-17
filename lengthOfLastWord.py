'''
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
'''


def lengthOfLastWord(s):

    s = s.strip()
    words = s.split(" ")
    return len(words[-1])


#Input:
s = "Hello World"
#Output: 5
print(lengthOfLastWord(s))

s = " fly me   to   the moon  "
#Output: 4
print(lengthOfLastWord(s))

s = "luffy is still joyboy"
#Output: 6
print(lengthOfLastWord(s))
