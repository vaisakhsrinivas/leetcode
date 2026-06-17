'''
Given a string s, find the length of the longest substring without duplicate characters.
Leetcode: 3
'''


def lengthOfLongestSubstring(s):
    length = 0
    left = 0
    substr = set()
    for right in range(len(s)):
        while s[right] in substr:
            substr.remove(s[left])
            left += 1
        substr.add(s[right])
        length = max(length, right - left + 1)
    return length

s = "abcabcbb"
# output 3
print(lengthOfLongestSubstring(s))

s = "bbbbb"
# output 1
print(lengthOfLongestSubstring(s))

s = "pwwkew"
# output 3
print(lengthOfLongestSubstring(s))

