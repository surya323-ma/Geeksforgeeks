You are given a 2D matrix mat[][] of size n x m that was initially filled in the following manner:
Each row is sorted in increasing order from left to right.
The first element of every row is greater than the last element of the previous row.
This implies that if the matrix is flattened row-wise, it forms a strictly sorted 1D array.
Later, this sorted 1D array was rotated at some unknown pivot. The rotated array was then written back into the matrix row-wise to form the current matrix.
Given such a matrix mat[][] and an integer x, determine whether x exists in the matrix.
class Solution:
   def searchMatrix(self, mat, x):
        for arr in mat:
            if arr[-1]<arr[0]:
                if x in arr:
                    return True
            elif x>=arr[0] and x<=arr[-1]:
                if x in arr:
                    return True
        return False
