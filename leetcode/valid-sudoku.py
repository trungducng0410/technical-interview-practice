import collections


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        # Check row
        # O(n^2)
        for i in range(n):
            if self.isValidRow(board[i]) == False:
                return False

        # Check col
        # O(n ^ 2)
        for i in range(n):
            col = []
            for j in range(n):
                col.append(board[j][i])
            if self.isValidCol(col) == False:
                return False

        # Check box
        # O(n ^ 2)
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                firstRow = [board[i][j], board[i][j + 1], board[i][j + 2]]
                secondRow = [board[i + 1][j], board[i + 1]
                             [j + 1], board[i + 1][j + 2]]
                thirdRow = [board[i + 2][j], board[i + 2]
                            [j + 1], board[i + 2][j + 2]]
                box = [firstRow, secondRow, thirdRow]

                if self.isValidBox(box) == False:
                    return False

        return True

    def isValidArr(self, arr):
        nums = set()
        for n in arr:
            if n != "." and n in nums:
                return False
            else:
                nums.add(n)
        return True

    def isValidRow(self, row):
        return self.isValidArr(row)

    def isValidCol(self, col):
        return self.isValidArr(col)

    def isValidBox(self, box):
        nums = set()
        for row in box:
            for n in row:
                if n != "." and n in nums:
                    return False
                else:
                    nums.add(n)
        return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                cur = board[r][c]

                if cur == ".":
                    continue

                if cur in rows[r] or cur in cols[c] or cur in boxes[(r // 3, c // 3)]:
                    return False

                cols[c].add(cur)
                rows[r].add(cur)
                boxes[(r // 3, c // 3)].add(cur)

        return True
