def rotateString(s :str, goal : str):

    result = ""
    l = len(s)
    for i in range(l):
        result = s[i:] + s[:i]
        if result == goal:
            return True
            break
    return False

# Example 1
s = "abcde"
goal = "cdeab"
print(rotateString(s, goal))

# Example 2
s = "abcde"
goal = "abced"
print(rotateString(s, goal))
#Output: false