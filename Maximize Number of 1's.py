Given a binary array arr[] containing only 0s and 1s and an integer k, you are allowed to flip at most k 0s to 1s. Find the maximum number of consecutive 1's that can be obtained in the array after performing the operation at most k times.
class Solution:
    # k is the maximum number of zeros allowed to flip
    def maxOnes(self, arr, k):
        start=0
        end=0
        res=0
        c=0
        while end<len(arr):
            if arr[end]==0:
                c+=1
            while c>k:
                if arr[start]==0:
                    c-=1
                start+=1
            res=max(res,end-start+1)
            end+=1
        return res
        # code here
