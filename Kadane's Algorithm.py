Given an integer array arr[]. You need to find the maximum sum of a subarray.
java code


// User function Template for Java
class Solution {

    // arr: input array
    // Function to find the sum of contiguous subarray with maximum sum.
    int maxSubarraySum(int[] arr) {
        int max=Integer.MIN_VALUE;
        int sum=0;
        for (int i=0;i<arr.length;i++){
            sum+=arr[i];
            max=Math.max(max,sum);
            if(sum<0){
                sum=0;
            }
        }
        return max;
        // Your code here
    }
}

python 3 code
class Solution:
    def maxSubArraySum(self, arr):
        max_sum = float('-inf')
        curr_sum = 0
        for num in arr:
            curr_sum += num
            max_sum  = max(max_sum , curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        return max_sum
        # Your code here
