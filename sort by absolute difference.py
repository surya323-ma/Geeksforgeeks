You are given a number x and array arr[]. Your task is to rearrange the elements of the array according to the absolute difference with x, i.e., an element having minimum difference comes first, and so on.
Note: If two or more elements are at equal distances arrange them in the same sequence as in the given array.
class Solution:
    def rearrange(self, arr, x):
            arr.sort(key=lambda m:abs(m-x))
            return arr
        # code here
        
