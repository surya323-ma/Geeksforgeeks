You are given an array arr[] of integers and two integers a and b, You have to find the maximum possible sum of a contiguous subarray whose length is at least a and at most b.
from collections import deque
class Solution:
    def maxSubarrSum(self, arr, a, b):
        n = len(arr)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]

        max_sum = float('-inf')
        dq = deque()
        for i in range(a, n + 1):
        # Maintain deque for minimum prefix in window of size b - a + 1
            if i - b > 0:
                while dq and dq[0] < i - b:
                    dq.popleft()
            while dq and prefix[dq[-1]] >= prefix[i - a]:
                dq.pop()
            dq.append(i - a)
            max_sum = max(max_sum, prefix[i] - prefix[dq[0]])
        return max_sum
