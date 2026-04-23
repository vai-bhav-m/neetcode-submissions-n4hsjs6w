from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def get_children(i ,j, m, n):
            dels = [(-1,0), (1,0), (0,1), (0,-1)]
            children = []
            for dx, dy in dels:
                if 0 <= (i + dx) < m and 0 <= (j + dy) < n:
                    children.append((i+dx, j+dy))
            return children

        def dfs(node, visited, grid):
            m, n = len(grid), len(grid[0])
            stack = deque()
            stack.append(node)
            visited.add(node)
            while stack:
                pos = stack.pop()
                children = get_children(pos[0], pos[1], m, n)
                for child in children:
                    if child not in visited and grid[child[0]][child[1]] == "1":
                        stack.append(child)
                        visited.add(child)
            return visited
        
        m, n = len(grid), len(grid[0])
        n_islands = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    visited = dfs((i,j), visited, grid)
                    n_islands += 1
        return n_islands
