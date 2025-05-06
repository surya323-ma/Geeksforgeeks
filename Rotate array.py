Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.

  #User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        n=len(arr)
        d=d%n
        def reverse(arr,start,end):
            while start<end:
                arr[start],arr[end]=arr[end],arr[start]
                start+=1
                end-=1
        reverse(arr,0,d-1)
        reverse(arr,d,n-1)
        reverse(arr,0,n-1)
        
        
        #Your code here
Approach:
This algorithm uses reversal technique to rotate the array efficiently. The steps are:
- Reverse the first d elements.
- Reverse the remaining elements from index d to n-1.
- Reverse the entire array to restore correct order.
This ensures that elements are correctly shifted to the left in O(n) time complexity without needing extra space.
Complexity Analysis:
- Time Complexity: O(n) – Each reversal takes linear time, so overall it remains linear.
- Space Complexity: O(1) – Since the reversal happens in place, no extra space is used.
This is an optimal approach compared to brute-force shifting elements one by one (O(nd) in worst case).
