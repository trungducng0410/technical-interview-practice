class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        maxA = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxA = max(maxA, self.dfs(grid, 0, r, c))

        return maxA

    def dfs(self, grid, area, r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
            return area

        grid[r][c] = 0
        area += 1

        area = self.dfs(grid, area, r - 1, c)
        area = self.dfs(grid, area, r + 1, c)
        area = self.dfs(grid, area, r, c - 1)
        area = self.dfs(grid, area, r, c + 1)

        return area


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        maxA = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxA = max(maxA, self.dfs(grid, r, c))

        return maxA

    def dfs(self, grid, r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
            return 0

        grid[r][c] = 0

        return 1 + self.dfs(grid, r - 1, c) + self.dfs(grid, r + 1, c) + self.dfs(grid, r, c - 1) + self.dfs(grid, r, c + 1)
