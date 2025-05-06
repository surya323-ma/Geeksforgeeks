Given an array of integers arr[] in a circular fashion. Find the maximum subarray sum that we can get if we assume the array to be circular.

java code


class Solution {

    // a: input array
    // n: size of array
    // Function to find maximum circular subarray sum.
    public int circularSubarraySum(int arr[]) {
        int n =arr.length;
        int mini=Integer.MAX_VALUE,maxi=Integer.MIN_VALUE;
        int total=0,sum1=0,sum2=0;
        for(int i=0;i<n;i++){
            total+=arr[i];
            sum1=Math.max(arr[i],arr[i]+sum1);
            maxi=Integer.max(maxi,sum1);
            sum2=Math.min(arr[i],arr[i]+sum2);
            mini=Math.min(mini,sum2);
        }
    return Math.max(maxi,total-mini);

        // Your code here
    }
}

python 3
class Solution:
    def circularSubarraySum(self, arr):
        n = len(arr)
        mini, maxi = float('inf'), float('-inf')
        total, sum1, sum2 = 0, 0, 0
        
        for num in arr:
            total += num
            sum1 = max(num, num + sum1)
            maxi = max(maxi, sum1)
            sum2 = min(num, num + sum2)
            mini = min(mini, sum2)
        
        return max(maxi, total - mini) if maxi > 0 else maxi  # Handling all-negative case

Approach:
- Kadane’s Algorithm is used twice:
- Find the maximum subarray sum (maxi) in normal order.
- Find the minimum subarray sum (mini) to determine the minimum contribution.
- Calculate total sum (total) of the array.
- Compute total - mini to check circular possibilities.
- Return the maximum of maxi and total - mini.
Complexity Analysis:
- Time Complexity: O(n) – Single pass through the array.
- Space Complexity: O(1) – No additional data structures.
This ensures an efficient approach to solving circular subarrays.
