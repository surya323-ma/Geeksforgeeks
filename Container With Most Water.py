Given an array arr[] of non-negative integers, where each element arr[i] represents the height of the vertical lines, find the maximum amount of water that can be contained between any two lines, together with the x-axis.

Note: In the case of a single vertical line it will not be able to hold water.


class Solution:
    def maxWater(self, arr):
        left=0
        right=len(arr)-1
        res=0
        while left<right :
            water=min(arr[left],arr[right])*(right-left)
            res=max(res,water)
            if arr[left]<arr[right]:left+=1
            else:right-=1
        return res
        # code here
