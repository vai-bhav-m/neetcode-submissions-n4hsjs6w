from collections import deque
class Solution:
    def get_neighbors(self, m, n, i, j):
        res = []
        # Check all 4 adjacent cells (up, down, left, right)
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < m and 0 <= nj < n:
                res.append((ni, nj))
        return res

    def bfs(self, visited, grid, i, j):
        q = deque()
        q.append((i, j))
        visited.add((i, j))
        m, n = len(grid), len(grid[0])
        while q:
            curr_node = q.popleft()
            neighs = self.get_neighbors(m, n, curr_node[0], curr_node[1])
            for child in neighs:
                if child not in visited and grid[child[0]][child[1]] == 1:
                    visited.add(child)
                    q.append(child)

        return visited

    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        for i in range(m):
            for j in range(n):
                if (i,j) in visited:
                    continue
                if grid[i][j] == 0:
                    visited.add((i,j))
                else:
                    curr_len = len(visited)
                    visited = self.bfs(visited, grid, i, j)
                    max_area = max(max_area, len(visited)-curr_len)
                
        return max_area