You are given a sorted array arr[] of unique integers, an integer k, and a target value x. Return exactly k elements from the array closest to x, excluding x if it exists.

An element a is closer to x than b if:
|a - x| < |b - x|, or
|a - x| == |b - x| and a > b (i.e., prefer the larger element if tied)
Return the k closest elements in order of closeness.

#cde here
from heapq import *
class Solution:
    def printKClosest(self, arr, k, x):
        heap=[]
        for i in arr:
            if i==x:
                continue
            heappush(heap,(abs(i-x),-i))
        res=[]
        while(heap and k):
            _,val=heappop(heap)
            res.append(-val)
            k-=1
        return res
