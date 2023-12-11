# DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        total = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    total += 1
                    self.visit(grid, i, j)

        return total

    def visit(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0":
            return

        grid[i][j] = "0"
        self.visit(grid, i - 1, j)
        self.visit(grid, i + 1, j)
        self.visit(grid, i, j - 1)
        self.visit(grid, i, j + 1)


# BFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    self.bfs(grid, visited, r, c)
                    islands += 1

        return islands

    def bfs(self, grid, visited, r, c):
        q = collections.deque()
        visited.add((r, c))
        q.append((r, c))

        while q:
            row, col = q.popleft()
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if r in range(len(grid)) and c in range(len(grid[0])) and grid[r][c] == "1" and (r, c) not in visited:
                    q.append((r, c))
                    visited.add((r, c))
