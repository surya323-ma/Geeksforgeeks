You are given a 2D matrix mat[][] of size n x m. The task is to modify the matrix such that if mat[i][j] is 0, all the elements in the i-th row and j-th column are set to 0.
class Solution:
    def setMatrixZeroes(self, mat):
        n, m = len(mat), len(mat[0])
        first_row_zero = any(mat[0][j] == 0 for j in range(m))
        first_col_zero = any(mat[i][0] == 0 for i in range(n))
        
        # Use first row and column as markers
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][j] == 0:
                    mat[i][0] = mat[0][j] = 0
        
        # Zero out cells based on markers
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0

        # Zero first row and column if flagged
        if first_row_zero:
            for j in range(m):
                mat[0][j] = 0
        if first_col_zero:
            for i in range(n):
                mat[i][0] = 0
