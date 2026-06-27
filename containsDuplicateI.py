'''
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
'''


def containsDuplicateI(nums):

    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print(containsDuplicateI([1,2,3,1]))
print(containsDuplicateI([1,2,3,4]))
print(containsDuplicateI([1,1,1,3,3,4,3,2,4,2]))