You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.

class Solution:
    def pushZerosToEnd(self,arr):
        n=len(arr)
        left = 0
        for right in range(n):
            if arr[right] !=0:
                arr[left],arr[right]=arr[right],arr[left]
                left +=1
