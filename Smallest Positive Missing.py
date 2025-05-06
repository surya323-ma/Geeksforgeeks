You are given an integer array arr[]. Your task is to find the smallest positive number missing from the array.

Note: Positive number starts from 1. The array can have negative integers too.

#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        n=len(arr)
        for i in range(0,n):
            while((arr[i]>0 and arr[i]<=n)and arr[i]<=n and arr[arr[i]-1] !=arr[i]):
                arr[arr[i]-1],arr[i]=arr[i],arr[arr[i]-1]
        
        for i in range(0,n):
            if arr[i]!=i+1:
                return i+1
        return n+1

Your approach is based on the Cyclic Sort technique, which efficiently places each number in its correct position within the array and helps find the missing smallest positive integer.
Approach Explanation:
- Rearrange the Array:
- Traverse the array and place each positive number (within the range 1 to n) in its correct position using a swap operation.
- The swapping ensures that every arr[i] ends up at arr[arr[i]-1] if possible.
- Find the Missing Number:
- After sorting, traverse the array again and find the first index i where arr[i] != i+1, which means i+1 is the missing number.
- If all numbers are in their correct positions, return n+1, which is the smallest missing number outside the array.
Time Complexity:
- O(n) due to a single pass rearrangement and another pass to find the missing number.
Space Complexity:
- O(1) since sorting is done in-place without extra space.


