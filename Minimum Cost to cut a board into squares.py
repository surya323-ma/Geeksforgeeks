Given a board of dimensions n × m that needs to be cut into n*m squares. The cost of making a cut along a horizontal or vertical edge is provided in two arrays:

x[]: Cutting costs along the vertical edges (length-wise).
y[]: Cutting costs along the horizontal edges (width-wise).
Find the minimum total cost required to cut the board into squares optimally.
class Solution:
    def minCost(self, n, m, x, y):
        x.sort(reverse=True)
        y.sort(reverse=True)
        h_segments = 1  # horizontal pieces
        v_segments = 1  # vertical pieces
        i = j = 0
        total_cost = 0

        while i < len(x) and j < len(y):
            if x[i] > y[j]:
                total_cost += x[i] * h_segments
                v_segments += 1
                i += 1
            else:
                total_cost += y[j] * v_segments
                h_segments += 1
                j += 1
        while i < len(x):
            total_cost += x[i] * h_segments
            i += 1
        while j < len(y):
            total_cost += y[j] * v_segments
            j += 1

        return total_cost    # code here
