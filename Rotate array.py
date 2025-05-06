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
