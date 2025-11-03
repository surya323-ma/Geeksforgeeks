Given a directed graph with V vertices numbered from 0 to V-1 and E directed edges, represented as a 2D array edges[][], where each element edges[i] = [u, v] represents a directed edge from vertex u to vertex v. Return all Safe Nodes of the graph.
A vertex with no outgoing edges is called a terminal node. A vertex is considered safe if every path starting from it eventually reaches a terminal node.
from collections import defaultdict, deque
class Solution:
    def safeNodes(self, V, edges):
        # Code here
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
    # 0 = unvisited, 1 = visiting, 2 = safe
        state = [0] * V
        def dfs(node):
            if state[node] != 0:
                return state[node] == 2
            state[node] = 1  # mark as visiting
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            state[node] = 2  # mark as safe
            return True

        return [i for i in range(V) if dfs(i)]
