given a matrix mat[][] of size n*n, where each row and column is sorted in non-decreasing order. Find the kth smallest element in the matrix.#code here
import heapq
class Solution:
    def kthSmallest(self, matrix, k):
        n=len(matrix)
        min_heap = []
    
    # Add the first element of each row (smallest in each row)
        for i in range(n):
            heapq.heappush(min_heap, (matrix[i][0], i, 0))
    
    # Extract `k` times to get the kth smallest element
        for _ in range(k):
            val, r, c = heapq.heappop(min_heap)
        
        # If there's a next column in the same row, add it to the heap
            if c + 1 < n:
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))
        return val
