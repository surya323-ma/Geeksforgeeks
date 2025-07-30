Given an unsorted array arr[] of integers, find the number of subarrays whose sum exactly equal to a given number k.

class Solution:
    def cntSubarrays(self, arr, k):
        # code here
    
        prefix_counts = {0: 1}
        curr_sum = 0
        count = 0

        for num in arr:
            curr_sum += num
            count += prefix_counts.get(curr_sum - k, 0)
            prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1

        return count   
