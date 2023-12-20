class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, alt = set(), set()

        def dfs(r, c, visit, prevH):
            if (r, c) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prevH:
                return

            visit.add((r, c))

            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, 0)
            dfs(ROWS - 1, c, alt, 0)

        for r in range(ROWS):
            dfs(r, 0, pac, 0)
            dfs(r, COLS - 1, alt, 0)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in alt:
                    res.append([r, c])

        return res
