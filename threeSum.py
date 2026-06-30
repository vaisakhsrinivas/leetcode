'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''

def threeSum(nums):
    nums.sort()
    result = []
    for i,n in enumerate(nums):
        if n > 0:
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i+1
        right = len(nums)-1
        while left < right:
            if nums[left] + nums[right] + n > 0:
                right -= 1
            elif nums[left] + nums[right] + n < 0:
                left += 1
            else:
                result.append([nums[left],nums[right],n])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
    return result



print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,1,1]))
print(threeSum([0,0,0]))
