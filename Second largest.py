Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest elemen

#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        if len(arr)<2:
            return-1
        first,second=float('-inf'),float('-inf')
        for num in arr:
            if num>first:
                second = first
                first = num 
            elif num > second and num !=first:
                second = num
        return second if second !=float('-inf') else -1
