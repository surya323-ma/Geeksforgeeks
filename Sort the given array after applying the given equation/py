Given an integer array arr[] sorted in ascending order, along with three integers: A, B, and C. The task is to transform each element x in the array using the quadratic function A*(x2) + B*x + C. After applying this transformation to every element, return the modified array in sorted order.

class Solution:
	def sortArray(self, arr, A, B, C):
		# Code here
		arr = [self.fun(A,B,C,x) for x in arr]
		return sorted(arr)
		
	def fun(self,a,b,c,n):
		eq = (a*(n**2)) + (b*n) + c
		return eq
