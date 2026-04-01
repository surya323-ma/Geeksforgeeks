Given an array arr[] and an integer diff, count the number of ways to partition the array into two subsets such that the difference between their sums is equal to diff.

Note: A partition in the array means dividing an array into two subsets say S1 and S2 such that the union of S1 and S2 is equal to the original array and each element is present in only one of the subsets.
class Solution:
    def countPartitions(self, arr, diff):
        # code here
        total = sum(arr)
        if (total + diff) % 2 != 0 or total < diff:
            return 0
        target = (total + diff) // 2
        dp = [0] * (target + 1)
        dp[0] = 1
    
        for num in arr:
            for s in range(target, num - 1, -1):
                dp[s] += dp[s - num]
    
        return dp[target]


        
