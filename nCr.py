Given two integer values n and r, the task is to find the value of Binomial Coefficient nCr

A binomial coefficient nCr can be defined as the coefficient of xr in the expansion of (1 + x)n that gives the number of ways to choose r objects from a set of n objects without considering the order.
The binomial coefficient nCr is calculated as : C(n,r) = n! / r! * (n-r) !
Note: If r is greater than n, return 0.
It is guaranteed that the value of nCr will fit within a 32-bit integer.\


class Solution:
    def nCr(self, n, r):
        # code here
        def factorial(n):
            result = 1
            for i in range(2, n+1):
                result *= i
            return result
            
        if r > n:
            return 0
        return factorial(n) // (factorial(r) * factorial(n-r))
