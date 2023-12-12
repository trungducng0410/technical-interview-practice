class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        time = 0
        fresh = 0

        q = collections.deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if not q:
            return -1 if fresh > 0 else 0

        while q:
            time += 1
            n = len(q)
            for i in range(n):
                r, c = q.popleft()

                grid[r][c] = 2

                # Left
                if c > 0 and grid[r][c - 1] == 1 and (r, c - 1) not in visited:
                    q.append((r, c - 1))
                    visited.add((r, c - 1))
                    fresh -= 1

                # Right
                if c < cols - 1 and grid[r][c + 1] == 1 and (r, c + 1) not in visited:
                    q.append((r, c + 1))
                    visited.add((r, c + 1))
                    fresh -= 1

                # Top
                if r > 0 and grid[r - 1][c] == 1 and (r - 1, c) not in visited:
                    q.append((r - 1, c))
                    visited.add((r - 1, c))
                    fresh -= 1

                # Bottom
                if r < rows - 1 and grid[r + 1][c] == 1 and (r + 1, c) not in visited:
                    q.append((r + 1, c))
                    visited.add((r + 1, c))
                    fresh -= 1

        return time - 1 if fresh == 0 else -1


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        time, fresh = 0, 0
        queue = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while queue and fresh > 0:
            length = len(queue)
            for i in range(length):
                row, col = queue.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                        grid[r][c] = 2
                        queue.append((r, c))
                        fresh -= 1

            time += 1

        return time if fresh == 0 else -1
