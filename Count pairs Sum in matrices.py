Given two matrices mat1[][] and mat2[][] of size n x n, where the elements in each matrix are arranged in strictly ascending order. Specifically, each row is sorted from left to right, and the last element of a row is smaller than the first element of the next row.
You're given a target value x, your task is to find and count all pairs {a, b} such that a is from mat1 and b is from mat2 where the sum of a + b is equal to x.
#code here
class Solution:
	def countPairs(self, mat1, mat2, x):
    # Flatten matrices
        list1 = [num for row in mat1 for num in row]
        list2 = [num for row in mat2 for num in row]
        # Two-pointer approach
        i, j = 0, len(list2) - 1
        count = 0
        while i < len(list1) and j >= 0:
            total = list1[i] + list2[j]
            if total == x:
                count += 1
                i += 1
                j -= 1
            elif total < x:
                i += 1
            else:
                j -= 1
        return count
