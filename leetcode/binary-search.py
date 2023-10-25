# Binary search iteratively
# Time complexity: O(logn)
# Space complexity: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1


# Binary search recursively
# Time complexity: O(logn)
# Space complexity: O(logn) - stack call
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def searchRecursive(nums, target, left, right):
            if left > right:
                return -1

            mid = (left + right) // 2

            if nums[mid] > target:
                return searchRecursive(nums, target, left, mid - 1)
            elif nums[mid] < target:
                return searchRecursive(nums, target, mid + 1, right)
            else:
                return mid

        return searchRecursive(nums, target, 0, len(nums) - 1)
