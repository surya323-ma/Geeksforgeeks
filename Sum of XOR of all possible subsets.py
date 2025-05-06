Given an array arr[], return the sum of the XOR of all elements for every possible subset of the array. Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

Note: The answer is guaranteed to fit within a 32-bit integer.


#User function Template for python3
class Solution:
    def subsetXORSum(self, arr):
        n=len(arr)
        result=0
        for i in range(32):
            count=0
            for num in arr:
                if num & (1<<i):
                    count+=1
            if count>0:
                result+=(1<<i)*(2**(n-1))
        return result# code here

Complexity Analysis:
- Time Complexity: O(32 * N) ≈ O(N) (since 32 is constant, iterating through all bits)
- Space Complexity: O(1) (only a few variables are used
Your approach efficiently calculates the sum of all subset XORs in a given array by leveraging bitwise operations.
Understanding the Approach:
- You iterate through each bit position (0 to 31), counting how many numbers in arr have the bit set.
- If a bit is present in any number, it contributes to the final XOR sum.
- Since each element participates in 2^(n-1) subsets, the contribution of each bit position is multiplied accordingly.
