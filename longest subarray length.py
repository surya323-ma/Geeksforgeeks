from math import inf
class Solution:
    def longestSubarray(self, arr):
        S = []
        res = 0
        arr.append(inf)
        for i in range(len(arr)):
            while S and arr[S[-1]] < arr[i]:
                j, l = S.pop(), i - 1 - (S[-1] if S else -1)
                if arr[j] <= l:
                    res = max(res, l)
            S.append(i)
        return res

  You are given an array of integers arr[]. Your task is to find the length of the longest subarray such that all the elements of the subarray are smaller than or equal to the length of the subarray.
