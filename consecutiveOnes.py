'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.
'''

def consecutiveOnes(nums):

    result = 0
    count = 0
    for num in nums:
        if num == 0:
            count = 0
        else:
            count += 1

        if result < count:
            result = count
    return result


nums = [1,0,1,1,0,1]
print(consecutiveOnes(nums))
#output = 2

nums = [1,1,0,1,1,1]
print(consecutiveOnes(nums))
#output = 3