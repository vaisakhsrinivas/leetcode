'''Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].'''

def findFirstAndLastPositionInSortedArray(nums, target):

    result = []
    for i, n in enumerate(nums):
        if n == target:
            result.append(i)
    if len(result) == 0:
        return [-1, -1]
    elif len(result) == 1:
        return [result[0], result[0]]
    elif len(result) == 2:
        return result
    else:
        return [result[0], result[-1]]



nums = [5,7,7,8,8,10]
target = 8
#Output: [3,4]
first, last = findFirstAndLastPositionInSortedArray(nums, target)
print(first, last)


nums = [5,7,7,8,8,10]
target = 6
#Output: [-1,-1]
first, last = findFirstAndLastPositionInSortedArray(nums, target)
print(first, last)

nums = []
target = 0
#Output: [-1,-1]
first, last = findFirstAndLastPositionInSortedArray(nums, target)
print(first, last)