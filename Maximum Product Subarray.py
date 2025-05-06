Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr[].

Note: It is guaranteed that the output fits in a 32-bit integ
#User function Template for python3
class Solution:

    # Function to find maximum
    # product subarray
    def maxProduct(self,arr):
        res=max(arr)
        currMax,currMin=1,1
        for i in range(len(arr)):
            if arr[i]<0:
                currMax,currMin=currMin,currMax
            currMax=max(arr[i]*currMax,arr[i])
            currMin=min(arr[i]*currMin,arr[i])
            res=max(res,currMax)
        return res
        # code here
Approach:
This algorithm finds the maximum product subarray efficiently using dynamic programming and tracking local minima/maxima. The key steps are:
- Initialize currMax and currMin to track the max/min product ending at each index.
- Iterate through the array, updating:
- Swap currMax and currMin if a negative number is encountered (since multiplication by negative flips sign).
- Update currMax and currMin using the current element's product.
- Track the maximum result encountered so far.
Complexity Analysis:
- Time Complexity: O(n) – The entire array is scanned once.
- Space Complexity: O(1) – Only a few variables are maintained.
This method is more efficient than brute force (O(n²)) and avoids unnecessary nested loops
