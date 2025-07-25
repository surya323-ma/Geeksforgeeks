You are given a circular array arr[] of integers, find the maximum possible sum of a non-empty subarray. In a circular array, the subarray can start at the end and wrap around to the beginning. Return the maximum non-empty subarray sum, considering both non-wrapping and wrapping cases.

class Solution:
    def maxCircularSum(self, arr):
        total_sum = sum(arr)
        max_kadane = curr_max = arr[0]
        min_kadane = curr_min = arr[0]

        for num in arr[1:]:
            curr_max = max(num, curr_max + num)
            max_kadane = max(max_kadane, curr_max)

            curr_min = min(num, curr_min + num)
            min_kadane = min(min_kadane, curr_min)

        return max_kadane if max_kadane < 0 else max(max_kadane, total_sum - min_kadane)
