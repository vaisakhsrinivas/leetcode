'''
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.

'''

def intersection(nums1, nums2):

    len1 = len(nums1)
    len2 = len(nums2)
    result = []

    if len1 < len2:
        for i in range(len1):
            if nums1[i] in nums2:
                result.append(nums1[i])
    else:
        for i in range(len2):
            if nums2[i] in nums1:
                result.append(nums2[i])
    return list(set(result))


nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection(nums1, nums2))
#ouput = [2]

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersection(nums1, nums2))
#output = [9,4]
