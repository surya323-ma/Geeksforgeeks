Consider a rat placed at position (0, 0) in an n x n square matrix maze[][]. The rat's goal is to reach the destination at position (n-1, n-1). The rat can move in four possible directions: 'U'(up), 'D'(down), 'L' (left), 'R' (right).

The matrix contains only two possible values:

0: A blocked cell through which the rat cannot travel.
1: A free cell that the rat can pass through.
Your task is to find all possible paths the rat can take to reach the destination, starting from (0, 0) and ending at (n-1, n-1), under the condition that the rat cannot revisit any cell along the same path. Furthermore, the rat can only move to adjacent cells that are within the bounds of the matrix and not blocked.
If no path exists, return an empty list.

Note: Return the final result vector in lexicographically smallest order.
class Solution:
    def ratInMaze(self, maze):
        n, m = len(maze), len(maze[0])
        if maze[0][0] == 0 or maze[n-1][m-1] == 0:
            return []

        result = []
        visited = [[False] * m for _ in range(n)]
        directions = [('D', 1, 0), ('L', 0, -1), ('R', 0, 1), ('U', -1, 0)]

        def dfs(x, y, path):
            if x == n - 1 and y == m - 1:
                result.append(path)
                return

            visited[x][y] = True
            for move, dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1 and not visited[nx][ny]:
                    dfs(nx, ny, path + move)
            visited[x][y] = False

        dfs(0, 0, "")
        return sorted(result)
