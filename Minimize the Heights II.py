Given an array arr[] denoting heights of N towers and a positive integer K.

For each tower, you must perform exactly one of the following operations exactly once.

Increase the height of the tower by K
Decrease the height of the tower by K
Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

You can find a slight modification of the problem here.
Note: It is compulsory to increase or decrease the height by K for each tower. After the operation, the resultant array should not contain any negative integers.


  #User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        arr.sort()
        n=len(arr)
        maxi=arr[n-1]-k
        mini=arr[0]+k
        diff=arr[n-1]-arr[0]
        for i in range(1,n):
            if(arr[i]-k)<0:
                continue
            largest=max(maxi,arr[i-1]+k)
            smalles=min(mini,arr[i]-k)
            diff=min(diff,largest-smalles)
        return diff
        # code here
Approach:
This algorithm efficiently minimizes the difference between the maximum and minimum values of an array after adding or subtracting k from each element. The steps are:
- Sort the array to easily access minimum and maximum values.
- Initialize maxi and mini, which represent adjusted values after modifying extreme elements.
- Compute initial difference (diff = arr[n-1] - arr[0]).
- Iterate through the array, updating largest and smallest:
- Skip modifications if arr[i] - k becomes negative.
- Find the new largest and smallest values after modification.
- Update diff to maintain the smallest possible range.
Complexity Analysis:
- Time Complexity: O(n log n) – The sorting step dominates the complexity.
- Space Complexity: O(1) – Modifications happen in place without extra storage.
This approach ensures an optimized and efficient solution to minimize the height difference
