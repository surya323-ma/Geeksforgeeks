You are given an undirected connected graph with V vertices numbered from 0 to V-1 and E edges, represented as a 2D array edges[][], where each element edges[i] = [u, v] represents an undirected edge between vertex u and vertex v.
Find the diameter of the graph.
The diameter of a graph (sometimes called the width) is the number of edges on the longest path between two vertices in the graph.

Note: Graph do not contains any cycle.
from collections import deque

class Solution:
    def diameter(self, V, edges):
        # Build adjacency list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # BFS to find farthest node and its distance
        def bfs(start):
            dist = [-1] * V
            dist[start] = 0
            q = deque([start])
            far_node = start

            while q:
                curr = q.popleft()
                for neighbor in adj[curr]:
                    if dist[neighbor] == -1:
                        dist[neighbor] = dist[curr] + 1
                        q.append(neighbor)
                        far_node = neighbor  # last updated will be farthest
            return far_node, dist[far_node]

        # First BFS to find one endpoint of the diameter
        far_node, _ = bfs(0)
        # Second BFS from far_node to get the diameter
        _, diameter = bfs(far_node)

        return diameter
