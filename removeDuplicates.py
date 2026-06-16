# inplace solution - for details check the question in leetcode

def removeDuplicates(s):
    count = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            s[count] = s[i]
            count += 1
    return count

nums = [1,1,2]
#output count = 2 and nums should be [1,2,2]
print(removeDuplicates(nums))

nums = [0,0,1,1,1,2,2,3,3,4]
#output count = 5
print(removeDuplicates(nums))
