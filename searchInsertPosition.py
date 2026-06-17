'''
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
'''


def searchInsertPosition(arr, target):

    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


# Example 1:
nums = [1,3,5,6]
target = 5
#Output: 2
print(searchInsertPosition(nums, target))

#Example 2:
nums = [1,3,5,6]
target = 2
print(searchInsertPosition(nums, target))
#Output: 1

#Example 3:
nums = [1,3,5,6]
target = 7
print(searchInsertPosition(nums, target))
#Output: 4

