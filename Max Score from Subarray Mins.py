Max Score from Subarray Mins
You are given an array arr[] of integers. Your task is to find the maximum sum of the smallest and second smallest elements across all subarrays (of size >= 2) of the given array.
#code herre
  class Solution:
    def maxSum(self, arr):
        return max(arr[i-1]+arr[i] for i in range(1,len(arr)))



#second chioce
    
class Solution:
    def maxSum(self, arr):
        max_sum = float('-inf')
        for i in range(1, len(arr)):
            pair_sum = arr[i - 1] + arr[i]
            if pair_sum > max_sum:
                max_sum = pair_sum
        return max_sum
