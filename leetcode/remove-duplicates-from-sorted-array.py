class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        while j < len(nums):
            while j < len(nums) and nums[i] == nums[j]:
                j += 1

            if j >= len(nums):
                break

            nums[i + 1], nums[j] = nums[j], nums[i + 1]
            i += 1
            j += 1

        return i + 1


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1

        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1

        return i
