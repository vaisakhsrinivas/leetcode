'''
Given an integer array nums, return the third distinct maximum number in this array.
If the third maximum does not exist, return the maximum number.
'''

def thirdDistinctMax(nums):

    distinct = []
    for num in nums:
        if num not in distinct:
            distinct.append(num)
    distinct.sort()
    if len(distinct) < 3:
        return max(distinct)
    if len(distinct) >= 3:
        return distinct[-3]


nums = [3,2,1]
thirdmax = thirdDistinctMax(nums)
print(thirdmax)
#output = 1

nums = [1,2]
thirdmax = thirdDistinctMax(nums)
print(thirdmax)
#output = 2

nums = [2,2,3,1]
thirdmax = thirdDistinctMax(nums)
print(thirdmax)
#output = 1