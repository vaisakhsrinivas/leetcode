from ast import List


def twoSum(nums: List[int], target: int) -> List[int]:

    secondnumber = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in secondnumber:
            return [secondnumber[diff], i]
        secondnumber[nums[i]] = i


nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))

nums = [3,2,4]
target = 6
print(twoSum(nums, target))

nums = [3,3]
target = 6
print(twoSum(nums, target))
