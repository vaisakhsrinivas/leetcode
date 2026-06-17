'''
You are given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "neetcodeneetcode", needle = "neet"

Output: 0
'''


def firstOccurenceInAString(h, n):

    l = len(h)
    r = len(n)

    for i in range(l-r+1):
        j = 0
        while j < r:
            if h[i+j] != n[j]:
                break
            j += 1
        if j == r:
            return i
    return -1


haystack = "neetcodeneetcode"
needle = "neet"
# Output: 0
print(firstOccurenceInAString(haystack, needle))

haystack = "neetcode"
needle = "codem"

# Output: -1
print(firstOccurenceInAString(haystack, needle))
