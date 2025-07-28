A beautiful matrix is defined as a square matrix in which the sum of elements in every row and every column is equal. Given a square matrix mat[][], your task is to determine the minimum number of operations required to make the matrix beautiful.
In one operation, you are allowed to increment the value of any single cell by 1.
#code here
class Solution:
    def balanceSums(self, mat):
        n = len(mat)
        total = 0
        max_val = float('-inf')
        arr = []

        for i in range(n):
            row_sum = 0
            col_sum = 0
            for j in range(n):
                row_sum += mat[i][j]
                col_sum += mat[j][i]
            arr.append(-row_sum)
            max_val = max(max_val, row_sum, col_sum)

        for el in arr:
            total += el + max_val

        return total
     
