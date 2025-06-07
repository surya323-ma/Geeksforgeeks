Given two binary arrays, a1[] and a2[]. Find the length of longest common span (i, j) where j>= i such that a1[i] + a1[i+1] + .... + a1[j] =  a2[i] + a2[i+1] + ... + a2[j].
#codw here
class Solution:
    def longestCommonSum(self, a1, a2):
        #Code here.
        n = len(a1)
        diff = [a1[i] - a2[i] for i in range(n)]
    
        prefix_sum = 0
        sum_index_map = {0: -1}  # Initialize for cases where the subarray starts from index 0
        max_length = 0

        for i in range(n):
            prefix_sum += diff[i]
            if prefix_sum in sum_index_map:
                max_length = max(max_length, i - sum_index_map[prefix_sum])
            else:
                sum_index_map[prefix_sum] = i

        return max_length
