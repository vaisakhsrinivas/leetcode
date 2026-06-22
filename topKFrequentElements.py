'''
Given an integer array nums and an integer k,
return the k most frequent elements. You may return the answer in any order.
'''


def topKFrequentElements(nums, k):

    result = []
    temp = []
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    for key,values in freq.items():
        temp.append([values,key])

    temp.sort()

    while len(result) < k:
        result.append(temp.pop()[1])
    return result

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequentElements(nums, k))

nums = [1]
k = 1
print(topKFrequentElements(nums, k))

nums = [1,2,1,2,1,2,3,1,3,2]
k = 2
print(topKFrequentElements(nums, k))