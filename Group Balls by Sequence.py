You are given an array arr[] of positive integers, where each element arr[i] represents the number written on the i-th ball, and a positive integer k.
Your task is to determine whether it is possible to rearrange all the balls into groups such that:


Each group contains exactly k balls.
The numbers in each group are consecutive integers
from collections import Counter 
#code here

class Solution:
    def validgroup(self, arr, k):
        if len(arr) % k != 0:
            return False

        count = Counter(arr)
        for num in sorted(count):
            freq = count[num]
            if freq > 0:
                for i in range(num, num + k):
                    if count[i] < freq:
                        return False
                    count[i] -= freq
        return True
