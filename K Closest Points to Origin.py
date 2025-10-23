Given an integer k and an array of points points[][], where each point is represented as points[i] = [xi, yi] on the X-Y plane. Return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance, defined as:
distance = sqrt( (x2 - x1)2 + (y2 - y1)2 )
Note: You can return the k closest points in any order, the driver code will print them in sorted order.
Test Cases are generated such that there will be a unique ans.
class Solution:
    def kClosest(self, points, k):
        import heapq
        heap = [(x**2 + y**2, [x, y]) for x, y in points]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
