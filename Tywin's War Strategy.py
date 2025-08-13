You are given an array arr[] of size n, where arr[i] represents the number of soldiers in the i-th troop. You are also given an integer k. A troop is considered "lucky" if its number of soldiers is a multiple of k. Find the minimum total number of soldiers to add across all troops so that at least ⌈n / 2⌉ troops become lucky.
import math
class Solution:
    def minSoldiers(self, arr, k):
        n = len(arr)
        required = math.ceil(n / 2)
        lucky_count = sum(1 for x in arr if x % k == 0)
        if lucky_count >= required:
            return 0
        deltas = [k - (x % k) for x in arr if x % k != 0]
        deltas.sort()
    
        to_add = required - lucky_count
        return sum(deltas[:to_add])    
