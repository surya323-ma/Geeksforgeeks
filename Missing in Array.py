You are given an array arr[] of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). This array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify and return the missing element.
class Solution:
    def missingNum(self, arr):
        # code here
        n = len(arr) + 1
        tot = n * (n + 1) >> 1
        return tot - sum(arr)


Your approach is based on the mathematical formula for the sum of the first ( n ) natural numbers:
[ S = \frac{n(n+1)}{2} ]
Since one number is missing in the given array, you calculate the expected total sum of numbers from 1 to ( n ) and subtract the sum of the array elements to find the missing number.
Explanation of the Approach:
- Calculate the expected sum of numbers from 1 to n using the formula.
- Compute the actual sum of the elements present in the array.
- The missing number is simply the difference between the expected sum and the actual sum.
Optimization:
- This approach runs in O(n) time complexity and O(1) space complexity, making it efficient for large inputs.
- Using the bitwise right shift (>> 1) instead of division by 2 is an optimization trick, but using // 2 for clarity might be preferable.
