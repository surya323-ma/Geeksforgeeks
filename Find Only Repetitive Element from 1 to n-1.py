
Given an array arr[] of size n, filled with numbers from 1 to n-1 in random order. The array has only one repetitive element. Your task is to find the repetitive element.

Note: It is guaranteed that there is a repeating element present in the array

#User function Template for python3
class Solution:
    def findDuplicate(self, arr):
        freq={}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i] = 1
        for i, count in freq.items():
            if count == 2:
                return i 
                
        #code here

