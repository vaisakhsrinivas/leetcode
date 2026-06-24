'''
You are given two integer arrays nums1 and nums2, both sorted in non-decreasing order, along with two integers m and n, where:

m is the number of valid elements in nums1,
n is the number of elements in nums2.
The array nums1 has a total length of (m+n), with the first m elements containing the values to be merged, and the last n elements set to 0 as placeholders.

Your task is to merge the two arrays such that the final merged array is also sorted in non-decreasing order and stored entirely within nums1.
You must modify nums1 in-place and do not return anything from the function.

Example 1:

Input: nums1 = [10,20,20,40,0,0], m = 4, nums2 = [1,2], n = 2

Output: [1,2,10,20,20,40]
'''

def mergeSortedArray(nums1, m, nums2, n):

    l1 = m-1
    l2 = n-1
    merge = m + n - 1

    while l2 >=0:
        if l1>=0 and nums1[l1] > nums2[l2]:
            nums1[merge] = nums1[l1]
            l1 -= 1
        else:
            nums1[merge] = nums2[l2]
            l2 -= 1
        merge -= 1

nums1 = [10,20,20,40,0,0]
m = 4
nums2 = [1,2]
n = 2

mergeSortedArray(nums1, m, nums2, n)
print(nums1)

nums1 = [0,0]
m = 0
nums2 = [1,2]
n = 2

mergeSortedArray(nums1, m, nums2, n)
print(nums1)
