'''
Given an integer array nums and an integer k,
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
'''


def containsDuplicateII(nums, k):

    seen = set()
    left = 0

    for right in range(len(nums)):
        if right-left > k:
            seen.remove(nums[left])
            left += 1
        if nums[right] in seen:
            return True
        seen.add(nums[right])
    return False


print(containsDuplicateII([1,2,3,1], 3))
print(containsDuplicateII([1,0,1,1], 1))
print(containsDuplicateII([1,2,3,1,2,3], 2))