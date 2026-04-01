Given a positive integer n, count all possible distinct binary strings of length n such that there are no consecutive 1’s.
class Solution:
	def countStrings(self,n):
    	# code here
    	a, b = 1, 1
    	for _ in range(n+1):
    	    a, b = b, a+b
        return a
