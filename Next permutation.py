Given an array of integers arr[] representing a permutation, implement the next permutation that rearranges the numbers into the lexicographically next greater permutation. If no such permutation exists, rearrange the numbers into the lowest possible order (i.e., sorted in ascending order). 

Note - A permutation of an array of integers refers to a specific arrangement of its elements in a sequence or linear order.
#User function Template for python3

class Solution:
    def nextPermutation(self, arr):
        n=len(arr)
        if n<=1:
            return arr
        i=n-2
        while i>=0 and arr[i]>=arr[i+1]:
            i-=1
        if i >=0:
            j=n-1
            while arr[j]<=arr[i]:
                j-=1
            arr[i],arr[j]=arr[j],arr[i]
        arr[i+1:]=reversed(arr[i+1:])
            
        # code here
Approach:
This algorithm finds the next lexicographical permutation of the given array using the following steps:
- Find the first decreasing element from the right (i.e., arr[i] < arr[i+1]).
- Swap it with the smallest element on the right that is greater than arr[i].
- Reverse the remaining part after i to get the smallest lexicographical order.
This ensures that we transition to the next permutation in O(n) time without generating all permutations.
Complexity Analysis:
- Time Complexity: O(n) – Finding i + finding j + reversing the suffix all take linear time.
- Space Complexity: O(1) – No extra space is used; modifications happen in-place.
This is an efficient method for computing the next permutation without excessive computation
