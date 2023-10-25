# Time complexity: O(logm + logn)
# Space complexity: O(m)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        firstCol = [row[0] for row in matrix]

        rowIndexes = self.binarySearchNearest(firstCol, target)

        coordinates = {}
        for i in rowIndexes:
            coordinates[i] = self.binarySearchNearest(matrix[i], target)

        for row, cols in coordinates.items():
            for col in cols:
                if matrix[row][col] == target:
                    return True

        return False

    def binarySearchNearest(self, nums, target):
        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                return [mid]

        return [left, right]


# Time complexity: O(logm + logn)
# Space complexity: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        top, bot = 0, m - 1
        while top <= bot:
            row = (top + bot) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2

        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2

            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True

        return False
