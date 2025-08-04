Given a 2D matrix mat[][] with dimensions n×m. Find the maximum possible sum of any submatrix within the given matrix.

class Solution:
    def maxRectSum(self, mat):
        # code here
   
        n = len(mat)
        m = len(mat[0])
        maxSum = float('-inf')

        for left in range(m):
            temp = [0] * n
            for right in range(left, m):
                for i in range(n):
                    temp[i] += mat[i][right]

            # Apply Kadane's algorithm on temp[]
                curr_sum = temp[0]
                max_curr = temp[0]
                for i in range(1, n):
                    curr_sum = max(temp[i], curr_sum + temp[i])
                    max_curr = max(max_curr, curr_sum)

                maxSum = max(maxSum, max_curr)

        return maxSum   
