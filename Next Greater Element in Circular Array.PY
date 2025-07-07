Given a circular integer array arr[], the task is to determine the next greater element (NGE) for each element in the array.

The next greater element of an element arr[i] is the first element that is greater than arr[i] when traversing circularly. If no such element exists, return -1 for that position.

Circular Property:

Since the array is circular, after reaching the last element, the search continues from the beginning until we have looked at all elements once.

class Solution:
    def nextLargerElement(self, arr):
       #code here 
        n = len(arr)
        result = [-1]*n
        stack = []
        
        for i in range(2*n-1,-1,-1):
            while stack and stack[-1]<=arr[i%n]:
               stack.pop()
            result[i%n] = stack[-1] if stack else -1
            stack.append(arr[i%n])
        return result


