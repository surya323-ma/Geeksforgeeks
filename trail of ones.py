Given an integer n, the task is to count the number of binary strings of length n that contains at least one pair of consecutive 1's.
Note: A binary string is a sequence made up of only 0's and 1's.
#code here
class Solution:
    def countConsec(self, n: int) -> int:
        # code here
        # Compute 2^n using bit shifting
        total = 1 << n 

        # Intial 2 values 
        tmp1, tmp2 = 1, 2
        # Compute n_th  terms of Fibonacci
        for i in range(2, n+1):
            tmp1, tmp2 = tmp2, tmp1 + tmp2
        return total - tmp2
