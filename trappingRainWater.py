'''
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
'''


def trap(height):

    left = 0
    right = len(height)-1
    lmax = height[left]
    rmax = height[right]
    totaltrap = 0
    while left < right:
        if lmax < rmax:
            left += 1
            lmax = max(lmax, height[left])
            totaltrap += lmax - height[left]
        else:
            right -= 1
            rmax = max(rmax, height[right])
            totaltrap += rmax - height[right]
    return totaltrap


height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))

height = [4,2,0,3,2,5]
print(trap(height))
