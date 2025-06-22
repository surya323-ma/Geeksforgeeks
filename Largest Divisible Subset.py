Given an array arr[] of distinct positive integers. Your task is to find the largest subset such that for every pair of elements (x, y) in the subset, either x divides y or y divides x.
Note : If multiple subsets of the same maximum length exist, return the one that is lexicographically greatest, after sorting the subset in ascending order.
#code here
  class Solution:
    def largestSubset(self, arr):
        if not arr:
            return []
        
        arr.sort()
        n = len(arr)
        
        dp = [[num] for num in arr]

        for i in range(n):
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    if len(dp[j]) + 1 > len(dp[i]):
                        dp[i] = dp[j] + [arr[i]]
                    elif len(dp[j]) + 1 == len(dp[i]):
                        dp[i] = max(dp[i], dp[j] + [arr[i]])
        
        max_len = max(len(sub) for sub in dp)
        candidates = [sub for sub in dp if len(sub) == max_len]
        return max(candidates)
