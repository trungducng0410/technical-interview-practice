class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1) if not count result array
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        start = self.findSmallestAbsIndex(nums)
        res.append(nums[start] ** 2)

        left, right = start - 1, start + 1

        while left >= 0 and right < len(nums):
            if abs(nums[left]) < abs(nums[right]):
                res.append(nums[left] ** 2)
                left -= 1
            else:
                res.append(nums[right] ** 2)
                right += 1

        while left >= 0:
            res.append(nums[left] ** 2)
            left -= 1

        while right < len(nums):
            res.append(nums[right] ** 2)
            right += 1

        return res

    # Can replace by find first positive number
    def findSmallestAbsIndex(self, nums):
        smallestIndex = 0
        for i in range(1, len(nums)):
            if abs(nums[i]) < abs(nums[smallestIndex]):
                smallestIndex = i
        return smallestIndex


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1) if not count result array
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        left, right = 0, len(nums) - 1
        i = len(nums) - 1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left] ** 2
                left += 1
            else:
                res[i] = nums[right] ** 2
                right -= 1

            i -= 1

        return res
