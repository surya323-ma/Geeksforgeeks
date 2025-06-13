Koko is given an array arr[], where each element represents a pile of bananas. She has exactly k hours to eat all the bananas.
Each hour, Koko can choose one pile and eat up to s bananas from it.
If the pile has atleast s bananas, she eats exactly s bananas.
If the pile has fewer than s bananas, she eats the entire pile in that hour.
Koko can only eat from one pile per hour.


Your task is to find the minimum value of s (bananas per hour) such that Koko can finish all the piles within k hours#code here
import math
class Solution:
    def hours_needed(self,arr,x):
        ans=0
        for item in arr:
            ans+=math.ceil(item/x)
        return ans
    
    def kokoEat(self,arr,k):
        l,h=1,max(arr)
        while l<=h:
            mid=(l+h)//2
            if self.hours_needed(arr,mid)>k:
                l=mid+1
            else:
                h=mid-1
        return l
