You are given two integer arrays a[] and b[] of equal size. A sum combination is formed by adding one element from a[] and one from b[], using each index pair (i, j) at most once. Return the top k maximum sum combinations, sorted in non-increasing order.
class Solution:
     def topKSumPairs(self, a, b, k):
        from heapq import heapify, heappop, heappush
        n = len(a)
        # Build-in heap is a minheap, so we negate arrays
        for i in range(n):
            a[i] *= -1
            b[i] *= -1
        a.sort()
        b.sort()
        h = [(a[i] + b[0], i, 0) for i in range(n)]
        heapify(h)
        output = []
        while len(output) < k:
            min_sum, i, j = heappop(h)
            output.append(-min_sum)
            if j < n - 1:
                heappush(h, (a[i] + b[j + 1], i, j + 1))
        return output
 #code heere 

import heapq

class Solution:
    def topKSumPairs(self, a, b, k):
        n = len(a)
        a.sort(reverse=True)
        b.sort(reverse=True)

        max_heap = []
        visited = set()

        # Start with the largest possible sum
        heapq.heappush(max_heap, (-(a[0] + b[0]), 0, 0))
        visited.add((0, 0))

        output = []

        while len(output) < k and max_heap:
            current_sum, i, j = heapq.heappop(max_heap)
            output.append(-current_sum)

            # Move to next element in a[]
            if i + 1 < n and (i + 1, j) not in visited:
                heapq.heappush(max_heap, (-(a[i + 1] + b[j]), i + 1, j))
                visited.add((i + 1, j))

            # Move to next element in b[]
            if j + 1 < n and (i, j + 1) not in visited:
                heapq.heappush(max_heap, (-(a[i] + b[j + 1]), i, j + 1))
                visited.add((i, j + 1))

        return output
