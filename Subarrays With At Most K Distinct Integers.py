You are given an array arr[] of positive integers and an integer k, find the number of subarrays in arr[] where the count of distinct integers is at most k.

Note: A subarray is a contiguous part of an array.

  class Solution:
    def countAtMostK(self, arr, k):
        count = defaultdict(int)
        left = 0
        result = 0

        for right in range(len(arr)):
            if count[arr[right]] == 0:
                k -= 1
            count[arr[right]] += 1

            while k < 0:
                count[arr[left]] -= 1
                if count[arr[left]] == 0:
                    k += 1
                left += 1

            result += right - left + 1

        return result
