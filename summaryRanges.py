'''
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
'''


def summaryRanges(nums):

    result = []
    i = 0

    while i < len(nums):
        start = nums[i]
        j = i
        while j+1 < len(nums) and nums[j+1] == nums[j]+1:
            j += 1
        if nums[j] == start:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[j]}")
        i = j+1
    return result


nums = [0,1,2,4,5,7]
ranges = summaryRanges(nums)
print(ranges)
#ouput - ['0->2', '4->5', '7']

nums = [0,2,3,4,6,8,9]
ranges = summaryRanges(nums)
print(ranges)
#ouput - ['0', '2->4', '6', '8->9']