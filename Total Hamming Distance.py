Given an integer array arr[], return the sum of Hamming distances between all the pairs of the integers in arr.

Note: The answer is guaranteed to fit within a 32-bit integer.


#User function Template for python3
class Solution:
    def totHammingDist(self, arr):
        total=0
        for bit in range(31):
            ones=0
            zeros=0
            for val in arr:
                if(val >> bit)& 0x1:
                    ones +=1
                else:
                    zeros +=1
            total += ones*zeros
        return total
       
