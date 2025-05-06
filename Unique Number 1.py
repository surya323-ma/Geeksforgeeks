Given a unsorted array arr[] of positive integers having all the numbers occurring exactly twice, except for one number which will occur only once. Find the number occurring only once

class Solution:
    def findUnique(self, arr):
        unique_num=0
        for num in arr:
            unique_num ^= num
        return unique_num
        # code here 
Your approach leverages the XOR (^) bitwise operation to efficiently find the unique number in an array where every other number appears twice.
